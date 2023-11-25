const { Conclusao } = require('./conclusao');
const { DadosAtendimento } = require('./dadosAtendimento');
const { DadosClinicos } = require('./dadosClinicos');
const { DadosLaboratoriais } = require('./dadosLaboratoriais');
const { Notificacao } = require('./notificacoes');
const { Paciente } = require('./pacientes');
const { Hospital } = require('./hospital');

const knex = require('knex');

// Configurações de conexão com o banco de dados	
const DB_NAME = "SRAG"
const DB_USER = "postgres"
const DB_PASSWORD = "minhasenha"
const DB_HOST = "localhost"
const DB_PORT = "5433"

// Instância de conexão com o banco de dados
const database = knex({
  client: 'pg',
  connection: {
    host: DB_HOST,
    port: DB_PORT,
    user: DB_USER,
    database: DB_NAME,
    password: DB_PASSWORD,
  }
});

// Exporta todas as instâncias das entidades
module.exports = {
  conclusao: new Conclusao(database),
  dadosAtendimento: new DadosAtendimento(database),
  dadosClinicos: new DadosClinicos(database),
  dadosLaboratoriais: new DadosLaboratoriais(database),
  notificacao: new Notificacao(database),
  paciente: new Paciente(database),
  hospital: new Hospital(database),
}