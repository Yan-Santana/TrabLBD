# Arquivo responsavel pela coordenacao geral do programa

import utilitarios
import database

from database import paciente
from database import residencia
from database import notificacao
from database import dados_clinicos
from database import dados_atendimento
from database import dados_laboratorial
from database import conclusao

database_connection = database.create_connection()

paciente.create_table(database_connection)
residencia.create_table(database_connection)
notificacao.create_table(database_connection)
dados_clinicos.create_table(database_connection)
dados_atendimento.create_table(database_connection)
dados_laboratorial.create_table(database_connection)
conclusao.create_table(database_connection)

utilitarios.inserir_dados(database_connection)

database_connection.commit()
database_connection.close()