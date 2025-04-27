# Processo Seletivo Paggo - Teste Prático ETL

Candito: Victor Ramos

## Como rodar a aplicação:

### Bancos de Dados e API:

Apenas utilize o comando `docker compose up -d --build` no terminal com o Docker Desktop aberto

### Aplicação ETL:

Utilizaremos o venv para controle das dependências do projeto.

Para usar o venv, utilize os seguintes comando no terminal:

- `py -m venv venv` (Iniciar o venv no projeto)

- `venv\Scripts\activate` (Ativar o venv)

- `pip install -r etl/requirements.txt` (Instalar dependências do projeto no ambiente venv)

- `python etl/main.py` (Executar o ETL)

## Periodos de dados contidos no Banco de Dados Fonte:

- timestamp: 2025-04-01 00:00:00 a 2025-04-11 00:00:00
- wind_speed: 0 a 25
- power: 0 a 5000
- ambient_temperature: -10 a 40