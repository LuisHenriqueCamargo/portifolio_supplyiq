
# === CONSULTA AO BANCO DE DADOS ===
query = f"SELECT * FROM vw_autonomia_tanques WHERE dias_restantes < {limite_dias}"
df_alerta = pd.read_sql(query, engine)

if df_alerta.empty:
    print("[ALERTA] Nenhum tanque em estado crítico.")
    exit()

corpo_alerta = df_alerta.to_string(index=False)

# === LEITURA DOS E-MAILS ATIVOS ===
df_emails = pd.read_excel(caminho_emails, sheet_name="contatos")
contatos_ativos = df_emails[df_emails["status"].str.lower() == "ativo"]

# === ENVIO DE E-MAIL PERSONALIZADO ===
for _, row in contatos_ativos.iterrows():
    nome = row["nome"]
    email = row["email"]

    corpo_msg = f"""
Olá {nome},

Os seguintes tanques estão com menos de {limite_dias} dias de autonomia:

{corpo_alerta}

Atenciosamente,  
SupplyIQ - Monitoramento de Abastecimento
"""

    msg = MIMEText(corpo_msg)
    msg["Subject"] = "⚠️ Alerta Crítico - Tanques com Baixa Autonomia"
    msg["From"] = remetente
    msg["To"] = email

    try:
        with smtplib.SMTP("smtp.office365.com", 587) as server:
            server.starttls()
            server.login(remetente, senha)
            server.send_message(msg)
        print(f"[ENVIADO] E-mail enviado para {nome} - {email}")
    except Exception as e:
        print(f"[ERRO] Falha ao enviar para {nome} - {email}: {e}")
