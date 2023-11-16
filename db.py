# Arquivo responsável por realizar a conexão com o banco de dados e executar as queries

import psycopg2

DB_NAME = "TrabLBD.db"
DB_USER = "postgres"
DB_PASSWORD = "minhasenha"
DB_HOST = "localhost"
DB_PORT = "5433"

def connect():
    conn = psycopg2.connect(
        database = DB_NAME,
        user = DB_USER,
        password = DB_PASSWORD,
        host = DB_HOST,
        port = DB_PORT
    )
    return conn

def execute_query(query):
    conn = connect()
    cur = conn.cursor()
    
    cur.execute(query)
    
    conn.commit()
    cur.commit()
    conn.close()

def commit_changes():
    conn = connect()
    conn.commit()
    conn.close()