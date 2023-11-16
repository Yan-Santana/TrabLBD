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
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                %s)"
            cur.execute(sql, row)
            
        # tenho que terminar de colocar os outros inserts aqui, ate entao so tem o do paciente
            
    conn.commit()
    cur.close()
    conn.close()