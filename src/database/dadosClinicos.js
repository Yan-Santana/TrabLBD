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
        histo_vgm VARCHAR(1),
        pais_vgm VARCHAR(3),
        lo_ps_vgm VARCHAR(30),
        dt_vgm DATE,
        dt_rt_vgm DATE,
        surto_sg VARCHAR(1),
        nosocomial VARCHAR(1),
        ave_suino VARCHAR(1),
        out_anim VARCHAR(60),
        febre VARCHAR(1),
        tosse VARCHAR(1),
        garganta VARCHAR(1),
        dispneia VARCHAR(1),
        desc_resp VARCHAR(1),
        saturacao VARCHAR(1),
        diarreia VARCHAR(1),
        vomito VARCHAR(1),
        dor_abd VARCHAR(1),
        fadiga VARCHAR(1),
        perd_olft VARCHAR(1),
        perd_pala VARCHAR(1),
        outro_sin VARCHAR(1),
        outro_des VARCHAR(30),
        fator_risc VARCHAR(1),
        puerpera VARCHAR(1),
        cardiopati VARCHAR(1),
        hematologi VARCHAR(1),
        sind_down VARCHAR(1),
        hepatica VARCHAR(1),
        asma VARCHAR(1),
        diabetes VARCHAR(1),
        neurologic VARCHAR(1),
        pneumopati VARCHAR(1),
        imunodepre VARCHAR(1),
        renal VARCHAR(1),
        obesidade VARCHAR(1),
        obes_imc VARCHAR(3),
        out_morbi VARCHAR(1),
        morb_desc VARCHAR(30),
        vacina VARCHAR(1),
        dt_ut_dose DATE,
        mae_vac VARCHAR(1),
        dt_vac_mae DATE,
        m_amamenta VARCHAR(1),
        dt_doseuni DATE,
        dt_1_dose DATE,
        dt_2_dose DATE,
        dat_sin_pri DATE
      )
    `);
  }

  async criar() {

  }
}

module.exports = { DadosClinicos };