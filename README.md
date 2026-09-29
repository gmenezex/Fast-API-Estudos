# Fast-API-Estudos
Estudos de Fast API Python

----------
### **Aula 01**:

Vamos criar o arquivo main.py

Criar o ambiente virtual no python:
python -m venv venv

Depois vamos instalar as dependencias do projeto:

FASTAPI > PARA CRIAR A API

UVICORN > PARA GERENCIAR AS REQUISIÇÕES

SQLALCHEMY > PARA USAR O BANCO DE DADOS

PASSLIB[BCRYPT] > PARA CRIPTOGRAFAR AS SENHAS DE FORMA SEGURA

PYTHON-JOSE[cryptography] > PERMITIR CRIAR OS TOKENS JWT (SISTEMA DE AUTENTICAÇÃO DA API)

PYTHON-DOTENV > CRIAR O ARQUIVO PARA ARMAZENAR INFORMAÇÕES NAS VARIAVEIS DE AMBIENTE

PYTHON-MULTIPART > DEPENDENCIA DO PYTHON-JOSE


pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] python-dotenv python-multipart

Sempre que quiser colocar a api no ar, vamos rodar o comando:

uvicorn main:app --reload

Para puxar uma instancia do Fast API
Dentro do main.py vamos importar o fastapi e depois instanciar sua classe.

`from fastapi import FastAPI

app = FastAPI()`