from db import execute_query, commit_changes
from db import execute_query, commit_changes

def create_table_conclusao():
   query = """
    CREATE TABLE conclusao (
        classi_fin VARCHAR(1),
        classi_out VARCHAR(30),
        criterio VARCHAR(1),
        evolucao VARCHAR(1),
        dt_evoluca DATE,
        dt_encerra DATE,
        nu_do VARCHAR(10),
        observa VARCHAR(999),
        nome_prof VARCHAR(60),
        reg_prof VARCHAR(15)
    )
"""
   
execute_query(create_table_conclusao())
commit_changes()