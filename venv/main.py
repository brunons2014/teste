import requests
import sqlalchemy
import time
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# 1. Configuração do banco (Conecta ao serviço 'db' do Docker)
engine = create_engine('postgresql://usuario:senha@localhost:5432/clima_db')
Base = declarative_base()

class RegistroClima(Base):
    __tablename__ = 'clima'
    id = Column(sqlalchemy.Integer, primary_key=True)
    cidade = Column(String)
    descricao = Column(String)
    temperatura = Column(Float)
    data_hora = Column(DateTime, default=datetime.now)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# 2. Consulta à API do OpenWeatherMap
API_KEY = "d79de0249cd455e8aac686f898f03317"
cidade = "campo grande"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dict = requisicao.json()

descricao = requisicao_dict['weather'][0]['description']
temperatura = requisicao_dict['main']['temp'] - 273.15
print(descricao, f"{temperatura:.2f}°C")

# 3. Armazenamento dos dados no banco
novo_registro = RegistroClima(
    cidade=cidade,
    descricao=descricao,
    temperatura=temperatura
)

session.add(novo_registro)
session.commit()

print(f"Dados armazenados no banco de dados com sucesso. {cidade}, {descricao}, {temperatura:.2f}°C")