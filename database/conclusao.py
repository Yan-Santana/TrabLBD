from utilitarios.tratadorDeDados import tratarData
class Conclusao:
    def __init__(self, database):
        self.database = database

    def criarTabela(self):
        cursor = self.database.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conclusao (
                id_conclusao SERIAL PRIMARY KEY,
                id_cod_atendimento INTEGER REFERENCES dados_atendimento(id_cod_atendimento),
                classi_fin VARCHAR(1),
                classi_out VARCHAR(30),
                criterio VARCHAR(1),
                evolucao VARCHAR(1),
                dt_evoluca DATE,
                dt_encerra DATE
            )
        ''')
        
        cursor.close()

    def criar(self, codAtendimento, dados):
        cursor = self.database.cursor()
    
        dtEvoluca = tratarData(dados['DT_EVOLUCA'])
        dtEncerra = tratarData(dados['DT_ENCERRA'])
        dados = {
            **dados,
            'DT_EVOLUCA': dtEvoluca,
            'DT_ENCERRA': dtEncerra,
            'ID_COD_ATENDIMENTO': codAtendimento,
        }

        cursor.execute('''
            INSERT INTO conclusao (
                id_cod_atendimento, classi_fin, classi_out,
                criterio, evolucao, dt_evoluca,
                dt_encerra
            ) VALUES (
                %(ID_COD_ATENDIMENTO)s, %(CLASSI_FIN)s, %(CLASSI_OUT)s,
                %(CRITERIO)s, %(EVOLUCAO)s, %(DT_EVOLUCA)s,
                %(DT_ENCERRA)s
            ) RETURNING *;
        ''', dados)

        
        cursor.close()