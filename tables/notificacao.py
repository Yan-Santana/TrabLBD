from db import execute_query, commit_changes
from db import execute_query, commit_changes

def create_table_notificacao():
    query = """
    CREATE TABLE notificacao (
        id_notificacao SERIAL PRIMARY KEY,
        id_paciente INTEGER REFERENCES paciente(id_paciente),
        nu_notific VARCHAR(12),
        dt_notific DATE,
        sg_uf_not VARCHAR(2),
        sem_not VARCHAR(6),
        id_municip VARCHAR(6),
        id_regiona VARCHAR(6)
    )
    """
    
execute_query(create_table_notificacao())
commit_changes()