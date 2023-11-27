from utilitarios.tratadorDeDados import tratarData

class Notificacao:
    def __init__(self, database):
        self.database = database

    def criarTabela(self):
        cursor = self.database.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notificacao (
                id_notificacao SERIAL PRIMARY KEY,
                id_dados_clinicos INTEGER REFERENCES dados_clinicos(id_dados_clinicos),
                dt_notific DATE,
                sg_uf_not VARCHAR(2),
                sem_not VARCHAR(64),
                id_municip VARCHAR(64),
                id_regiona VARCHAR(64)
            )
        ''')

        
        cursor.close()

    def criar(self, idDadosClinicos, dados):
        cursor = self.database.cursor()

        dataNotific = tratarData(dados['DT_NOTIFIC'])
        dados = {
            **dados,
            'DT_NOTIFIC': dataNotific,
            'ID_DADOS_CLINICOS': idDadosClinicos,
        }

        cursor.execute('''
            INSERT INTO notificacao (
                id_dados_clinicos, dt_notific, sg_uf_not,
                sem_not, id_municip, id_regiona
            ) VALUES (
                %(ID_DADOS_CLINICOS)s, %(DT_NOTIFIC)s, 
                %(SG_UF_NOT)s, %(SEM_NOT)s, %(ID_MUNICIP)s, %(ID_REGIONA)s
            ) RETURNING *;
        ''', dados)

        
        cursor.close()
