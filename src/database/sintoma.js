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
        id_dados_clinicos INTEGER REFERENCES dados_clinicos(id_dados_clinicos),
        nome VARCHAR(32),
        ignorado BOOLEAN DEFAULT(false)
      )
    `);
  }

  async criar(idDadosClinicos, dados) { 
    const tratarIgnorado = (valor) => {
      if (valor === '1' || valor === '2') return true
      return false;
    }

    dados = {
      FEBRE: tratarIgnorado(dados["FEBRE"]),
      TOSSE: tratarIgnorado(dados["TOSSE"]),
      GARGANTA: tratarIgnorado(dados["GARGANTA"]),
      DISPNEIA: tratarIgnorado(dados["DISPNEIA"]),
      DESC_RESP: tratarIgnorado(dados["DESC_RESP"]),
      SATURACAO: tratarIgnorado(dados["SATURACAO"]),
      DIARREIA: tratarIgnorado(dados["DIARREIA"]),
      VOMITO: tratarIgnorado(dados["VOMITO"]),
      DOR_ABD: tratarIgnorado(dados["DOR_ABD"]),
      FADIGA: tratarIgnorado(dados["FADIGA"]),
      PERD_OLFT: tratarIgnorado(dados["PERD_OLFT"]),
      PERD_PALA: tratarIgnorado(dados["PERD_PALA"]),
    };

    let sql = `
      INSERT INTO sintoma (
        nome,
        id_dados_clinicos,
        ignorado
      ) VALUES
    `;

    Object.keys(dados).forEach(sintoma => {
      // Insere a tupla
      sql = sql.concat(`('${sintoma}', ${idDadosClinicos}, ${dados[sintoma]}),`);
    });

    // Finalizando a instrução
    sql = sql.substring(0, sql.length - 1) + ';' + sql.substring(sql.length -1 + 1)

    await this.database.raw(sql, dados);
  }
}

module.exports = { Sintoma };