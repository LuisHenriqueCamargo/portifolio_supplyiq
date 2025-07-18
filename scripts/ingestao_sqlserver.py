from sqlalchemy import create_engine
import pandas as pd

excel_path = r"F:\Abastecimento_Supply\data\abastecimento.xlsx"

connection_string = (
    "mssql+pyodbc://@localhost\\SQLEXPRESS/supplyiq"
    "?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)
engine = create_engine(connection_string)

def ingestao_incremental():
    df_novo = pd.read_excel(excel_path)
    print(f"[INGESTÃO] Dados novos carregados: {df_novo.shape[0]} linhas.")

    try:
        df_existente = pd.read_sql("SELECT * FROM abastecimentos", engine)
        print(f"[BANCO] Registros atuais: {df_existente.shape[0]} linhas.")

        # Eliminar duplicatas com base nas colunas-chave
        df_merged = pd.concat([df_existente, df_novo]).drop_duplicates(subset=["data", "tanque", "posto"], keep="last")
        print(f"[MERGE] Após limpeza: {df_merged.shape[0]} linhas.")
    except:
        # Se a tabela não existir ainda
        df_merged = df_novo
        print("[BANCO] Tabela ainda não existe. Criando nova.")

    # Atualiza a tabela completa ( aqui limpamos as duplicatas antes)
    df_merged.to_sql("abastecimentos", engine, if_exists="replace", index=False)
    print("[INGESTÃO] Dados atualizados com sucesso.")

if __name__ == "__main__":
    ingestao_incremental()
