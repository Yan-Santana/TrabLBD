from datetime import datetime

def obter_dados_paciente_csv(linha):
    return { 
            "cs_sexo": linha["CS_SEXO"], 
            "dt_nasc": datetime.strptime(linha["DT_NASC"], "%d/%m/%Y") if linha["DT_NASC"] != "" else None, 
            "nu_idade_n": linha["NU_IDADE_N"],
            "tp_idade": linha["TP_IDADE"], 
            "cs_raca": linha["CS_RACA"], 
            "cs_gestant": linha["CS_GESTANT"], 
            "cs_escol_n": linha["CS_ESCOL_N"],
            "pac_cocbo": linha["PAC_COCBO"],
        }
    