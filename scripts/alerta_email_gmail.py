import smtplib
from email.mime.text import MIMEText
import pandas as pd
from sqlalchemy import create_engine

# === CONFIGURAÇÕES GERAIS ===
remetente = "lh.santos2013@gmail.com"  # <- Seu Gmail
senha = "mklj gwkf wauu uzjn"          # <- Senha de app gerada no Gmail
limite_dias = 2
caminho_emails = r"F:\\Abastecimento_Supply\\data\\emails_alerta.xlsx"

# === CONEXÃO COM SQL SERVER ===
engine = create_engine(
    "mssql+pyodbc://@localhost\\SQLEXPRESS/supplyiq"
    "?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

# === CONSULTA TANQUES CRÍTICOS ===
query = f"""
SELECT tanque, autonomia_dias, nivel_risco
FROM vw_tanques_criticos
WHERE nivel_risco = 'Crítico'
"""
try:
    df_alerta = pd.read_sql(query, engine)
except Exception as e:
    print(f"[ERRO] Falha ao consultar SQL Server: {e}")
    exit()

if df_alerta.empty:
    print("[ALERTA] Nenhum tanque crítico. Nenhum e-mail será enviado.")
    exit()

# === LEITURA DE CONTATOS ===
try:
    df_emails = pd.read_excel(caminho_emails, sheet_name="contatos")
except Exception as e:
    print(f"[ERRO] Não foi possível ler a planilha de e-mails: {e}")
    exit()

contatos_ativos = df_emails[df_emails["status"].str.lower() == "ativo"]

# === ENVIO PERSONALIZADO DE ALERTAS ===
for _, contato in contatos_ativos.iterrows():
    nome = contato["nome"]
    email = contato["email"]

    corpo_html = f"""
    <p>Olá <strong>{nome}</strong>,</p>

    <p>Os seguintes tanques estão com nível <strong style="color:red;">CRÍTICO</strong> de autonomia (≤ {limite_dias} dias):</p>

    <pre>{df_alerta.to_string(index=False)}</pre>

    <p><strong>Recomendamos abastecimento imediato.</strong></p>

    <p>Atenciosamente,<br>
    ⛽ SupplyIQ - Monitoramento Inteligente de Abastecimento</p>
    """

    msg = MIMEText(corpo_html, "html")
    msg["Subject"] = "⚠️ Alerta Crítico - Tanques com Baixa Autonomia"
    msg["From"] = remetente
    msg["To"] = email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(remetente, senha)
            server.send_message(msg)
        print(f"[ENVIADO] E-mail enviado para {nome} - {email}")
    except Exception as e:
        print(f"[ERRO] Falha ao enviar para {nome} - {email}: {e}")
