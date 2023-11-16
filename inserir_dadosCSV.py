# Arquivo responsavel por inserir os dados do arquivo CSV no banco de dados

from db import connect
import csv

def inserir_dados():
    conn = connect()
    cur = conn.cursor()

    with open('entrada.csv', 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader) 
        
        for row in csv_reader:
            sql = "INSERT INTO paciente VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s)"
            cur.execute(sql, row)
            
            sql = "INSERT INTO conclusao VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(sql, row)
            
            sql = "INSERT INTO dados_clinicos VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(sql, row)
            
            sql = "INSERT INTO dados_laboratorial VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(sql, row)
            
            sql = "INSERT INTO notificacao VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(sql, row)
            
            sql = "INSERT INTO residencia VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s)"
            cur.execute(sql, row)
            
            sql = "INSERT INTO dados_atendimento VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s)"
        # tenho que confirmar essa parte ainda 
            
    conn.commit()
    cur.close()
    conn.close()