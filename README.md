# Sistema de gestão e agendamento (Estúdio de Tatuagem e Barbearia)
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/samuelveigarangel/estudio-paintblack/blob/master/LICENSE)

## Apêndice
* [Sobre o projeto](#sobre-o-projeto)
* [Funcionalidades](#funcionalidades)
    * [Início](#entrar)
    * [Cadastro](#cadastro)
    * [Cliente](#cliente)
        * [Serviço](#serviço)
        * [Editar](#editar)
        * [Histórico](#histórico)
    * [Dashboard](#dashboard)
* [Tecnologias Usadas](#tecnologias-usadas)
* [Implantação em produção](#implantação-em-produção)
* [Como executar o projeto](#como-executar-o-projeto)

# Sobre o projeto

Com o intuito de melhorar a gestão de um estúdio de tatuagem e barbearia, foi desenvolvido uma aplicação 
que realiza o cadastro de novos clientes e o agendamento de serviços de tatuagem e corte de cabelo. Além 
disso, aplicação é composta por um dashboard com informações de pagamento individual de funcionários, 
faturamento e quantidade de atendimentos no mês.

# Início
Tela inicial que mostra agenda do dia, além da opção de especificar algum dia da agenda.

![inicio](https://user-images.githubusercontent.com/82840278/171342518-5e5dd4b3-b49a-415e-95f4-56aab655e9ca.PNG)

# Cadastro 
Tela de cadastro de novos clientes com utilização de mask Jquery no campo telefone, além das validações básicas que o formulário django fornece.

![Cadastro](https://user-images.githubusercontent.com/82840278/171342446-da2b1f98-eaf7-4f43-9898-eb944cac2b7e.PNG)
# Cliente
Tela que procura clientes cadastrados no sistema. Para cada cliente, há opções de associar um novo serviço, editar serviços e histórico de serviços.

![procurar-cliente](https://user-images.githubusercontent.com/82840278/171342975-dc471118-9a1e-4c58-898f-03aecca4033f.PNG)
## Serviço
Tela que criar um novo serviço para o cliente. Há opções de você escolher o funcionário que irá fazer o serviço, o tipo de serviço (Tatuagem e Corte de Cabelo) e a data.

![criar-servico](https://user-images.githubusercontent.com/82840278/171342608-9f50784b-be84-4f92-b3ad-5c66fb920c60.PNG)
## Editar
Lista todos os serviços realizados e agendados do cliente com opções de editar e excluir. A opção editar criar um mesmo layout do criar serviço com os campos editáveis. Se selecionado opção excluir, aparecerá uma windows.confirm para confirmação de exclusão.

![list-servicos](https://user-images.githubusercontent.com/82840278/171343053-814b3bb3-530d-4fee-bc3d-59d4080484f2.PNG)
## Histórico
Mostra todos os serviços realizados e agendados do cliente.

![historico](https://user-images.githubusercontent.com/82840278/171343109-8a3b7e90-7b14-4d23-be89-4273b70251aa.PNG)
# Dashboard
Painel visual que apresenta informações gerais sobre o estúdio. Quantidade de tatuagens e cortes de cabelo no mês, faturamento de todos os meses do ano, pagamento de cada funcionário e o lucro. 
Para o gráfico do faturamento, foi utilizado biblioteca Chart.js. Se o faturamento do mês ficar abaixo de 2 mil reais, a barra ficará vermelha, acima disso, verde.

![dashboard](https://user-images.githubusercontent.com/82840278/171343148-6a34c546-cf1d-4dda-9a62-c002b8ad67ba.PNG)




# Tecnologias Usadas
## Back end
- Python 
- Django django
- SQlite

## Front end
- HTML
- CSS
- Bootstrap
- JS
- ChartJs

# Implantação em produção
- Back end: Heroku
- Banco de dados: Postgresql

# Como executar o projeto

```bash
# clonar repositório
git clone https://github.com/samuelveigarangel/estudio-paintblack.git

# Abra o prompt de comando e vá para pasta do projeto

# Crie um ambiente virtual
python -m venv venv

# Ative seu ambiente virtual
venv\Scripts\activate

# Instale os requerimentos 
pip install -r requirements.txt

# Faça o migrate para criar a dabatase
py manage.py migrate

# !! MUITO IMPORTANTE !!
# Configure .env
# Copie .env-exemple e renomeie para .env
# Abra .env 
# Preencha os campos conforme solicitado

# Crie um super user
python manage.py createsuperuser

# Colete os arquivos estáticos
python manage.py collectstatic

# Execute o projeto 
python manage.py runserver

```
