const {
  dadosLaboratoriais,
  dadosAtendimento,
  dadosClinicos,
  notificacao,
  residencia,
  conclusao,
  paciente
} = require('./database');

const importarDados = require('./utils/importarDados');
const path = require('path');

const main = async () => {
  await paciente.criarTabela();
  await residencia.criarTabela();
  await dadosLaboratoriais.criarTabela();
  await dadosClinicos.criarTabela();
  await dadosAtendimento.criarTabela();
  await notificacao.criarTabela();
  await conclusao.criarTabela();

  console.log('Banco de dados sincronizado com sucesso!');
  console.log('Iniciando importação dos dados');

  await importarDados(path.resolve(__dirname, '..', 'dados.csv'));

  console.log('Importação concluída com sucesso!');
  return process.exit(0);
}

main();