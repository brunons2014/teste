import requests
import sqlalchemy
import time
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# 1. Configuração do banco (Conecta ao serviço 'db' do Docker)
# Nota: 'db' é o nome do serviço definido no seu docker-compose.yml
engine = create_engine('postgresql://usuario:senha@db:5432/clima_db')
Base = declarative_base()

class RegistroClima(Base):
    __tablename__ = 'clima'
    id = Column(Integer, primary_key=True)
    cidade = Column(String)
    descricao = Column(String)
    temperatura = Column(Float)
    data_hora = Column(DateTime, default=datetime.now)

# Cria a tabela se não existir
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Variáveis da API
API_KEY = "d79de0249cd455e8aac686f898f03317"
cidade = "campo grande"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

def capturar_e_salvar():
    """Função que realiza a captura da API e salva no banco"""
    try:
        # Consulta à API
        requisicao = requests.get(link)
        requisicao_dict = requisicao.json()

        if requisicao.status_code == 200:
            descricao = requisicao_dict['weather'][0]['description']
            temperatura = requisicao_dict['main']['temp'] - 273.15

            # Armazenamento no banco
            novo_registro = RegistroClima(
                cidade=cidade,
                descricao=descricao,
                temperatura=temperatura
            )

            session.add(novo_registro)
            session.commit()
            print(f"[{datetime.now()}] Sucesso: {cidade} | {descricao} | {temperatura:.2f}°C")
        else:
            print(f"Erro na API: {requisicao.status_code}")
            
    except Exception as e:
        print(f"Erro durante a execução: {e}")
        session.rollback() # Reverte em caso de erro no banco

# 3. Loop de execução automática
if __name__ == "__main__":
    print("Iniciando monitoramento climático...")
    while True:
        capturar_e_salvar()
        
        # Define o intervalo (ex: 3600 segundos = 1 hora)
        # Para testar rápido, você pode colocar 60 (1 minuto)
        print("Aguardando 1 hora para a próxima atualização...")
        time.sleep(3600)