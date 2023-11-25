const { Conclusao } = require('./conclusao');
const { DadosAtendimento } = require('./dadosAtendimento');
const { DadosClinicos } = require('./dadosClinicos');
const { DadosLaboratoriais } = require('./dadosLaboratoriais');
const { Notificacao } = require('./notificacoes');
const { Paciente } = require('./pacientes');
const { Residencia } = require('./residencias');

const knex = require('knex');

const DB_NAME = "SRAG"
const DB_USER = "postgres"
const DB_PASSWORD = "minhasenha"
const DB_HOST = "localhost"
const DB_PORT = "5433"

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

module.exports = {
  conclusao: new Conclusao(database),
  dadosAtendimento: new DadosAtendimento(database),
  dadosClinicos: new DadosClinicos(database),
  dadosLaboratoriais: new DadosLaboratoriais(database),
  notificacao: new Notificacao(database),
  paciente: new Paciente(database),
  residencia: new Residencia(database),
}