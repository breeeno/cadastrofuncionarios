from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Funcionario(BaseModel):
    name: str
    idade: float
    salario: float
    cpf: float
    contato: float


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/funcionarios/{funcionarios_id}")
def read_funcionario(funcionarios_id: int, funcionarios: Funcionario):
    return {"funcionarios_id": funcionarios_id, "funcionarios_name": funcionarios.name}


@app.post("/funcionarios/")
def create_funcionario(funcionario: Funcionario):
    return funcionario


@app.put("/funcionarios/{funcionarios_id}")
def update_item(funcionarios_id: int, funcionarios: Funcionario):
    return {"funcionarios_id": funcionarios_id, "funcionarios_name": funcionarios.name}


@app.delete("/funcionarios/{funcionarios_id}")
def detele_funcionario(funcionario: Funcionario):
    return "Funcionario excluido com sucesso."
