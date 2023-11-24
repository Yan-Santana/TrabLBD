from datetime import datetime

def obter_dados_notificacao_csv(linha):
    return { 
        "dt_notific": datetime.strptime(linha["DT_NOTIFIC"], "%d/%m/%Y") if linha["DT_NOTIFIC"] != "" else None,
        "sg_uf_not": linha["SG_UF_NOT"],
        "sem_not": linha["SEM_NOT"],
        "id_municip": linha["ID_MUNICIP"],
        "id_regiona": linha["ID_REGIONA"],
        }