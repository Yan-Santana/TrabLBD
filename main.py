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

paciente.create_table(database_connection)
#residencia.create_table()
#notificacao.create_table()
#dados_clinicos.create_table()
#dados_atendimento.create_table()
#dados_laboratorial.create_table()
#conclusao.create_table()

inserir_dadosCSV.inserir_dados(database_connection)

database_connection.close()