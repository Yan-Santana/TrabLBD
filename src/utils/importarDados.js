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

  const inputStream = fs.createReadStream(filePath, 'utf8').pipe(leitorCsv);

  const inserirLinha = async (linha) => {
    const novoPaciente = await paciente.criar(linha);
    const novaResidencia = await residencia.criar(novoPaciente.id_paciente, linha);
  };

  return new Promise(async (resolve, reject) => {
    for await (const linha of inputStream) {
      await inserirLinha(linha);
    }

    resolve();
  });
}