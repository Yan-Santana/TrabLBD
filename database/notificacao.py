from database import execute_query

def inserir(connection, dados):
    sql_notificacao = """
        INSERT INTO notificacao (
            dt_notific, sg_uf_not,
            sem_not, id_municip, id_regiona
        ) VALUES (
            %(dt_notific)s, %(sg_uf_not)s,
            %(sem_not)s, %(id_municip)s, %(id_regiona)s
        );
    """

    return execute_query(connection, sql_notificacao, dados)


def create_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS notificacao (
        id_notificacao SERIAL PRIMARY KEY,
        dt_notific DATE,
        sg_uf_not VARCHAR(2),
        sem_not VARCHAR(64),
        id_municip VARCHAR(64),
        id_regiona VARCHAR(64)
    )
    """

    execute_query(connection, query)