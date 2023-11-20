from utilitarios import paciente as paciente_utils
from database import paciente

import psycopg2
import csv

def inserir_dados(connection):
    with open('entrada.csv', 'r') as file:
        csv_reader = csv.DictReader(file, delimiter = ';')
        next(csv_reader)  # Pule o cabeçalho

        try:
            for row in csv_reader:
                dados_paciente = paciente_utils.obter_dados_paciente_csv(row)

                paciente.inserir(connection, dados_paciente)

        except (csv.Error, psycopg2.Error) as e:
            print(f"Erro encontrado -> {e}")

    connection.commit()
    print("Dados inseridos com sucesso!")
