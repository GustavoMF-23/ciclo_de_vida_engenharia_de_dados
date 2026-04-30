# 4. Arquitetura — Fluxo de Dados

## 4.1 Arquitetura Escolhida

A arquitetura adotada segue o modelo **Lakehouse** com o padrão **Medalhão (Bronze → Silver → Gold)**, integrando processamento **batch** e **streaming** em um único pipeline.

### Objetivos da Arquitetura

* Ingestão de dados em tempo real e em lote
* Armazenamento escalável e desacoplado
* Transformações progressivas com aumento de qualidade
* Disponibilização eficiente para consumo analítico

---

## 4.2 Fluxo de Dados

O fluxo de dados ocorre nas seguintes etapas:

### 1. Origem dos Dados

* Aplicação de streaming (eventos simulados)
* Bases operacionais (usuários e catálogo)

### 2. Ingestão

* **Streaming:** eventos enviados continuamente
* **Batch:** dados carregados periodicamente

### 3. Armazenamento (Data Lake)

* **Bronze:** dados brutos (JSON / CSV)
* **Silver:** dados tratados e limpos
* **Gold:** dados agregados e prontos para análise

### 4. Processamento

* **Batch:** agregações históricas
* **Streaming:** métricas em tempo quase real

### 5. Consumo

* Dashboards (BI)
* APIs de recomendação

---

## 4.3 Separação entre Streaming e Batch

### Streaming

Fluxo contínuo de eventos:

eventos → ingestão → bronze → processamento incremental

### Batch

Fluxo periódico:

CSV / banco → ingestão → processamento → camadas refinadas

---

## 4.4 Justificativa da Arquitetura

O modelo **Lakehouse** combina:

* Flexibilidade do **Data Lake** (dados brutos e variados)
* Estrutura analítica do **Data Warehouse**

### Benefícios

* Redução de custos (armazenamento mais barato)
* Suporte a múltiplos tipos de processamento
* Facilidade de evolução do projeto

---

### Arquitetura Medalhão

A organização em camadas melhora qualidade, governança e reprocessamento:

* **Bronze:** preservação dos dados originais
* **Silver:** limpeza e padronização
* **Gold:** dados prontos para consumo

---

A arquitetura foi projetada priorizando:

* Desacoplamento
* Escalabilidade
* Reprocessamento

Permitindo suporte tanto para análises históricas quanto em tempo real.

---

## 4.5 Trade-offs

| Aspecto         | Decisão                               | Impacto  | Justificativa                        |
| --------------- | ------------------------------------- | -------- | ------------------------------------ |
| Acoplamento     | Arquitetura em camadas                | Baixo    | Facilita manutenção                  |
| Escalabilidade  | Separação armazenamento/processamento | Alta     | Crescimento sem mudanças estruturais |
| Disponibilidade | Batch + Streaming                     | Moderada | Depende dos pipelines                |
| Confiabilidade  | Dados brutos no Bronze                | Alta     | Permite reprocessamento              |
| Reversibilidade | Preservação dos dados                 | Alta     | Correção sem perda                   |
| Latência        | Batch vs Streaming                    | Variável | Equilíbrio custo/tempo               |
| Complexidade    | Arquitetura híbrida                   | Alta     | Necessária para múltiplos cenários   |
| Custo           | Data Lake                             | Baixo    | Armazenamento econômico              |

---
