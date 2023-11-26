const { tratarData } = require('../utils/tratadorDeDados');

class DadosAtendimento {
  /** 
   * @param {Knex} database 
   */
  constructor(database) {
    this.database = database;
  }

  async criarTabela() {
    await this.database.raw(`
      CREATE TABLE IF NOT EXISTS dados_atendimento (
        id_cod_atendimento SERIAL PRIMARY KEY,
        id_dados_clinicos INTEGER REFERENCES dados_clinicos(id_dados_clinicos),
        id_hospital INTEGER REFERENCES hospital(id_hospital),
        antiviral VARCHAR(1),
        tp_antivir VARCHAR(1),
        dt_antivir DATE,
        hospital VARCHAR(1),
        dt_interna DATE,
        sg_uf_inte VARCHAR(2),
        id_rg_inte VARCHAR(64),
        id_mn_inte VARCHAR(64),
        uti VARCHAR(1),
        dt_entuti DATE,
        dt_saiduti DATE,
        suport_ven VARCHAR(1),
        raiox_res VARCHAR(1),
        dt_raiox DATE,
        tomo_res VARCHAR(6) NULL,
        tomo_out VARCHAR(99),
        dt_tomo DATE,
        amostra VARCHAR(1),
        dt_coleta DATE,
        tp_amostra VARCHAR(30)
      )
    `);
  }

  async criar(idDadosClinicos, idHospital, dados) {
    const dtAntivir = tratarData(dados.DT_ANTIVIR);
    const dtInterna = tratarData(dados.DT_INTERNA);
    const dtEntuti = tratarData(dados.DT_ENTUTI);
    const dtSaiduti = tratarData(dados.DT_SAIDUTI);
    const dtRaiox = tratarData(dados.DT_RAIOX);
    const dtTomo = tratarData(dados.DT_TOMO);
    const dtColeta = tratarData(dados.DT_COLETA);

    dados = {
      ...dados,
      DT_ANTIVIR: dtAntivir,
      DT_INTERNA: dtInterna,
      DT_ENTUTI: dtEntuti,
      DT_SAIDUTI: dtSaiduti,
      DT_RAIOX: dtRaiox,
      DT_TOMO: dtTomo,
      DT_COLETA: dtColeta,
      ID_DADOS_CLINICOS: idDadosClinicos,
      ID_HOSPITAL: idHospital,
    }

    const { rows } = await this.database.raw(`
      INSERT INTO dados_atendimento (
        id_dados_clinicos, antiviral, tp_antivir,
        id_hospital, dt_antivir, hospital, 
        dt_interna, sg_uf_inte, id_rg_inte, 
        id_mn_inte, uti, 
        dt_entuti, dt_saiduti, suport_ven, 
        raiox_res, dt_raiox, tomo_res, 
        tomo_out, dt_tomo, amostra, 
        dt_coleta, tp_amostra
      ) VALUES (
        :ID_DADOS_CLINICOS, :ANTIVIRAL, :TP_ANTIVIR, 
        :ID_HOSPITAL, :DT_ANTIVIR, :HOSPITAL, 
        :DT_INTERNA, :SG_UF_INTE, :ID_RG_INTE, 
        :ID_MN_INTE, :UTI, 
        :DT_ENTUTI, :DT_SAIDUTI, :SUPORT_VEN, 
        :RAIOX_RES, :DT_RAIOX, :TOMO_RES, 
        :TOMO_OUT, :DT_TOMO, :AMOSTRA, 
        :DT_COLETA, :TP_AMOSTRA
      ) RETURNING id_cod_atendimento;
    `, dados);

    return rows[0].id_cod_atendimento;
  }
}

module.exports = { DadosAtendimento };