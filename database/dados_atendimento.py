from utilitarios.tratadorDeDados import tratarData

class DadosAtendimento:
    def __init__(self, database):
        self.database = database

    def criarTabela(self):
        cursor = self.database.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dados_atendimento (
                id_cod_atendimento SERIAL PRIMARY KEY,
                id_dados_clinicos INTEGER REFERENCES dados_clinicos(id_dados_clinicos),
                id_hospital INTEGER REFERENCES hospital(id_hospital),
                antiviral VARCHAR(1),
                tp_antivir VARCHAR(1),
                dt_antivir DATE,
                hospital VARCHAR(1),
                dt_interna DATE,
                sg_uf_inte VARCHAR(2),
                id_rg_inte VARCHAR(64),
                id_mn_inte VARCHAR(64),
                uti VARCHAR(1),
                dt_entuti DATE,
                dt_saiduti DATE,
                suport_ven VARCHAR(1),
                raiox_res VARCHAR(1),
                dt_raiox DATE,
                tomo_res VARCHAR(6) NULL,
                tomo_out VARCHAR(99),
                dt_tomo DATE,
                amostra VARCHAR(1),
                dt_coleta DATE,
                tp_amostra VARCHAR(30)
            )
        ''')

        
        cursor.close()

    def criar(self, idDadosClinicos, idHospital, dados):
        cursor = self.database.cursor()

        dtAntivir = tratarData(dados['DT_ANTIVIR'])
        dtInterna = tratarData(dados['DT_INTERNA'])
        dtEntuti = tratarData(dados['DT_ENTUTI'])
        dtSaiduti = tratarData(dados['DT_SAIDUTI'])
        dtRaiox = tratarData(dados['DT_RAIOX'])
        dtTomo = tratarData(dados['DT_TOMO'])
        dtColeta = tratarData(dados['DT_COLETA'])

        dados = {
            **dados,
            'DT_ANTIVIR': dtAntivir,
            'DT_INTERNA': dtInterna,
            'DT_ENTUTI': dtEntuti,
            'DT_SAIDUTI': dtSaiduti,
            'DT_RAIOX': dtRaiox,
            'DT_TOMO': dtTomo,
            'DT_COLETA': dtColeta,
            'ID_DADOS_CLINICOS': idDadosClinicos,
            'ID_HOSPITAL': idHospital,
        }

        cursor.execute('''
            INSERT INTO dados_atendimento (
                id_dados_clinicos, antiviral, tp_antivir,
                id_hospital, dt_antivir, hospital, 
                dt_interna, sg_uf_inte, id_rg_inte, 
                id_mn_inte, uti, 
                dt_entuti, dt_saiduti, suport_ven, 
                raiox_res, dt_raiox, tomo_res, 
                tomo_out, dt_tomo, amostra, 
                dt_coleta, tp_amostra
            ) VALUES (
                %(ID_DADOS_CLINICOS)s, %(ANTIVIRAL)s, %(TP_ANTIVIR)s, 
                %(ID_HOSPITAL)s, %(DT_ANTIVIR)s, %(HOSPITAL)s, 
                %(DT_INTERNA)s, %(SG_UF_INTE)s, %(ID_RG_INTE)s, 
                %(ID_MN_INTE)s, %(UTI)s, 
                %(DT_ENTUTI)s, %(DT_SAIDUTI)s, %(SUPORT_VEN)s, 
                %(RAIOX_RES)s, %(DT_RAIOX)s, %(TOMO_RES)s, 
                %(TOMO_OUT)s, %(DT_TOMO)s, %(AMOSTRA)s, 
                %(DT_COLETA)s, %(TP_AMOSTRA)s
            ) RETURNING id_cod_atendimento;
        ''', dados)

        result = cursor.fetchone()
        
        cursor.close()

        return result[0]
