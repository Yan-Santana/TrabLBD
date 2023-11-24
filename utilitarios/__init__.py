from utilitarios import paciente as paciente_utils
from utilitarios import residencia as residencia_utils
from utilitarios import notificacao as notificacao_utils
from database import notificacao, paciente, residencia

import psycopg2
import csv

def inserir_dados(connection):
    with open('entrada.csv', 'r') as file:
        csv_reader = csv.DictReader(file, delimiter = ';')
        next(csv_reader) 

        try:
            for i, row in enumerate(csv_reader):
                dados_paciente = paciente_utils.obter_dados_paciente_csv(row)
                dados_residencia = residencia_utils.obter_dados_residencia_csv(row)
                dados_notificacao = notificacao_utils.obter_dados_notificacao_csv(row)

                paciente.inserir(connection, dados_paciente)
                
                residencia.inserir(connection, dados_residencia)
                notificacao.inserir(connection, dados_notificacao)
                
        except (csv.Error, psycopg2.Error) as e:
            print(f"Erro encontrado -> {e}")

    connection.commit()
    print("Dados inseridos com sucesso!")
