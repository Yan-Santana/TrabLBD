from database import execute_query

def inserir(connection, dados):
    sql_paciente = """
        INSERT INTO paciente (
            cs_sexo, dt_nasc, nu_idade_n,
            tp_idade, cs_raca, cs_gestant, cs_escol_n,
            pac_cocbo
        ) VALUES (
            %(cs_sexo)s, %(dt_nasc)s, %(nu_idade_n)s,
            %(tp_idade)s, %(cs_raca)s, %(cs_gestant)s, %(cs_escol_n)s,
            %(pac_cocbo)s
        );
    """

    return execute_query(connection, sql_paciente, dados)

def create_table(connection):
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

    execute_query(connection, query)