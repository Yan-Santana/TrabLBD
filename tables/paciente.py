from db import execute_query, commit_changes
from db import execute_query, commit_changes

def create_table_paciente():
    query = """
        CREATE TABLE IF NOT EXISTS paciente (
        id_paciente SERIAL PRIMARY KEY,
        cs_sexo VARCHAR(1),
        dt_nasc DATE NULL,
        nu_idade_n VARCHAR(3),
        tp_idade VARCHAR(1),
        cs_raca VARCHAR(2),
        cs_gestant VARCHAR(1),
        cs_escol_n VARCHAR(1),
        pac_cocbo VARCHAR(6)
    )
    """
    return query
execute_query(create_table_paciente())
commit_changes()