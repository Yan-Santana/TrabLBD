const {
  dadosLaboratoriais,
  dadosAtendimento,
  dadosClinicos,
  notificacao,
  hospital,
  conclusao,
  paciente
} = require('./database');

const importarDados = require('./utils/importarDados');
const path = require('path');

const main = async () => {
  // Cria as tabelas no banco de dados se não existir
  await paciente.criarTabela();
  await hospital.criarTabela();
  await dadosLaboratoriais.criarTabela();
  await dadosClinicos.criarTabela();
  await dadosAtendimento.criarTabela();
  await notificacao.criarTabela();
  await conclusao.criarTabela();

  console.log('Banco de dados sincronizado com sucesso!');
  console.log('Iniciando importação dos dados');

  // Importa os dados do arquivo CSV
  await importarDados(path.resolve(__dirname, '..', 'entrada.csv'));

  console.log('Importação concluída com sucesso!');
  //return process.exit(0);
}

main();