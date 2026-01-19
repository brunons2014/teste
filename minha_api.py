from fastapi import FastAPI
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from main import RegistroClima  # Importa a classe que você já criou
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Conecta ao banco (no Docker use 'db', local use 'localhost')
engine = create_engine('postgresql://usuario:senha@localhost:5432/clima_db')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/clima")
def buscar_clima():
    with Session(engine) as session:
        # Busca todos os registros do banco
        statement = select(RegistroClima).order_by(RegistroClima.data_hora.desc())
        resultados = session.execute(statement).scalars().all()
        return resultados