const { tratarData } = require('../utils/tratadorDeDados');
const { Knex } = require('knex');

class Conclusao {
  /** 
   * @param {Knex} database 
   */
  constructor(database) {
    this.database = database;
  }

  async criarTabela() {
    await this.database.raw(`
      CREATE TABLE IF NOT EXISTS conclusao (
        id_conclusao SERIAL PRIMARY KEY,
        id_cod_atendimento INTEGER,
        classi_fin VARCHAR(1),
        classi_out VARCHAR(30),
        criterio VARCHAR(1),
        evolucao VARCHAR(1),
        dt_evoluca DATE,
        dt_encerra DATE,
        nu_do VARCHAR(10),
        observa VARCHAR(999),
        nome_prof VARCHAR(60),
        reg_prof VARCHAR(15)
      )
    `);
  }

async criar(dados) {
  const dtEvoluca = tratarData(dados.DT_EVOLUCA);
  const dtEncerra = tratarData(dados.DT_ENCERRA);
  dados = {
    ...dados,
    DT_EVOLUCA: dtEvoluca,
    DT_ENCERRA: dtEncerra,
  }

  const { rows } = await this.database.raw(`
    INSERT INTO conclusao (
      id_cod_atendimento, classi_fin, classi_out,
      criterio, evolucao, dt_evoluca,
      dt_encerra, nu_do, observa,
      nome_prof, reg_prof
    ) VALUES (
      :ID_COD_ATENDIMENTO, :CLASSI_FIN, :CLASSI_OUT,
      :CRITERIO, :EVOLUCAO, :DT_EVOLUCA,
      :DT_ENCERRA, :NU_DO, :OBSERVA,
      :NOME_PROF, :REG_PROF
    ) RETURNING *;
  `, {
    ...dados,
    dt_evoluca: dtEvolucaoTratada, // Substituindo a data tratada no objeto de dados
  });

  return rows;
}

}

module.exports = { Conclusao };