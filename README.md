# Projeto-Heeds 
## Trata-se de aplicação Django para gerenciamento de locais visitados.
### Configuração para rodar o projeto

Download Project

    git clone https://github.com/samueloliveiraf/projeto-heeds.git


Install PostgreSQL

    sudo apt -y install postgresql postgresql-contrib
    
PostgreSQL

    sudo su - postgres
    psql
    CREATE DATABASE dbname;

Install PostGIS

(postgresql-12-postgis-3) a numeração 12 é referente a versão do postgres coloque a sua versão exemple: (postgresql-12-postgis-3) caso sua vesão seja 12...

    sudo apt install postgis postgresql-12-postgis-3

PostgreSQL

    sudo su - postgres
    psql
    CREATE EXTENSION postgis;

Intall Python
    
    sudo apt -y install build-essential python3-venv python3-dev libpq-dev
    
---------------------------------------------------------------------
### Os camandos a seguir tem ser executado dentro da pasta do projeto
---------------------------------------------------------------------
   
Run Project

    python3 -m venv venv

Active venv

    source venv/bin/activate
    
Install Requirements

    pip install -r requirements.txt

Config .env

    touch .env
    vim .env
 Exemple: 
    
    DB_NAME=dbname
    DB_USER=postgres
    DB_PASSWORD=159753got42
    DB_HOST=localhost
    DB_PORT=5432

    SECRET_KEY=django-insecure-02s!=^#6cew&ko!%o^y@4x1le8=(uf^mvjjukoii@*cb74qx7q
    
-------------------------------------------------------------------
### A SECRET_KEY acima é a oficial do projeto
-------------------------------------------------------------------

Comands ends

    python manage.py migrate
    
Run

    python manage.py runserver

