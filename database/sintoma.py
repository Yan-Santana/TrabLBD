class Sintoma:
    def __init__(self, database):
        self.database = database

    def criarTabela(self):
        cursor = self.database.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sintoma (
                id_sintoma SERIAL PRIMARY KEY,
                id_dados_clinicos INTEGER REFERENCES dados_clinicos(id_dados_clinicos),
                nome VARCHAR(32),
                ignorado BOOLEAN DEFAULT(false)
            )
        ''')

        
        cursor.close()

    def criar(self, idDadosClinicos, dados):
        cursor = self.database.cursor()

        def validarSeSintomaFoiCitado(valor):
            return {
                "inserir": valor == '1' or valor == '9',
                "ignorado": 'true' if valor == '9' else 'false'
            }

        dados = {
            'FEBRE': validarSeSintomaFoiCitado(dados['FEBRE']),
            'TOSSE': validarSeSintomaFoiCitado(dados['TOSSE']),
            'GARGANTA': validarSeSintomaFoiCitado(dados['GARGANTA']),
            'DISPNEIA': validarSeSintomaFoiCitado(dados['DISPNEIA']),
            'DESC_RESP': validarSeSintomaFoiCitado(dados['DESC_RESP']),
            'SATURACAO': validarSeSintomaFoiCitado(dados['SATURACAO']),
            'DIARREIA': validarSeSintomaFoiCitado(dados['DIARREIA']),
            'VOMITO': validarSeSintomaFoiCitado(dados['VOMITO']),
            'DOR_ABD': validarSeSintomaFoiCitado(dados['DOR_ABD']),
            'FADIGA': validarSeSintomaFoiCitado(dados['FADIGA']),
            'PERD_OLFT': validarSeSintomaFoiCitado(dados['PERD_OLFT']),
            'PERD_PALA': validarSeSintomaFoiCitado(dados['PERD_PALA']),
        }

        sql = 'INSERT INTO sintoma (nome, id_dados_clinicos, ignorado) VALUES '

        sintomasItems = [];
        for sintoma in dados.items():
            if (sintoma[1]['inserir']):
                # Insere a tupla
                sintomasItems.append(f"('{sintoma[0]}', {idDadosClinicos}, {sintoma[1]['ignorado']})")

        if len(sintomasItems) == 0: return

        sintomasValores = ','.join(sintomasItems)
        sintomasValores += ';'

        cursor.execute(sql + sintomasValores) 
        cursor.close()
