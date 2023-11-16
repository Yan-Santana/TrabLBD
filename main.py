# Arquivo responsavel pela coordenacao geral do programa

from db import connect, execute_query
from tables import paciente
import inserir_dadosCSV
import tables

# Estou arrumando a main ainda, esta dando um erro ao tentar importar o arquivo das ""tables""

conn = connect() 

tables.paciente.create_table_paciente()
tables.residencia.create_table_residencia()
tables.notificacao.create_table_notificacao()
tables.dados_clinicos.create_table_dados_clinicos()
tables.dados_atendimento.create_table_dados_atendimento()
tables.dados_laboratoriais.create_table_dados_laboratoriais()
tables.conclusao.create_table_conclusao()

inserir_dadosCSV.inserir_dados()

conn.commit()
conn.close()