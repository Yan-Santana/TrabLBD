# Arquivo responsavel pela coordenacao geral do programa

from db import create_db, connect_db, execute_query
import tables
import inserir_dadosCSV
import tables

create_db()

conn = connect_db() 

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