from db import connect
from utilitarios import paciente
import csv
import psycopg2

def inserir_dados():
    with connect() as conn, conn.cursor() as cur:
        with open('entrada.csv', 'r') as f:
            csv_reader = csv.DictReader(f, delimiter = ';')
            next(csv_reader)  # Pule o cabeçalho

            try:
                for row in csv_reader:
                    dados_paciente = paciente.obter_dados_paciente_csv(row)
                    sql_paciente = """
                        INSERT INTO paciente (
                            cs_sexo, dt_nasc, nu_idade_n,
                            tp_idade, cs_raca, cs_gestant, cs_escol_n,
                            pac_cocbo
                        ) VALUES (
                            %(cs_sexo)s, %(dt_nasc)s, %(nu_idade_n)s,
                            %(tp_idade)s, %(cs_raca)s, %(cs_gestant)s, %(cs_escol_n)s,
                            %(pac_cocbo)s
                        );
                    """
                    
                    cur.execute(sql_paciente, dados_paciente)
                    
            except (csv.Error, psycopg2.Error) as e:
                print(f"Erro encontrado -> {e}")

        conn.commit()
        print("Print de dados inseridos com sucesso!")

inserir_dados()
