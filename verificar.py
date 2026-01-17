from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://usuario:senha@localhost:5432/clima_db')
df = pd.read_sql('SELECT * FROM clima', engine)

print("--- Dados no Banco de Dados ---")
print(df)