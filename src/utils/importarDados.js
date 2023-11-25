const CsvReadableStream = require('csv-reader');
const fs = require('fs');
const { paciente, hospital, notificacao, dadosClinicos } = require('../database');

class Fila {
  fila = [];
  callback = null;
  finalizar = false;

  constructor(callback) {
    this.callback = callback;
    this.executar();
  }

  async inserir(funcao) {
    this.fila.push(funcao);
  }

  async executar() {
    while (!this.finalizar && this.fila.length > 0) {
      const promisesArray = [];
      let interador = 0;

      while (interador < 1000) {
        const funcao = this.fila.shift(1000);
        if (!funcao) break;
        promisesArray.push(funcao());
      }

      await Promise.all(promisesArray);
    }

    this.callback();
  }

  async finalizar() {
    this.finalizar = true;
  }
}

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
    const fila = new Fila(resolve);
    fila.executar();

    // Leitura assíncrona do arquivo CSV 
    for await (const linha of inputStream) {
      fila.inserir(() => inserirLinha(linha));
    }

    // Finaliza a função
    resolve();
  });
}