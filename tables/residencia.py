from db import execute_query, commit_changes
from db import execute_query, commit_changes

def create_table_residencia():
    query = """
    CREATE TABLE residencia (
        id_residencia SERIAL PRIMARY KEY,
        id_paciente INTEGER REFERENCES paciente(id_paciente),
        nu_cep VARCHAR(8),
        sg_uf VARCHAR(2),
        id_rg_resi VARCHAR(6),
        id_mn_resi VARCHAR(6),
        nm_bairro VARCHAR(72),
        nm_logrado VARCHAR(50),
        nm_numero VARCHAR(8),
        nm_complem VARCHAR(15),
        nu_ddd_tel VARCHAR(4),
        cs_zona VARCHAR(1),
        id_pais VARCHAR(3)
    )
    """
    return query

   
execute_query(create_table_residencia())
commit_changes()