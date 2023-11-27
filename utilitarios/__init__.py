from .tratadorDeDados import tratarLinha

from database.paciente import Paciente
from database.sintoma import Sintoma
from database.hospital import Hospital
from database.notificacao import Notificacao
from database.dados_clinicos import DadosClinicos
from database.dados_atendimento import DadosAtendimento
from database.dados_laboratorial import DadosLaboratoriais
from database.conclusao import Conclusao

import psycopg2
import csv

def inserir_dados(connection):
    paciente = Paciente(connection)
    sintoma = Sintoma(connection)
    hospital = Hospital(connection)
    notificacao = Notificacao(connection)
    dadosClinicos = DadosClinicos(connection)
    dadosAtendimento = DadosAtendimento(connection)
    dadosLaboratoriais = DadosLaboratoriais(connection)
    conclusao = Conclusao(connection)

    paciente.criarTabela()
    hospital.criarTabela()
    dadosClinicos.criarTabela()
    dadosLaboratoriais.criarTabela()
    dadosAtendimento.criarTabela()
    notificacao.criarTabela()
    conclusao.criarTabela()
    sintoma.criarTabela()

    with open('dados.csv', 'r') as file:
        csv_reader = csv.DictReader(file, delimiter = ';')
        next(csv_reader) 

        try:
            for linha in csv_reader:
                linha = tratarLinha(linha)
                novoPaciente = paciente.criar(linha)
                idHospital = hospital.pegarIdOuCriar(linha)
                idDadosClinicos = dadosClinicos.criar(novoPaciente[0], linha)
                notificacao.criar(idDadosClinicos, linha)
                idDadosAtendimento = dadosAtendimento.criar(idDadosClinicos, idHospital, linha)

                conclusao.criar(idDadosAtendimento, linha)
                dadosLaboratoriais.criar(idDadosClinicos, linha)
                sintoma.criar(idDadosClinicos, linha)
                
        except (csv.Error, psycopg2.Error) as e:
            print(f"Erro encontrado -> {e}")

    connection.commit()
    print("Dados inseridos com sucesso!")
    
    
 