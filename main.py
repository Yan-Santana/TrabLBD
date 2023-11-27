# Arquivo responsavel pela coordenacao geral do programa

import utilitarios
import database

database_connection = database.create_connection()

utilitarios.inserir_dados(database_connection)

database_connection.commit()
database_connection.close()