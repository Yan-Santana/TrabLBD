# Arquivo temporário para testes

import psycopg2
import csv

# Conectar ao PostgresSql
conn = psycopg2.connect (
    database="SRAG",
    user="postgres",
    password="minhasenha", 
    host="localhost", 
    port="5433"
)

# Criando o banco de dados
conn.autocommit = True
cursor = conn.cursor()
cursor.execute("CREATE DATABASE Teste")
cursor.close()

# Conectar ao banco
conn = psycopg2.connect (
    database="postgres",
    user="postgres",
    password="minhasenha",
    host="localhost",
    port="5433"
)

# Criar as tabelas
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTSpaciente (
        id_paciente SERIAL PRIMARY KEY,
        nm_paciente VARCHAR(70),
        nu_cpf VARCHAR(15),
        cs_sexo VARCHAR(1),
        dt_nasc DATE,
        nu_idade_n VARCHAR(3),
        tp_idade VARCHAR(1),
        cs_raca VARCHAR(2),
        cs_etnia VARCHAR(4),
        cs_gestant VARCHAR(1),
        cs_escol_n VARCHAR(1),
        pac_cocbo VARCHAR(6),
        nm_mae_pac VARCHAR(70)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTSnotificacao (
        id_notificacao SERIAL PRIMARY KEY,
        id_paciente INTEGER REFERENCES paciente(id_paciente),
        nu_notific VARCHAR(12),
        dt_notific DATE,
        sg_uf_not VARCHAR(2),
        sem_not VARCHAR(6),
        id_municip VARCHAR(6),
        id_regiona VARCHAR(6)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTSresidencia (
        id_residencia SERIAL PRIMARY KEY,
        id_paciente INTEGER REFERENCES paciente(id_paciente),
        nu_cep VARCHAR(8),
        sg_uf VARCHAR(2),
        id_rg_resi VARCHAR(6),
        id_mn_resi VARCHAR(6),
        nm_bairro VARCHAR(72),
        nm_logrado VARCHAR(50),
        nm_numero VARCHAR(8),
        nm_complem VARCHAR(15),
        nu_ddd_tel VARCHAR(4),
        cs_zona VARCHAR(1),
        id_pais VARCHAR(3)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTSdados_clinicos (
        id_dados_clinicos SERIAL PRIMARY KEY,
        id_paciente INTEGER REFERENCES paciente(id_paciente),
        histo_vgm VARCHAR(1),
        pais_vgm VARCHAR(3),
        lo_ps_vgm VARCHAR(30),
        dt_vgm DATE,
        dt_rt_vgm DATE,
        surto_sg VARCHAR(1),
        nosocomial VARCHAR(1),
        ave_suino VARCHAR(1),
        out_anim VARCHAR(60),
        febre VARCHAR(1),
        tosse VARCHAR(1),
        garganta VARCHAR(1),
        dispneia VARCHAR(1),
        desc_resp VARCHAR(1),
        saturacao VARCHAR(1),
        diarreia VARCHAR(1),
        vomito VARCHAR(1),
        dor_abd VARCHAR(1),
        fadiga VARCHAR(1),
        perd_olft VARCHAR(1),
        perd_pala VARCHAR(1),
        outro_sin VARCHAR(1),
        outro_des VARCHAR(30),
        fator_risc VARCHAR(1),
        puerpera VARCHAR(1),
        cardiopati VARCHAR(1),
        hematologi VARCHAR(1),
        sind_down VARCHAR(1),
        hepatica VARCHAR(1),
        asma VARCHAR(1),
        diabetes VARCHAR(1),
        neurologic VARCHAR(1),
        pneumopati VARCHAR(1),
        imunodepre VARCHAR(1),
        renal VARCHAR(1),
        obesidade VARCHAR(1),
        obes_imc VARCHAR(3),
        out_morbi VARCHAR(1),
        morb_desc VARCHAR(30),
        vacina VARCHAR(1),
        dt_ut_dose DATE,
        mae_vac VARCHAR(1),
        dt_vac_mae DATE,
        m_amamenta VARCHAR(1),
        dt_doseuni DATE,
        dt_1_dose DATE,
        dt_2_dose DATE,
        dat_sin_pri DATE
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTSdados_atendimento (
        cod_atendimento SERIAL PRIMARY KEY,
        id_dados_clinicos INTEGER REFERENCES dados_clinicos(id_paciente),
        antiviral VARCHAR(1),
        tp_antivir VARCHAR(1),
        out_antivir VARCHAR(30),
        dt_antivir DATE,
        hospital VARCHAR(1),
        dt_interna DATE,
        sg_uf_inte VARCHAR(2),
        id_rg_inte VARCHAR(6),
        id_mn_inte VARCHAR(20),
        id_un_inte VARCHAR(20),
        uti VARCHAR(1),
        dt_entuti DATE,
        dt_saiduti DATE,
        suport_ven VARCHAR(1),
        raiox_res VARCHAR(1),
        dt_raiox DATE,
        tomo_res INTEGER,
        tomo_out VARCHAR(100),
        dt_tomo DATE,
        amostra VARCHAR(1),
        dt_coleta DATE,
        tp_amostra VARCHAR(30),
        out_amostra VARCHAR(1)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTSdados_laboratoriais (
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
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTSconclusao (
        classi_fin VARCHAR(1),
        classi_out VARCHAR(30),
        criterio VARCHAR(1),
        evolucao VARCHAR(1),
        dt_evoluca DATE,
        dt_encerra DATE,
        nu_do VARCHAR(10),
        observa VARCHAR(999),
        nome_prof VARCHAR(60),
        reg_prof VARCHAR(15)
    )
""")

with open('entrada.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Pula a primeira linha
    for row in reader:
        cur.execute(
            "INSERT INTO teste VALUES (%s, %s)",
            row
        )
        
conn.commit()
cur.close()
conn.close()
