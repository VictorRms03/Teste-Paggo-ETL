import httpx
import pandas as pd
from sqlalchemy import create_engine
import datetime

DATABASE_URL = "postgresql://postgres:postgres@localhost:5434/alvo_db";

def main():

    # Inserindo data desejada
    date_input = input("Digite a data (YYYY-MM-DD): ")
    date = datetime.datetime.strptime(date_input, "%Y-%m-%d")

    # Definindo o intervalo de tempo para a consulta
    start_time = date.isoformat()
    end_time = (date + datetime.timedelta(days=1)).isoformat()

    # URL da API do backend
    url = f"http://localhost:8000/data?start_time={start_time}&end_time={end_time}&variables=wind_speed,power"

    #Requisição para o backend
    with httpx.Client() as client:
        response = client.get(url)
        response.raise_for_status()
        data = response.json()

    # Convertendo dados para DataFrame
    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df.set_index("timestamp", inplace=True)

    # Resample e agregação dos dados
    agg = df.resample("10T").agg(["mean", "min", "max", "std"])
    agg.columns = ['_'.join(col) for col in agg.columns]

    # Salvando os dados no banco de dados alvo
    engine = create_engine(DATABASE_URL)
    agg.to_sql('signal', con=engine, if_exists='append', index=True)

if __name__ == "__main__":
    main()