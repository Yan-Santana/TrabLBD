# Arquivo responsável por realizar a conexão com o banco de dados e executar as queries
# Além de ser o indexador do pacote "database"

import psycopg2

DB_NAME = "SRAG"
DB_USER = "postgres"
DB_PASSWORD = "minhasenha"
DB_HOST = "localhost"
DB_PORT = "5433"

def create_connection():
    try:
        conn = psycopg2.connect(
            database = DB_NAME,
            user = DB_USER,
            password = DB_PASSWORD,
            host = DB_HOST,
            port = DB_PORT
        )
        print("Conexão com o banco de dados realizada com sucesso!")
        return conn
    except psycopg2.Error as e:
        print(f"Erro na conexão com o banco de dados: {e}")


def execute_query(connection, query):
    cursor = connection.cursor()
    
    cursor.execute(query)
    
    connection.commit()
    cursor.close()