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
        id_paciente INTEGER REFERENCES paciente(id_paciente),
        sg_uf VARCHAR(2),
        id_rg_resi VARCHAR(64),
        id_mn_resi VARCHAR(64),
        cs_zona VARCHAR(1),
        id_pais VARCHAR(20)
      )
    `);
  }

  async criar(idPaciente, dados) {
    dados = {
      ...dados,
      ID_PACIENTE: idPaciente
    };

    const { rows } = await this.database.raw(`
      INSERT INTO residencia (
        sg_uf, id_rg_resi, id_mn_resi,
        cs_zona, id_pais, id_paciente
      ) VALUES ( 
        :SG_UF, :ID_RG_RESI, :ID_MN_RESI,
        :CS_ZONA, :ID_PAIS, :ID_PACIENTE
      ) RETURNING *;
    `, dados);

    return rows[0];
  }
}

module.exports = { Residencia };