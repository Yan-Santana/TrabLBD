const { tratarData } = require('../utils/tratadorDeDados');

class Notificacao {
  /** 
   * @param {Knex} database 
   */
  constructor(database) {
    this.database = database;
  }

  async criarTabela() {
    await this.database.raw(`
      CREATE TABLE IF NOT EXISTS notificacao (
        id_notificacao SERIAL PRIMARY KEY,
        dt_notific DATE,
        sg_uf_not VARCHAR(2),
        sem_not VARCHAR(64),
        id_municip VARCHAR(64),
        id_regiona VARCHAR(64)
      )
    `);
  }

  async criar(dados) {
    const dataNotific = tratarData(dados.DT_NOTIFIC);
    dados = {
      ...dados,
      DT_NOTIFIC: dataNotific,
    }
    const { rows } = await this.database.raw(`
      INSERT INTO notificacao (
        dt_notific, sg_uf_not,
        sem_not, id_municip, id_regiona
      ) VALUES (
        :DT_NOTIFIC, :SG_UF_NOT, :SEM_NOT, :ID_MUNICIP, :ID_REGIONA
      ) RETURNING *;
    `, dados);

    return rows[0];
  }
}

module.exports = { Notificacao };