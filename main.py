import psycopg2
import csv

connect = psycopg2.connect(database="SRAG", user="postgres", password="postgres123", host="localhost", port="5432")


with open('INFLUD20-01-05-2023.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # Pula a primeira linha

    for row in reader:
        cur = connect.cursor()
        
        query = "INSERT INTO dados (data, estado, municipio, obito, sexo, idade, raca, evolucao, dt_notific, dt_inicio_sintomas, dt_obito, classificacao_final, criterio_confirmacao, criterio_obito, status_notificacao, municipio_notificacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        row[3] = int (row[3])
        row[5] = int (row[5])
        
        cur.execute(query, row)
        connect.commit()
        
        
cur.close()
connect.close()
