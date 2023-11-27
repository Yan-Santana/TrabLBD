from utilitarios.tratadorDeDados import tratarData

class Paciente:
  def __init__(self, database):
    self.database = database

  def criarTabela(self):
    cursor = self.database.cursor()

    cursor.execute('''
      CREATE TABLE IF NOT EXISTS paciente (
        id_paciente SERIAL PRIMARY KEY,
        cs_sexo VARCHAR(1),
        dt_nasc DATE NULL,
        nu_idade_n VARCHAR(3),
        tp_idade VARCHAR(1),
        cs_raca VARCHAR(2),
        cs_gestant VARCHAR(1),
        cs_escol_n VARCHAR(1),
        pac_cocbo VARCHAR(6)
      )
    ''')

    
    cursor.close()

  def criar(self, dados):
    cursor = self.database.cursor()

    dataNascimentoTratada = tratarData(dados['DT_NASC'])
    dados = {
      **dados,
      'DT_NASC': dataNascimentoTratada,
    }

    cursor.execute('''
      INSERT INTO paciente (
        cs_sexo, dt_nasc, nu_idade_n,
        tp_idade, cs_raca, cs_gestant, cs_escol_n,
        pac_cocbo
      ) VALUES (
          %(CS_SEXO)s, %(DT_NASC)s, %(NU_IDADE_N)s,
          %(TP_IDADE)s, %(CS_RACA)s, %(CS_GESTANT)s, %(CS_ESCOL_N)s,
          %(PAC_COCBO)s
      ) RETURNING *;
    ''', dados)

    row = cursor.fetchone()
    
    cursor.close()

    return row
