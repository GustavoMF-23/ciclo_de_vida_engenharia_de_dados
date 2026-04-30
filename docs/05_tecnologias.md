# 5. Tecnologias

A implementação do pipeline seguirá uma abordagem modular, cobrindo todas as etapas do ciclo de vida de dados: ingestão, armazenamento, processamento, orquestração e consumo.

As tecnologias foram escolhidas considerando:

* Viabilidade em ambiente local
* Facilidade de uso
* Aderência às práticas modernas de engenharia de dados

---

## Tecnologias Utilizadas

| Tecnologia               | Função                              | Camada da Arquitetura |
| ------------------------ | ----------------------------------- | --------------------- |
| Python (scripts + Faker) | Geração de eventos simulados        | Origem de Dados       |
| PostgreSQL               | Armazenamento de dados operacionais | Origem de Dados       |
| CSV                      | Fonte de dados externa              | Origem de Dados       |
| Apache Kafka (opcional)  | Broker de mensagens                 | Ingestão (Streaming)  |
| Airbyte / Python         | Ingestão batch                      | Ingestão (Batch)      |
| Data Lake (local)        | Armazenamento centralizado          | Armazenamento         |
| JSON / CSV               | Dados brutos                        | Bronze                |
| Parquet                  | Formato otimizado                   | Silver / Gold         |
| Python (pandas)          | Processamento batch                 | Processamento         |
| Apache Spark (opcional)  | Processamento distribuído           | Processamento         |
| Apache Airflow           | Orquestração                        | Orquestração          |
| Power BI / Metabase      | Visualização                        | Consumo               |
| FastAPI                  | Exposição via API                   | Consumo               |

---

## 5.1 Ingestão

A ingestão será dividida entre **streaming** e **batch**.

### 5.1.1 Streaming

Eventos (logs de reprodução e interações) serão gerados por scripts em Python simulando usuários.

Modo avançado: envio via Kafka.

```python
from kafka import KafkaConsumer
import json
import os
from datetime import datetime

consumer = KafkaConsumer(
    'music_events',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='music-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

output_path = "data/bronze/streaming/"
os.makedirs(output_path, exist_ok=True)

for message in consumer:
    event = message.value
    file_name = f"{output_path}events_{datetime.utcnow().strftime('%Y%m%d')}.json"
    
    with open(file_name, "a") as f:
        f.write(json.dumps(event) + "\n")
```

---

### 5.1.2 Batch

Dados de usuários e músicas serão carregados de CSV ou PostgreSQL.

```python
import pandas as pd
import os

input_users = "data/raw/users.csv"
input_music = "data/raw/music.csv"
output_path = "data/bronze/batch/"

os.makedirs(output_path, exist_ok=True)

df_users = pd.read_csv(input_users)
df_users.to_csv(f"{output_path}users_bronze.csv", index=False)

df_music = pd.read_csv(input_music)
df_music.to_csv(f"{output_path}music_bronze.csv", index=False)
```

---

### 5.1.3 Organização das Pastas

```
data/
├── raw/
│   ├── users.csv
│   └── music.csv
├── bronze/
│   ├── streaming/
│   └── batch/
├── silver/
└── gold/
```

---

## 5.2 Armazenamento

O armazenamento será baseado em um **Data Lake local**, seguindo a arquitetura medalhão:

* **Bronze:** dados brutos
* **Silver:** dados tratados
* **Gold:** dados agregados

**Formatos:**

* JSON / CSV (bruto)
* Parquet (otimizado)

**Banco relacional:**

* PostgreSQL para dados operacionais

**Justificativa:**

* Parquet melhora desempenho e reduz armazenamento
* Separação em camadas facilita governança e reprocessamento

---

## 5.3 Processamento e Transformação

### 🔹 Batch

* Python + pandas
* Limpeza, joins e agregações

### 🔹 Streaming (simplificado)

* Processamento incremental dos eventos

### 🔹 Escala (opcional)

* Apache Spark

**Justificativa:**

* pandas atende bem cenários acadêmicos
* Spark permite simular escala real

---

### Transformação (Silver → Gold)

* **Silver:** dados limpos
* **Gold:** dados agregados e prontos para consumo
* Formato: Parquet

---

## 5.4 Orquestração

**Ferramenta:** Apache Airflow

Responsável por:

* Agendamento de pipelines
* Controle de dependências
* Monitoramento

**Justificativa:**
Automatiza e garante confiabilidade do fluxo de dados.

---

## 5.5 Consumo de Dados

Os dados da camada Gold serão disponibilizados via:

* Power BI / Metabase
* Dashboards de uso e engajamento
* API (FastAPI - opcional)

**Justificativa:**
Transformar dados em valor acessível para stakeholders.

---

## 5.6 Ciclo de Vida dos Dados

### Segurança

* Controle de acesso
* Anonimização de dados sensíveis

### Gestão de Dados

* Padronização de schemas
* Organização em camadas

### DataOps

* Versionamento com Git
* Automação de pipelines
* Reprodutibilidade

### Monitoramento

* Logs (Airflow)
* Detecção de falhas

### Governança

* Definição de ownership
* Controle de qualidade
* Rastreabilidade (linhagem de dados)

---
