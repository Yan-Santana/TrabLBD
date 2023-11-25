const CsvReadableStream = require('csv-reader');
const fs = require('fs');
const { paciente, hospital, notificacao, dadosClinicos } = require('../database');

/**
 * @param {string} filePath 
 */
module.exports = async (filePath) => {
  const leitorCsv = new CsvReadableStream({
    trim: true,
    delimiter: ';',
    asObject: true
  });

  // Cria um stream de leitura do arquivo CSV
  const inputStream = fs.createReadStream(filePath, 'utf8').pipe(leitorCsv);

  // Função para inserir uma linha no banco de dados
  const inserirLinha = async (linha) => {
    const novoPaciente = await paciente.criar(linha);
    const idHospital = await hospital.pegarIdOuCriar(linha);
    const idDadosClinicos = await dadosClinicos.criar(novoPaciente.id_paciente, linha);
    const novaNotificacao = await notificacao.criar(idDadosClinicos, linha);
  };

  return new Promise(async (resolve, reject) => {
    // Leitura assíncrona do arquivo CSV 
    for await(const linha of inputStream) {
      inserirLinha(linha);
    }



    // Finaliza a função
    resolve();
  });
}