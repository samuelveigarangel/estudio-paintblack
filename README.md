# Sistema de gestão e agendamento (Estúdio de Tatuagem e Barbearia)
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/samuelveigarangel/estudio-paintblack/blob/main/LICENSE)

<h1 align="center">Sobre o projeto</h1>

<p align="center">
 <a href="#sobre-o-projeto">Sobre</a> •
 <a href="#tecnologias-usadas">Tecnologias Usadas</a> •
 <a href="#implantação-em-produção">Implantação em Produção</a> •
 <a href="#como-executar-o-projeto">Como Executar o Projeto</a>
</p>


## Index
* [Sobre o projeto](#sobre-o-projeto)
    * [Entrar](#entrar)
* [Tecnologias Usadas](#tecnologias-usadas)
* [Implantação em produção](#implantação-em-produção)
* [Como executar o projeto](#como-executar-o-projeto)


# Página inicial
# Cadastro 
# Cliente
# Dashboard
# Sobre o projeto

Com o intuíto de melhorar a gestão de um estúdio de tatuagem e barbearia, foi desenvolvido uma aplicação 
que realiza o cadastro de novos clientes e o agendamento de serviços de tatuagem e corte de cabelo. Além 
disso, aplicação é composta por um dashboard com informações de pagamento individual de funcionários, 
faturamento e quantidade de atendimentos no mês.



# Tecnologias Usadas
## Back end
- Python
- Django
- SQlite

## Front end
- HTML
- CSS
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