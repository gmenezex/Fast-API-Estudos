# Criando um roteador no arquivo
from fastapi import APIRouter

# Roteador de authenticação
# Nele precisamos passar 2 parametros ()
# prefix > caminho que vai ser acessado a rota, exemplo: 127.0.0.1/auth
# tag > Precisamos colocar as tags para ser gerada a documentação de forma automatica
auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@auth_router.get('/')
async def autenticar():
    """
    Essa é a rota padrão de autenticação do nosso sistema
    """
    return {"mensagem" : "Você acessou a rota padrão de autenticação", "autenticado": False}