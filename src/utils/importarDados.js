const CsvReadableStream = require('csv-reader');
const fs = require('fs');
const { default: PQueue } = require('p-queue');

const { paciente, hospital, notificacao, dadosClinicos, conclusao, dadosAtendimento } = require('../database');

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
    const novaConclusao = await conclusao.criar(idDadosClinicos, linha);
    const novoDadosAtendimento = await dadosAtendimento.criar(idDadosClinicos, linha);
  };

  return new Promise(async (resolve, reject) => {
    const fila = new PQueue({ concurrency: 1000, autoStart: true, interval: 0 });

    inputStream.on('data', async (linha) => {
      await fila.add(async () => inserirLinha(linha));
    })
      .on('end', async () => {
        fila.onEmpty().then(() => {
          resolve();
        });
      });
  });
}