class Paciente {
  /** 
   * @param {Knex} database 
   */
  constructor(database) {
    this.database = database;
  }

  async criarTabela() {
    await this.database.raw(`
      CREATE TABLE IF NOT EXISTS paciente (
        id_paciente SERIAL PRIMARY KEY,
        cs_sexo VARCHAR(1),
        dt_nasc DATE NULL,
        nu_idade_n VARCHAR(3),
        tp_idade VARCHAR(1),
        cs_raca VARCHAR(2),
        cs_gestant VARCHAR(1),
        cs_escol_n VARCHAR(1),
        pac_cocbo VARCHAR(6)
      )
    `);
  }

  async criar(dados) {
    const dataSplitada = dados.DT_NASC.split('/');
    const dataNascimentoTratada = dataSplitada.length !== 1 ? new Date(Date.parse(`${dataSplitada[1]}/${dataSplitada[0]}/${dataSplitada[2]}`)) : null;
    dados = {
      ...dados,
      DT_NASC: dataNascimentoTratada,
    }

    const { rows } = await this.database.raw(`
      INSERT INTO paciente (
        cs_sexo, dt_nasc, nu_idade_n,
        tp_idade, cs_raca, cs_gestant, cs_escol_n,
        pac_cocbo
      ) VALUES (
        :CS_SEXO, :DT_NASC, :NU_IDADE_N,
        :TP_IDADE, :CS_RACA, :CS_GESTANT, :CS_ESCOL_N, 
        :PAC_COCBO
      ) RETURNING *;
    `, dados);

    return rows[0];
  }
}

module.exports = { Paciente };