const { tratarData } = require('../utils/tratadorDeDados');

class DadosLaboratoriais {
  /** 
   * @param {Knex} database 
   */
  constructor(database) {
    this.database = database;
  }

  async criarTabela() {
    await this.database.raw(`
      CREATE TABLE IF NOT EXISTS dados_laboratoriais (
        requi_gal SERIAL PRIMARY KEY,
        id_dados_clinicos INTEGER,
        tp_tes_an INTEGER,
        dt_res_an DATE,
        res_an VARCHAR(1),
        pos_an_flu VARCHAR(1),
        tp_flu_an VARCHAR(1),
        pos_an_out VARCHAR(1),
        an_sars2 VARCHAR(1),
        an_vsr VARCHAR(1),
        an_para1 VARCHAR(1),
        an_para2 VARCHAR(1),
        an_para3 VARCHAR(1),
        an_adeno VARCHAR(1),
        an_outro VARCHAR(1),
        ds_an_out VARCHAR(30),
        pcr_resul VARCHAR(1),
        dt_pcr DATE,
        pos_pcrflu VARCHAR(1),
        tp_flu_pcr VARCHAR(1),
        pcr_fluasu VARCHAR(1),
        fluasu_out VARCHAR(30),
        pcr_flubli VARCHAR(1),
        flubli_out VARCHAR(30),
        pos_pcrout VARCHAR(1),
        pcr_sars2 VARCHAR(1),
        pcr_vsr VARCHAR(1),
        pcr_para1 VARCHAR(1),
        pcr_para2 VARCHAR(1),
        pcr_para3 VARCHAR(1),
        pcr_para4 VARCHAR(1),
        pcr_adeno VARCHAR(1),
        pcr_metap VARCHAR(1),
        pcr_boca VARCHAR(1),
        pcr_rino VARCHAR(1),
        pcr_outro VARCHAR(1),
        ds_pcr_out VARCHAR(30),
        tp_am_sor VARCHAR(12),
        sor_out VARCHAR(100),
        tp_sor INTEGER NULL,
        out_sor VARCHAR(100),
        res_igg VARCHAR(1),
        res_igm VARCHAR(1),
        res_iga VARCHAR(1),
        dt_res DATE
      )
    `);
  }

  async criar(idDadosClinicos, dados) {
  const dtPcr = tratarData(dados.DT_PCR);
  const dtRes = tratarData(dados.DT_RES);
  const dtResAn = tratarData(dados.DT_RES_AN);

  dados = {
    ...dados,
    DT_PCR: dtPcr,
    DT_RES: dtRes,
    DT_RES_AN: dtResAn,
    ID_DADOS_CLINICOS: idDadosClinicos,
  }

  const { rows } = await this.database.raw(`
  INSERT INTO dados_laboratoriais (
    tp_tes_an, dt_res_an, res_an,
    pos_an_flu, tp_flu_an, pos_an_out,
    an_sars2, an_vsr, an_para1,
    an_para2, an_para3, an_adeno, an_outro,
    ds_an_out, pcr_resul, dt_pcr, pos_pcrflu,
    tp_flu_pcr, pcr_fluasu, fluasu_out, pcr_flubli,
    flubli_out, pos_pcrout, pcr_sars2, pcr_vsr,
    pcr_para1, pcr_para2, pcr_para3, pcr_para4,
    pcr_adeno, pcr_metap, pcr_boca, pcr_rino,
    pcr_outro, ds_pcr_out, tp_am_sor,
    sor_out, tp_sor, out_sor,
    res_igg, res_igm, res_iga,
    dt_res, id_dados_clinicos
  ) VALUES (
    :TP_TES_AN, :DT_RES_AN, :RES_AN, 
    :POS_AN_FLU, :TP_FLU_AN, :POS_AN_OUT,
    :AN_SARS2, :AN_VSR, :AN_PARA1,
    :AN_PARA2, :AN_PARA3, :AN_ADENO, :AN_OUTRO,
    :DS_AN_OUT, :PCR_RESUL, :DT_PCR, :POS_PCRFLU,
    :TP_FLU_PCR, :PCR_FLUASU, :FLUASU_OUT, :PCR_FLUBLI,
    :FLUBLI_OUT, :POS_PCROUT, :PCR_SARS2, :PCR_VSR,
    :PCR_PARA1, :PCR_PARA2, :PCR_PARA3, :PCR_PARA4,
    :PCR_ADENO, :PCR_METAP, :PCR_BOCA, :PCR_RINO,
    :PCR_OUTRO, :DS_PCR_OUT, :TP_AM_SOR,
    :SOR_OUT, :TP_SOR, :OUT_SOR,
    :RES_IGG, :RES_IGM, :RES_IGA,
    :DT_RES, :ID_DADOS_CLINICOS
  ) RETURNING *;
`, dados);

return rows[0];
}

}

module.exports = { DadosLaboratoriais };