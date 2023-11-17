from db import execute_query, commit_changes
from db import execute_query, commit_changes

def create_table_dados_laboratorial():
    query = """
        CREATE TABLE dados_laboratoriais (
            requi_gal SERIAL PRIMARY KEY,
            tp_tes_an INTEGER,
            dt_res_an DATE,
            res_an VARCHAR(1),
            lab_an VARCHAR(70),
            co_lab_an VARCHAR(7),
            pos_an_flu VARCHAR(1),
            tp_flu_an VARCHAR(1),
            pos_an_out VARCHAR(1),
            an_sars2 VARCHAR(1),
            an_vsr VARCHAR(1),
            vsr VARCHAR(1),
            an_para1 VARCHAR(1),
            an_para2 VARCHAR(1),
            an_para3 VARCHAR(1),
            an_adeno VARCHAR(1),
            an_outro VARCHAR(1),
            ds_an_out VARCHAR(30),
            pcr_resul VARCHAR(1),
            dt_pcr DATE,
            pos_pcrflu VARCHAR(1),
            tp_flu_pcr VARCHAR(1),
            pcr_fluasu VARCHAR(1),
            fluasu_out VARCHAR(30),
            pcr_flubli VARCHAR(1),
            flubli_out VARCHAR(30),
            pos_pcrout VARCHAR(1),
            pcr_sars2 VARCHAR(1),
            pcr_vsr VARCHAR(1),
            pcr_para1 VARCHAR(1),
            pcr_para2 VARCHAR(1),
            pcr_para3 VARCHAR(1),
            pcr_para4 VARCHAR(1),
            pcr_adeno VARCHAR(1),
            pcr_metap VARCHAR(1),
            pcr_boca VARCHAR(1),
            pcr_rino VARCHAR(1),
            pcr_outro VARCHAR(1),
            ds_pcr_out VARCHAR(30),
            lab_pcr VARCHAR(7),
            tp_am_sor INTEGER,
            sor_out VARCHAR(100),
            dt_cor_sor DATE,
            tp_sor INTEGER,
            out_sor VARCHAR(100),
            res_sor VARCHAR(1),
            res_igg VARCHAR(1),
            res_igm VARCHAR(1),
            res_iga VARCHAR(1),
            dt_res DATE
        )
        """
    return query

   
execute_query(create_table_dados_laboratorial())
commit_changes()