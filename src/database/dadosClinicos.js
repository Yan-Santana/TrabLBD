const { tratarData } = require('../utils/tratadorDeDados');

class DadosClinicos {
  /** 
   * @param {Knex} database 
   */
  constructor(database) {
    this.database = database;
  }

  async criarTabela() {
    await this.database.raw(`
      CREATE TABLE IF NOT EXISTS dados_clinicos (
        id_dados_clinicos SERIAL PRIMARY KEY,
        id_paciente INTEGER REFERENCES paciente(id_paciente),
        histo_vgm VARCHAR(3),
        pais_vgm VARCHAR(60),
        lo_ps_vgm VARCHAR(60),
        dt_vgm DATE NULL,
        dt_rt_vgm DATE NULL,
        surto_sg VARCHAR(3),
        nosocomial VARCHAR(3),
        ave_suino VARCHAR(3),
        out_anim VARCHAR(60),
        outro_sin VARCHAR(3),
        outro_des VARCHAR(60),
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
        morb_desc VARCHAR(60),
        vacina VARCHAR(3),
        dt_ut_dose DATE NULL,
        mae_vac VARCHAR(3),
        dt_vac_mae DATE NULL,
        m_amamenta VARCHAR(3),
        dt_doseuni DATE NULL,
        DT_1_DOSE DATE NULL,
        dt_2_dose DATE NULL
      )
    `);
  }

  async criar(idPaciente, dados) {
    dados = {
      ...dados,
      ID_PACIENTE: idPaciente,
      DT_DOSEUNI: tratarData(dados.DT_DOSEUNI),
      DT_1_DOSE: tratarData(dados.DT_1_DOSE),
      DT_2_DOSE: tratarData(dados.DT_2_DOSE),
      DT_UT_DOSE: tratarData(dados.DT_UT_DOSE),
      DT_VAC_MAE: tratarData(dados.DT_VAC_MAE),
      DT_VGM: tratarData(dados.DT_VGM),
      DT_RT_VGM: tratarData(dados.DT_RT_VGM),
    };

    const { rows } = await this.database.raw(`
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
        :ID_PACIENTE,
        :HISTO_VGM,
        :PAIS_VGM,
        :LO_PS_VGM,
        :DT_VGM,
        :DT_RT_VGM,
        :SURTO_SG,
        :NOSOCOMIAL,
        :AVE_SUINO,
        :OUT_ANIM,
        :OUTRO_SIN,
        :OUTRO_DES,
        :FATOR_RISC,
        :PUERPERA,
        :CARDIOPATI,
        :HEMATOLOGI,
        :SIND_DOWN,
        :HEPATICA,
        :ASMA,
        :DIABETES,
        :NEUROLOGIC,
        :PNEUMOPATI,
        :IMUNODEPRE,
        :RENAL,
        :OBESIDADE,
        :OBES_IMC,
        :OUT_MORBI,
        :MORB_DESC,
        :VACINA,
        :DT_UT_DOSE,
        :MAE_VAC,
        :DT_VAC_MAE,
        :M_AMAMENTA,
        :DT_DOSEUNI,
        :DT_1_DOSE
      ) RETURNING id_dados_clinicos;
    `, dados);

    return rows[0].id_dados_clinicos;
  }
}

module.exports = { DadosClinicos };