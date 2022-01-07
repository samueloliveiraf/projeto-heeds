# Projeto-Heeds 
## Trata-se de aplicação Django para gerenciamento de locais visitados...
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

(postgresql-13-postgis-3) a numeração 13 é referente ao a versão do postgres coloque a sua versão ex: (postgresql-12-postgis-3) caso sua vesão seja 12...

    sudo apt install postgis postgresql-13-postgis-3

PostgreSQL

    sudo su - postgres
    psql
    CREATE EXTENSION postgis;

Intall Python
    
    sudo apt -y install sudo apt install python3 build-essential python3-venv python3-dev libpq-dev python3-pip
    
-------------------------------------------------------------------
### Os camandos a seguir tem ser executado dentro da pasta projeto
-------------------------------------------------------------------
   
Run Project

    python -m venv venv

Active venv

    sourch venv/bin/activate
    
Install Requirements

    pip install -r requirements.txt

Config .env

    touch .env
