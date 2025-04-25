-- CREATE DATABASE fonte_db

-- Criação da tabela (se ainda não existir)
CREATE TABLE IF NOT EXISTS data (
    timestamp TIMESTAMP PRIMARY KEY,
    wind_speed DECIMAL(4, 2),
    power DECIMAL(10, 2),
    ambient_temperature DECIMAL(4,2)
);

-- Inserção de dados aleatórios por 10 dias (1 registro por minuto)
DO $$
DECLARE
    timeStampAtual TIMESTAMP := '2025-04-01 00:00:00';
    timeStampFinal TIMESTAMP := '2025-04-11 00:00:00';
BEGIN
    WHILE timeStampAtual < timeStampFinal LOOP
        INSERT INTO data (timestamp, wind_speed, power, ambient_temperature)
        VALUES (
            timeStampAtual,
            ROUND( ( random() * 25)::NUMERIC, 2 ), -- wind_speed entre 0 e 25
            ROUND( ( random() * 5000)::NUMERIC, 2 ), -- power entre 0 e 5000
            ROUND( ( (random() * 50 - 10)::NUMERIC), 2 ) -- ambient_temperature entre -10 e 40
        );
        timeStampAtual := timeStampAtual + INTERVAL '1 minute';
    END LOOP;
END
$$;

-- SELECT * FROM data ORDER BY "timestamp" DESC 