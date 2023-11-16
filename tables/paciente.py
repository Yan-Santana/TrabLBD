from db import execute_query, commit_changes
from db import execute_query, commit_changes

def create_table_paciente():
    query = """
        CREATE TABLE paciente (
        id_paciente SERIAL PRIMARY KEY,
        nm_paciente VARCHAR(70),
        nu_cpf VARCHAR(15),
        cs_sexo VARCHAR(1),
        dt_nasc DATE,
        nu_idade_n VARCHAR(3),
        tp_idade VARCHAR(1),
        cs_raca VARCHAR(2),
        cs_etnia VARCHAR(4),
        cs_gestant VARCHAR(1),
        cs_escol_n VARCHAR(1),
        pac_cocbo VARCHAR(6),
        nm_mae_pac VARCHAR(70)
    )
"""
execute_query(create_table_paciente())
commit_changes()