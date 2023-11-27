from utilitarios.tratadorDeDados import tratarData

class DadosLaboratoriais:
    def __init__(self, database):
        self.database = database

    def criarTabela(self):
        cursor = self.database.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dados_laboratoriais (
                requi_gal SERIAL PRIMARY KEY,
                id_dados_clinicos INTEGER REFERENCES dados_clinicos(id_dados_clinicos),
                tp_tes_an INTEGER,
                dt_res_an DATE,
                res_an VARCHAR(1),
                pos_an_flu VARCHAR(1),
                tp_flu_an VARCHAR(1),
                pos_an_out VARCHAR(1),
                an_sars2 VARCHAR(1),
                an_vsr VARCHAR(1),
                an_para1 VARCHAR(1),
                an_para2 VARCHAR(1),
                an_para3 VARCHAR(1),
                an_adeno VARCHAR(1),
                an_outro VARCHAR(1),
                ds_an_out VARCHAR(30),
                pcr_resul VARCHAR(1),
                dt_pcr DATE,
                pos_pcrflu VARCHAR(1),
                tp_flu_pcr VARCHAR(1),
                pcr_fluasu VARCHAR(1),
                fluasu_out VARCHAR(30),
                pcr_flubli VARCHAR(1),
                flubli_out VARCHAR(30),
                pos_pcrout VARCHAR(1),
                pcr_sars2 VARCHAR(1),
                pcr_vsr VARCHAR(1),
                pcr_para1 VARCHAR(1),
                pcr_para2 VARCHAR(1),
                pcr_para3 VARCHAR(1),
                pcr_para4 VARCHAR(1),
                pcr_adeno VARCHAR(1),
                pcr_metap VARCHAR(1),
                pcr_boca VARCHAR(1),
                pcr_rino VARCHAR(1),
                pcr_outro VARCHAR(1),
                ds_pcr_out VARCHAR(30),
                tp_am_sor VARCHAR(12),
                sor_out VARCHAR(100),
                tp_sor INTEGER NULL,
                out_sor VARCHAR(100),
                res_igg VARCHAR(1),
                res_igm VARCHAR(1),
                res_iga VARCHAR(1),
                dt_res DATE
            )
        ''')

        
        cursor.close()

    def criar(self, idDadosClinicos, dados):
        cursor = self.database.cursor()

        dtPcr = tratarData(dados['DT_PCR'])
        dtRes = tratarData(dados['DT_RES'])
        dtResAn = tratarData(dados['DT_RES_AN'])

        dados = {
            **dados,
            'DT_PCR': dtPcr,
            'DT_RES': dtRes,
            'DT_RES_AN': dtResAn,
            'ID_DADOS_CLINICOS': idDadosClinicos,
        }

        cursor.execute('''
            INSERT INTO dados_laboratoriais (
                tp_tes_an, dt_res_an, res_an,
                pos_an_flu, tp_flu_an, pos_an_out,
                an_sars2, an_vsr, an_para1,
                an_para2, an_para3, an_adeno, an_outro,
                ds_an_out, pcr_resul, dt_pcr, pos_pcrflu,
                tp_flu_pcr, pcr_fluasu, fluasu_out, pcr_flubli,
                flubli_out, pos_pcrout, pcr_sars2, pcr_vsr,
                pcr_para1, pcr_para2, pcr_para3, pcr_para4,
                pcr_adeno, pcr_metap, pcr_boca, pcr_rino,
                pcr_outro, ds_pcr_out, tp_am_sor,
                sor_out, tp_sor, out_sor,
                res_igg, res_igm, res_iga,
                dt_res, id_dados_clinicos
            ) VALUES (
                %(TP_TES_AN)s, %(DT_RES_AN)s, %(RES_AN)s, 
                %(POS_AN_FLU)s, %(TP_FLU_AN)s, %(POS_AN_OUT)s,
                %(AN_SARS2)s, %(AN_VSR)s, %(AN_PARA1)s,
                %(AN_PARA2)s, %(AN_PARA3)s, %(AN_ADENO)s, %(AN_OUTRO)s,
                %(DS_AN_OUT)s, %(PCR_RESUL)s, %(DT_PCR)s, %(POS_PCRFLU)s,
                %(TP_FLU_PCR)s, %(PCR_FLUASU)s, %(FLUASU_OUT)s, %(PCR_FLUBLI)s,
                %(FLUBLI_OUT)s, %(POS_PCROUT)s, %(PCR_SARS2)s, %(PCR_VSR)s,
                %(PCR_PARA1)s, %(PCR_PARA2)s, %(PCR_PARA3)s, %(PCR_PARA4)s,
                %(PCR_ADENO)s, %(PCR_METAP)s, %(PCR_BOCA)s, %(PCR_RINO)s,
                %(PCR_OUTRO)s, %(DS_PCR_OUT)s, %(TP_AM_SOR)s,
                %(SOR_OUT)s, %(TP_SOR)s, %(OUT_SOR)s,
                %(RES_IGG)s, %(RES_IGM)s, %(RES_IGA)s,
                %(DT_RES)s, %(ID_DADOS_CLINICOS)s
            ) RETURNING *;
        ''', dados)

        row = cursor.fetchone()

        
        cursor.close()

        return row