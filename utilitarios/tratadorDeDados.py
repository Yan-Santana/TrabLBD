"""
@description Trata todas as datas que vem do banco de dados para o formato dd/mm/yyyy
@param {string | None} data 
@returns string | None
"""
from datetime import datetime  # Adicionando a importação correta

def tratarData(data):
    if not data == None:
        # Correção do índice aqui (de data para 0)
        return datetime.strptime(data, "%d/%m/%Y")
    else:
        return None

def tratarLinha(linha):
    atributos = linha.keys()

    for atributo in atributos:
        if linha[atributo] == '':
            linha[atributo] = None
            
    return linha
