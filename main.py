from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Cliente(BaseModel):
    nome: str
    email: str

clientes = [
    {"id": 1, "nome": "João Silva", "email": "joao@email.com"},
    {"id": 2, "nome": "Maria Oliveira", "email": "maria@email.com"},
    {"id": 3, "nome": "Carlos Souza", "email": "carlos@email.com"}
]

id_counter = 4

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à minha API com FastAPI!"}

@app.get("/clientes")
def listar_clientes():
    return clientes

@app.get("/clientes/{cliente_id}")
def buscar_cliente(cliente_id: int):
    for cliente in clientes:
        if cliente["id"] == cliente_id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente não encontrado")

@app.post("/clientes")
def criar_cliente(cliente: Cliente):
    global id_counter
    novo_cliente = {
        "id": id_counter,
        "nome": cliente.nome,
        "email": cliente.email
    }
    clientes.append(novo_cliente)
    id_counter += 1
    return novo_cliente

@app.put("/clientes/{cliente_id}")
def atualizar_cliente(cliente_id: int, dados: Cliente):
    for cliente in clientes:
        if cliente["id"] == cliente_id:
            cliente["nome"] = dados.nome
            cliente["email"] = dados.email
            return cliente
    raise HTTPException(status_code=404, detail="Cliente não encontrado")

@app.delete("/clientes/{cliente_id}")
def deletar_cliente(cliente_id: int):
    for i, cliente in enumerate(clientes):
        if cliente["id"] == cliente_id:
            del clientes[i]
            return {"mensagem": "Cliente removido com sucesso"}
    raise HTTPException(status_code=404, detail="Cliente não encontrado")