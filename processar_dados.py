import pandas as pd
from sqlalchemy import create_engine

# Configurações do banco de dados
DB_USER = 'postgres'
DB_PASSWORD = '200396'  # Senha que coloquei 200396
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'iot_data'  # Nome do banco de dados

# Caminho para o arquivo CSV
CSV_FILE_PATH = 'C:\\Users\\Victor Silva\\meuambiente\\IOT-temp.csv' # Substitua com o caminho para seu CSV

def processar_dados():
    # Conectar ao banco de dados PostgreSQL
    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
    
    # Ler o arquivo CSV usando pandas
    df = pd.read_csv(CSV_FILE_PATH)
    
    # Inserir os dados no banco de dados
    df.to_sql('temperature_readings', engine, if_exists='replace', index=False)
    print("Dados inseridos no banco de dados com sucesso!")

if __name__ == "__main__":
    processar_dados()
