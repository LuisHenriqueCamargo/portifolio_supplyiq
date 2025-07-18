from sqlalchemy import create_engine
import pandas as pd

excel_path = r"F:\Abastecimento_Supply\data\abastecimento.xlsx"

connection_string = (
    "mssql+pyodbc://@localhost\\SQLEXPRESS/supplyiq"
    "?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"


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
