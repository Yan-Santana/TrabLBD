class DadosAtendimento {
  /** 
   * @param {Knex} database 
   */
  constructor(database) {
    this.database = database;
  }

  async criarTabela() {
    await this.database.raw(`
      CREATE TABLE IF NOT EXISTS dados_atendimento (
        cod_atendimento SERIAL PRIMARY KEY,
        id_dados_clinicos INTEGER,
        antiviral VARCHAR(1),
        tp_antivir VARCHAR(1),
        out_antivir VARCHAR(30),
        dt_antivir DATE,
        hospital VARCHAR(1),
        dt_interna DATE,
        sg_uf_inte VARCHAR(2),
        id_rg_inte VARCHAR(6),
        id_mn_inte VARCHAR(20),
        id_un_inte VARCHAR(20),
        uti VARCHAR(1),
        dt_entuti DATE,
        dt_saiduti DATE,
        suport_ven VARCHAR(1),
        raiox_res VARCHAR(1),
        dt_raiox DATE,
        tomo_res INTEGER,
        tomo_out VARCHAR(100),
        dt_tomo DATE,
        amostra VARCHAR(1),
        dt_coleta DATE,
        tp_amostra VARCHAR(30),
        out_amostra VARCHAR(1)
      )
    `);
  }

  async criar() {

  }
}

module.exports = { DadosAtendimento };