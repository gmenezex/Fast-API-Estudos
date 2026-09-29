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

----------
### **Aula 02**:

Nessa aula vai ser abordada a criação de rotas dentro do sistema.

Acessar os endpoint, como por exemplo:
127.0.0.1/ordens

As requisições para as rotas/endpoins são:
#GET:  Leitura/Pegar
#POST:  Enviar/Criar
#PUT/PATH:  Alterar/Editar
#DELETE:  Deletar

##### Vamos criar as rotas
------
Como vai ser um sistema para pizzaria com usuario e pedido, vai ser criado duas rotas.
Pedidos:
order_routes.py
Autenticação:
auth_routes.py

Depois precisamos informar para o FASTAPI, quais são as rotas do sistema dentro do arquivo main.py
`
from fastapi import FastAPI

app = FastAPI()

from auth_routes import auth_router
from order_routes import order_router
`

Depois vamos instanciar o roteador dentro do arquivo de rota, por exemplo no arquivo auth_routes.py:
`
# Criando um roteador no arquivo
from fastapi import APIRouter

 Roteador de authenticação
 Nele precisamos passar 2 parametros ()
 prefix > caminho que vai ser acessado a rota, exemplo: 127.0.0.1/auth
 tag > Precisamos colocar as tags para ser gerada a documentação de forma automatica

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)
`

Depois disso, precisamos fazer o app incluir as rotas no aplicativo, vai ser feito dentro do main.py
Exemplo:
app.include_router(auth_router)
app.include_router(order_router)

Agora vamos criar uma rota dentro do order_routes.py
Vamos usar um decoretor, informando o caminho e depois 
vinculando ele em uma função.
Vamos sempre dar um retorno em json.
Se colocamos entre """""" uma mensagem, ela vai ficar gravada na documentação do FASTAPI
`
@order_router.get('/')
async def pedidos():
    """
        Essa é a rota padrão de pedidos do nosso sistema. Todas as rotas de pedidos precisam
        de autenticação.
    """
    return {"mensagem" : "Você acessou a rota de pedidos"}
`

