class Residencia {
  /** 
   * @param {Knex} database 
   */
  constructor(database) {
    this.database = database;
  }

  async criarTabela() {
    await this.database.raw(`
      CREATE TABLE IF NOT EXISTS residencia (
        id_residencia SERIAL PRIMARY KEY,
        sg_uf VARCHAR(2),
        id_rg_resi VARCHAR(64),
        id_mn_resi VARCHAR(64),
        cs_zona VARCHAR(1),
        id_pais VARCHAR(20)
      )
    `);
  }

  async criar() {

  }
}

module.exports = { Residencia };