# "id_paciente": id_paciente,
def obter_dados_residencia_csv(linha):
    return {
         
        "sg_uf": linha["SG_UF"],
        "id_rg_resi": linha["ID_RG_RESI"],
        "id_mn_resi": linha["ID_MN_RESI"],
        "cs_zona": linha["CS_ZONA"],
        "id_pais": linha["ID_PAIS"],
    }
