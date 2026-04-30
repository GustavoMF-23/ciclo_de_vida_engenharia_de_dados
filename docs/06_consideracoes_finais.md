# 6. Considerações Finais

## 6.1 Riscos e Limitações

| Risco                               | Probabilidade | Impacto | Nível de Risco | Mitigação                                           |
| ----------------------------------- | ------------- | ------- | -------------- | --------------------------------------------------- |
| Limitações de infraestrutura local  | Alta          | Médio   | Alto           | Uso de dados reduzidos e ferramentas leves (pandas) |
| Complexidade do streaming           | Média         | Alto    | Alto           | Implementação simplificada e Kafka opcional         |
| Baixa qualidade dos dados simulados | Média         | Médio   | Médio          | Uso de Faker e regras realistas                     |
| Integração entre ferramentas        | Média         | Alto    | Alto           | Padronização (Parquet) e testes incrementais        |
| Falhas na orquestração              | Baixa         | Alto    | Médio          | Uso de Airflow com retries e dependências           |
| Escalabilidade limitada             | Alta          | Médio   | Alto           | Arquitetura preparada para evolução futura          |

---

## 6.2 Próximos Passos

* Implementar ingestão de dados
* Criar estrutura do Data Lake
* Desenvolver pipelines batch e streaming
* Criar dashboards iniciais

---

## 6.3 Referências

* Databricks — *What is a Data Lakehouse?*
  https://www.databricks.com/glossary/data-lakehouse

* Databricks — *Medallion Architecture*
  https://docs.databricks.com/en/lakehouse/medallion.html

* Apache Software Foundation — *Apache Kafka Documentation*
  https://kafka.apache.org/documentation/

* Apache Software Foundation — *Apache Airflow Documentation*
  https://airflow.apache.org/docs/

* Amazon Web Services — *What is a Data Lake?*
  https://aws.amazon.com/what-is/data-lake/

---
