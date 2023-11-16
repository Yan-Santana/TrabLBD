# Trabalho de Laboratorio de banco de dados.

<hr>

### 🚀 Autores 🚀
  * [Beatriz Veron](https://github.com/Beatrizveron)
  * [Felipe Dos Anjos](https://github.com/FelipeDasr)
  * [Matheus Gil](https://github.com/MatheusSopranGil)
  * [Yan Santana](https://github.com/Yan-Santana)
    
## Detalhes do trabalho: [Trabalho LabBD - SRAG.pdf](https://github.com/Yan-Santana/TrabLBD/files/13252223/Trabalho.LabBD.-.SRAG.pdf)

<hr>

## Antes de tentar executar os comandos abaixo voce devera instalar o git. 
#### Link: `https://git-scm.com/downloads`

### Este documento descreve os passos necessários para criar uma nova pasta em seu computador, navegar até a pasta e inicializar um repositório Git, seguido da clonagem de um repositório remoto usando o comando git clone. Ele também inclui comandos auxiliares como git add e git push.:

  * I. Criar uma nova pasta no seu computador: `mkdir nome_da_sua_pasta`
  * II. Navegar até a pasta recém-criada: `cd nome_da_sua_pasta`
  * III. Inicializar um repositório Git: `git init`
  * IV. Clonar o repositório: `git clone https://github.com/Yan-Santana/TrabLBD.git` <br>
  * OBS: Os codigos acima so serao executado uma unica vez! Eles podem pedir que voce confirme seu e-mail e senha no primeiro acesso, exemplo: `git config --global user.name "Seu Nome"` - `git config --global user.email "seu_email@exemplo.com"`

<br>

####  Adicionar arquivos ao stage (área de preparação):

  * I. Antes de fazer commit das mudanças, você precisa adicionar os arquivos modificados à área de preparação. Você pode usar o comando git add seguido do nome do arquivo ou do caractere curinga '.' para adicionar todos os arquivos modificados: `git add nome_do_arquivo` ou `git add .` -> Isso prepara os arquivos para serem incluídos no próximo commit.
  * II. Depois de adicionar os arquivos ao stage, você pode realizar um commit das mudanças usando o seguinte comando: `git commit -m "Mensagem do commit aqui"`
  * III. Para enviar suas alterações para um repositório remoto, você pode usar o comando git push: `git push`
  * IV. Para puxar as alterações mais recentes de um repositório remoto para o seu repositório local, use o seguinte comando: `git pull` <br>
  * OBS: Antes de modificar qualquer coisa no código, lembre-se de executar o comando `git pull` para trazer as modificações mais recentes de outros colaboradores para o seu repositório local e garantir que você esteja trabalhando com a versão mais atualizada do código.

## Organizacao do codigo

├── db.py (conexão com o banco de dados)
├── tables/
|  ├── _init_.py
|  ├── paciente.py (criação da tabela paciente)
|  ├── notificacao.py (criação da tabela notificacao) 
|  ├── residencia.py (criação da tabela residencia)
|  ├── dados_clinicos.py (criação da tabela dados_clinicos)
|  ├── dados_atendimento.py (criação da tabela dados_atendimento)
|  ├── dados_laboratoriais.py (criação da tabela dados_laboratoriais)
|  └── conclusao.py (criação da tabela conclusao)
├── inserir_dados.py (inserção dos dados CSV) 
├── main.py (arquivo principal que executa todas as partes)