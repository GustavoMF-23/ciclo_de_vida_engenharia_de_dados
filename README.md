# Music Streaming Analytics Pipeline

---

## 1. Descrição do Projeto

### Contexto de Negócio

Uma plataforma fictícia de streaming de música deseja melhorar a experiência do usuário por meio de recomendações personalizadas, além de otimizar decisões de negócio com base no comportamento de escuta.

### Problema

Os dados de uso (reproduções, interações e preferências) estão dispersos e não estruturados, dificultando análises e geração de insights.

### Objetivos

* Centralizar dados de consumo musical
* Permitir análises históricas e em tempo real
* Suportar sistemas de recomendação
* Monitorar métricas de uso (engajamento, retenção)

### Stakeholders

* Equipe de Data / BI
* Equipe de Produto
* Equipe de Marketing
* Usuários finais (indiretamente)

---

## 2. Definição e Classificação dos Dados

### Fontes de Dados

| Fonte              | Descrição             | Formato | Volume   | Frequência    | Latência |
| ------------------ | --------------------- | ------- | -------- | ------------- | -------- |
| Logs de Reprodução | Eventos de reprodução | JSON    | ~30k/dia | Streaming     | Segundos |
| Interações         | Likes e skips         | JSON    | ~10k/dia | Streaming     | Segundos |
| Usuários           | Dados cadastrais      | CSV/SQL | ~10k     | Batch diário  | 24h      |
| Catálogo           | Metadados musicais    | CSV     | ~50k     | Batch semanal | 7 dias   |

### Classificação

**Dados Operacionais**

* Estruturados (CSV/SQL)
* Atualização baixa frequência
* Ex: usuários e catálogo

**Dados de Streaming**

* Semi-estruturados (JSON)
* Alta frequência e baixa latência
* Ex: reproduções e interações

### Resumo

* Origem: simulação + datasets externos
* Formatos: JSON, CSV, SQL
* Latência: segundos (streaming) / horas (batch)

---

## 3. Domínios e Serviços

### Domínios

| Domínio    | Responsabilidade      |
| ---------- | --------------------- |
| Usuário    | Dados cadastrais      |
| Catálogo   | Metadados musicais    |
| Interações | Eventos em tempo real |
| Analytics  | Insights              |

---

### Serviços

| Domínio    | Serviço    | Função                  |
| ---------- | ---------- | ----------------------- |
| Usuários   | Cadastro   | Criar usuários          |
| Usuários   | Consulta   | Ler dados               |
| Usuários   | Exportação | Batch                   |
| Catálogo   | Gestão     | Manter músicas          |
| Catálogo   | Consulta   | Metadados               |
| Catálogo   | Ingestão   | Carregar dados          |
| Interações | Geração    | Simular eventos         |
| Interações | Publicação | Enviar eventos          |
| Interações | Ingestão   | Persistir               |
| Analytics  | Batch      | Processamento histórico |
| Analytics  | Streaming  | Tempo real              |
| Analytics  | Modelagem  | Estruturar dados        |
| Analytics  | Exposição  | Servir dados            |

---

## 4. Arquitetura — Fluxo de Dados

### Arquitetura

Modelo **Lakehouse + Medalhão (Bronze → Silver → Gold)**

### Fluxo

1. Origem (eventos + dados batch)
2. Ingestão (streaming e batch)
3. Armazenamento (Data Lake)
4. Processamento
5. Consumo

### Camadas

* Bronze: dados brutos
* Silver: dados tratados
* Gold: dados agregados

### Trade-offs

* Alta escalabilidade
* Baixo custo
* Maior complexidade (batch + streaming)

---

## 5. Tecnologias

### Stack

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

---

### Estrutura

```
data/
├── raw/
├── bronze/
├── silver/
└── gold/
```

---

## 6. Considerações Finais

### Riscos

| Risco                   | Mitigação             |
| ----------------------- | --------------------- |
| Infraestrutura limitada | Uso de pandas         |
| Complexidade streaming  | Kafka opcional        |
| Dados simulados         | Faker                 |
| Integração              | Parquet               |
| Orquestração            | Airflow               |
| Escalabilidade          | Arquitetura preparada |

---

### Próximos Passos

* Implementar ingestão
* Criar Data Lake
* Desenvolver pipelines
* Criar dashboards

---

### Referências

* Databricks — Data Lakehouse
* Databricks — Medallion Architecture
* Apache Kafka Docs
* Apache Airflow Docs
* AWS — Data Lake

---
