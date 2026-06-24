# 5. Tecnologias

A implementação do pipeline seguirá uma abordagem modular, cobrindo todas as etapas do ciclo de vida de dados: ingestão, armazenamento, processamento, orquestração e consumo.

As tecnologias foram escolhidas considerando:
* Viabilidade em ambiente local
* Facilidade de uso
* Aderência às práticas modernas de engenharia de dados

Inicialmente, a ideia era utilizar as tecnologias descritas abaixo:
| Tecnologia          | Função             |
| ------------------- | ------------------ |
| Python + Faker      | Simulação          |
| PostgreSQL          | Dados operacionais |
| Kafka (opcional)    | Streaming          |
| Airbyte             | Ingestão           |
| Data Lake           | Armazenamento      |
| Parquet             | Otimização         |
| Pandas              | Processamento      |
| Spark (opcional)    | Escala             |
| Airflow             | Orquestração       |
| Power BI / Metabase | Visualização       |
| FastAPI             | API                |

Principais adaptações em relação ao planejamento original
* Kafka → substituído por um gerador de eventos em Python (Faker) que grava arquivos JSON na camada Bronze, reduzindo a complexidade operacional, mas mantendo o conceito de streaming
* Airflow → substituído por um script orchestrator.py que executa o pipeline de ponta a ponta
* Spark → substituído por pandas, adequado ao volume de dados do protótipo
* PostgreSQL → substituído por arquivos CSV/Parquet para simplificar a implantação, já que simplifica a configuração e mantém o fluxo ETL
* Fast API → substituído pelo Power BI, utilizando como camada de consumo os dados da Gold. 

| Tecnologia          | Função                          |
| ------------------- | --------------------------------|
| Python              | Desenvolvimento dos pipelines   |
| Faker               | Geração de dados simulados      |
| Parquet             | Armazenamento otimizado         |
| Pandas              | Processamento de dados          |
| JSON                | Eventos de streaming            |
| Power BI            | Visualização  e análise         |
| Git/GitHub          | Versionamento                   |

________________________________________


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
