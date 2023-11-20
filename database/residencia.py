from database import execute_query

def inserir(connection, dados):
    sql_residencia = """
        INSERT INTO residencia (
            sg_uf, id_rg_resi, id_mn_resi,
           cs_zona, id_pais
        ) VALUES ( 
            %(sg_uf)s, %(id_rg_resi)s, 
            %(id_mn_resi)s, %(cs_zona)s, %(id_pais)s
        );
    """
# %(id_paciente)s,
    return execute_query(connection, sql_residencia, dados)
# id_paciente INTEGER,
def create_table(connection):
    query = """
        CREATE TABLE IF NOT EXISTS residencia (
            id_residencia SERIAL PRIMARY KEY,
            sg_uf VARCHAR(2),
            id_rg_resi VARCHAR(32),
            id_mn_resi VARCHAR(32),
            cs_zona VARCHAR(1),
            id_pais VARCHAR(20)
        )
    """
    
    execute_query(connection, query)

