const CsvReadableStream = require('csv-reader');
const fs = require('fs');

const { tratarLinha } = require('./tratadorDeDados');

const {
  paciente,
  hospital,
  notificacao,
  dadosClinicos,
  conclusao,
  dadosAtendimento,
  dadosLaboratoriais
} = require('../database');

const { contarLinhasArquivo } = require('./csv');

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
    linha = tratarLinha(linha);
    const novoPaciente = await paciente.criar(linha);
    const idHospital = await hospital.pegarIdOuCriar(linha);
    const idDadosClinicos = await dadosClinicos.criar(novoPaciente.id_paciente, linha);
    const novaNotificacao = await notificacao.criar(idDadosClinicos, linha);
    const novaConclusao = await conclusao.criar(idDadosClinicos, linha);
    const novoDadosAtendimento = await dadosAtendimento.criar(idDadosClinicos, linha);
    const novoDadosLaboratoriais = await dadosLaboratoriais.criar(idDadosClinicos, linha);
  };

  return new Promise(async (resolve, reject) => {
    const totalDados = await contarLinhasArquivo(filePath) - 1;
    let dadosInseridos = 0;

    inputStream.on('readable', async () => {
      while (true) {
        const maximoConcorrencia = 100;
        const arrayDePromises = [];

        while (arrayDePromises.length < maximoConcorrencia) {
          const linha = inputStream.read();

          if (!linha) break;
          arrayDePromises.push(inserirLinha(linha));
        }

        dadosInseridos += arrayDePromises.length;
        await Promise.all(arrayDePromises);

        if (dadosInseridos === totalDados) {
          return resolve();
        }
      }
    });
  });
}