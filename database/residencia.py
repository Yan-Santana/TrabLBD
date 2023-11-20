from database import execute_query

def inserir_residencia(connection, dados):
    sql_residencia = """
        INSERT INTO residencia (
            id_paciente, sg_uf, id_rg_resi, id_mn_resi,
           cs_zona, id_pais
        ) VALUES (
            %(id_paciente)s, %(sg_uf)s, %(id_rg_resi)s, 
            %(id_mn_resi)s, %(cs_zona)s, %(id_pais)s
        );
    """

    return execute_query(connection, sql_residencia, dados)

def create_table(connection):
    query = """
        CREATE TABLE IF NOT EXISTS residencia (
            id_residencia SERIAL PRIMARY KEY,
            id_paciente INTEGER REFERENCES paciente(id_paciente),
            sg_uf VARCHAR(2),
            id_rg_resi VARCHAR(6),
            id_mn_resi VARCHAR(6),
            cs_zona VARCHAR(1),
            id_pais VARCHAR(3)
        )
    """
    
    execute_query(connection, query)

