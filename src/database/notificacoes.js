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
        id_dados_clinicos INTEGER,
        dt_notific DATE,
        sg_uf_not VARCHAR(2),
        sem_not VARCHAR(64),
        id_municip VARCHAR(64),
        id_regiona VARCHAR(64)
      )
    `);
  }

  async criar(idDadosClinicos, dados) {
    const dataNotific = tratarData(dados.DT_NOTIFIC);
    dados = {
      ...dados,
      DT_NOTIFIC: dataNotific,
      ID_DADOS_CLINICOS: idDadosClinicos,
    }   

    const { rows } = await this.database.raw(`
      INSERT INTO notificacao (
        id_dados_clinicos, dt_notific, sg_uf_not,
        sem_not, id_municip, id_regiona
      ) VALUES (
        :ID_DADOS_CLINICOS, :DT_NOTIFIC, :SG_UF_NOT, :SEM_NOT, :ID_MUNICIP, :ID_REGIONA
      ) RETURNING *;
    `, dados);

    return rows[0];
  }
}

module.exports = { Notificacao };