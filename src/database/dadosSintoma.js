class DadosSintoma {
    /** 
     * @param {Knex} database 
     */
    constructor(database) {
      this.database = database;
    }
  
    async criarTabela() {
      await this.database.raw(`
        CREATE TABLE IF NOT EXISTS dados_sintoma (
          id_sintoma SERIAL PRIMARY KEY,
          id_dados_clinicos INT,
          ignorado BOOLEAN
        )
      `);
    }
  
    async criar(id_sintoma, id_dados_clinicos, dados) { 
        dados = {
            ...dados,
            ID_SINTOMA: id_sintoma,
            ID_DADOS_CLINICOS: id_dados_clinicos,
        }

        const { rows } = await this.database.raw(`
        INSERT INTO sintoma (
        id_sintoma,
        id_dados_clinicos,
        ) VALUES (
        :id_sintoma,
        :id_dados_clinicos,
        ) RETURNING *;
      `, dados);
  
      return rows[0];
    }
  }
  
  module.exports = { DadosSintoma };