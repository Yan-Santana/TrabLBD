import psycopg2

class Hospital:
    def __init__(self, database):
        self.database = database

    def criarTabela(self):
        cursor = self.database.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS hospital (
                id_hospital SERIAL PRIMARY KEY,
                id_unidade VARCHAR(64),
                id_rg_resi VARCHAR(64),
                id_mn_resi VARCHAR(64),
                sg_uf VARCHAR(2),
                cs_zona VARCHAR(1),
                id_pais VARCHAR(64)
            )
        ''')

        
        cursor.close()

    def pegarIdOuCriar(self, dados):
        cursor = self.database.cursor()

        cursor.execute('SELECT id_hospital FROM hospital WHERE id_unidade = %s LIMIT 1', (dados['ID_UNIDADE'],))
        hospital = cursor.fetchone()

        # Se o hospital já existe, retorna o ID
        if hospital:
            return hospital[0]

        # Se não existe, cria um novo hospital
        cursor.execute('''
            INSERT INTO hospital (
                id_unidade, sg_uf, id_rg_resi, id_mn_resi,
                cs_zona, id_pais
            ) VALUES ( 
                %s, %s, %s, %s,
                %s, %s
            ) RETURNING id_hospital;
        ''', (
            dados['ID_UNIDADE'], dados['SG_UF'], dados['ID_RG_RESI'], dados['ID_MN_RESI'],
            dados['CS_ZONA'], dados['ID_PAIS']
        ))

        id_hospital = (cursor.fetchone())[0]

        
        cursor.close()

        return id_hospital
