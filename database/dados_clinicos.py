from utilitarios.tratadorDeDados import tratarData

class DadosClinicos:
    def __init__(self, database):
        self.database = database

    def criarTabela(self):
        cursor = self.database.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dados_clinicos (
                id_dados_clinicos SERIAL PRIMARY KEY,
                id_paciente INTEGER REFERENCES paciente(id_paciente),
                histo_vgm VARCHAR(3),
                pais_vgm VARCHAR(255),
                lo_ps_vgm VARCHAR(255),
                dt_vgm DATE NULL,
                dt_rt_vgm DATE NULL,
                surto_sg VARCHAR(3),
                nosocomial VARCHAR(3),
                ave_suino VARCHAR(3),
                out_anim VARCHAR(255),
                outro_sin VARCHAR(3),
                outro_des VARCHAR(255),
                fator_risc VARCHAR(3),
                puerpera VARCHAR(3),
                cardiopati VARCHAR(3),
                hematologi VARCHAR(3),
                sind_down VARCHAR(3),
                hepatica VARCHAR(3),
                asma VARCHAR(3),
                diabetes VARCHAR(3),
                neurologic VARCHAR(3),
                pneumopati VARCHAR(3),
                imunodepre VARCHAR(3),
                renal VARCHAR(3),
                obesidade VARCHAR(3),
                obes_imc VARCHAR(35),
                out_morbi VARCHAR(3),
                morb_desc VARCHAR(255),
                vacina VARCHAR(3),
                dt_ut_dose DATE NULL,
                mae_vac VARCHAR(3),
                dt_vac_mae DATE NULL,
                m_amamenta VARCHAR(3),
                dt_doseuni DATE NULL,
                DT_1_DOSE DATE NULL,
                dt_2_dose DATE NULL
            )
        ''')

        
        cursor.close()

    def criar(self, idPaciente, dados):
        cursor = self.database.cursor()

        dados = {
            **dados,
            'ID_PACIENTE': idPaciente,
            'DT_DOSEUNI': tratarData(dados['DT_DOSEUNI']),
            'DT_1_DOSE': tratarData(dados['DT_1_DOSE']),
            'DT_2_DOSE': tratarData(dados['DT_2_DOSE']),
            'DT_UT_DOSE': tratarData(dados['DT_UT_DOSE']),
            'DT_VAC_MAE': tratarData(dados['DT_VAC_MAE']),
            'DT_VGM': tratarData(dados['DT_VGM']),
            'DT_RT_VGM': tratarData(dados['DT_RT_VGM']),
        }

        cursor.execute('''
            INSERT INTO dados_clinicos (
                id_paciente,
                histo_vgm,
                pais_vgm,
                lo_ps_vgm,
                dt_vgm,
                dt_rt_vgm,
                surto_sg,
                nosocomial,
                ave_suino,
                out_anim,
                outro_sin,
                outro_des,
                fator_risc,
                puerpera,
                cardiopati,
                hematologi,
                sind_down,
                hepatica,
                asma,
                diabetes,
                neurologic,
                pneumopati,
                imunodepre,
                renal,
                obesidade,
                obes_imc,
                out_morbi,
                morb_desc,
                vacina,
                dt_ut_dose,
                mae_vac,
                dt_vac_mae,
                m_amamenta,
                dt_doseuni,
                dt_1_dose
            ) VALUES (
                %(ID_PACIENTE)s,
                %(HISTO_VGM)s,
                %(PAIS_VGM)s,
                %(LO_PS_VGM)s,
                %(DT_VGM)s,
                %(DT_RT_VGM)s,
                %(SURTO_SG)s,
                %(NOSOCOMIAL)s,
                %(AVE_SUINO)s,
                %(OUT_ANIM)s,
                %(OUTRO_SIN)s,
                %(OUTRO_DES)s,
                %(FATOR_RISC)s,
                %(PUERPERA)s,
                %(CARDIOPATI)s,
                %(HEMATOLOGI)s,
                %(SIND_DOWN)s,
                %(HEPATICA)s,
                %(ASMA)s,
                %(DIABETES)s,
                %(NEUROLOGIC)s,
                %(PNEUMOPATI)s,
                %(IMUNODEPRE)s,
                %(RENAL)s,
                %(OBESIDADE)s,
                %(OBES_IMC)s,
                %(OUT_MORBI)s,
                %(MORB_DESC)s,
                %(VACINA)s,
                %(DT_UT_DOSE)s,
                %(MAE_VAC)s,
                %(DT_VAC_MAE)s,
                %(M_AMAMENTA)s,
                %(DT_DOSEUNI)s,
                %(DT_1_DOSE)s
            ) RETURNING id_dados_clinicos;
        ''', dados)

        row = cursor.fetchone()

        
        cursor.close()

        return row[0]
