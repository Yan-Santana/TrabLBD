class Sintoma {
  /** 
   * @param {Knex} database 
   */
  constructor(database) {
    this.database = database;
  }

  async criarTabela() {
    await this.database.raw(`
      CREATE TABLE IF NOT EXISTS sintoma (
        id_sintoma SERIAL PRIMARY KEY,
        nome VARCHAR(32)
      )
    `);
  }

  async criar(dados) { 
    const { rows } = await this.database.raw(`
      INSERT INTO sintoma (
       nome
      ) VALUES (
       :NOME
      ) RETURNING *;
    `, dados);

    return rows[0];
  }
}

module.exports = { Sintoma };