class Hospital {
  /** 
   * @param {Knex} database 
   */
  constructor(database) {
    this.database = database;
  }

  async criarTabela() {
    await this.database.raw(`
      CREATE TABLE IF NOT EXISTS hospital (
        id_hospital SERIAL PRIMARY KEY,
        id_unidade VARCHAR(64),
        id_rg_resi VARCHAR(64),
        id_mn_resi VARCHAR(64),
        sg_uf VARCHAR(2),
        cs_zona VARCHAR(1),
        id_pais VARCHAR(64)
      )
    `);
  }

  async pegarIdOuCriar(dados) {
    const hospital = await this.database.raw('SELECT id_hospital FROM hospital WHERE id_unidade = :ID_UNIDADE LIMIT 1', dados);

    // Se o hospital já existe, retorna o ID
    if (hospital.rows.length > 0) {
      return hospital.rows[0].id_hospital;
    }

    // Se não existe, cria um novo hospital
    const { rows } = await this.database.raw(`
      INSERT INTO hospital (
        id_unidade, sg_uf, id_rg_resi, id_mn_resi,
        cs_zona, id_pais
      ) VALUES ( 
        :ID_UNIDADE, 
        :SG_UF, :ID_RG_RESI, :ID_MN_RESI,
        :CS_ZONA, :ID_PAIS
      ) RETURNING id_hospital;
    `, dados);

    return rows[0].id_hospital;
  }
}

module.exports = { Hospital };