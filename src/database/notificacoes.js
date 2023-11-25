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

  async criar() {

  }
}

module.exports = { Notificacao };