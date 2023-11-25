const CsvReadableStream = require('csv-reader');
const fs = require('fs');
const { paciente, residencia } = require('../database');

/**
 * @param {string} filePath 
 */
module.exports = async (filePath) => {
  const leitorCsv = new CsvReadableStream({
    parseNumbers: true,
    parseBooleans: true,
    trim: true,
    delimiter: ';',
    asObject: true
  });

  // Cria um stream de leitura do arquivo CSV
  const inputStream = fs.createReadStream(filePath, 'utf8').pipe(leitorCsv);

  // Função para inserir uma linha no banco de dados
  const inserirLinha = async (linha) => {
    const novoPaciente = await paciente.criar(linha);
    const novaResidencia = await residencia.criar(novoPaciente.id_paciente, linha);
  };

  return new Promise(async (resolve, reject) => {
    // Leitura assíncrona do arquivo CSV 
    for await (const linha of inputStream) {
      await inserirLinha(linha);
    }

    // Finaliza a função
    resolve();
  });
}