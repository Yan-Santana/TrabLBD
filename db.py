# Arquivo responsável por realizar a conexão com o banco de dados e executar as queries

import psycopg2

DB_NAME = "SRAG"
DB_USER = "postgres"
DB_PASSWORD = "minhasenha"
DB_HOST = "localhost"
DB_PORT = "5433"

def connect():
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


def execute_query(query):
    conn = connect()
    cur = conn.cursor()
    
    cur.execute(query)
    
    conn.commit()
    cur.close()
    conn.close()

def commit_changes():
    conn = connect()
    conn.commit()
    conn.close()