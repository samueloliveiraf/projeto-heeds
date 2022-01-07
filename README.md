# Projeto-Heeds 
## Trata-se de aplicação Django para gerenciamento de locais visitados...
### Configuração para rodar o projeto


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
