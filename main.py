# Arquivo responsavel pela coordenacao geral do programa

import database

from database import paciente

#from tables import residencia
#from tables import notificacao
#from tables import dados_clinicos
#from tables import dados_atendimento
#from tables import dados_laboratorial
#from tables import conclusao
import inserir_dadosCSV

# Estou arrumando a main ainda, esta dando um erro ao tentar importar o arquivo das ""tables""

database_connection = database.create_connection()

paciente.create_table_paciente(database_connection)
#tables.residencia.create_table_residencia()
#tables.notificacao.create_table_notificacao()
#tables.dados_clinicos.create_table_dados_clinicos()
#tables.dados_atendimento.create_table_dados_atendimento()
#tables.dados_laboratorial.create_table_dados_laboratorial()
#tables.conclusao.create_table_conclusao()

inserir_dadosCSV.inserir_dados(database_connection)

database_connection.close()