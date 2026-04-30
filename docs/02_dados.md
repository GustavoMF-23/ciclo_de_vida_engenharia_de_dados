# 2. Definição e Classificação dos Dados

O projeto utilizará diferentes fontes de dados, combinando dados operacionais (batch) e dados de streaming (tempo real), com o objetivo de simular o funcionamento de uma plataforma de streaming de música.

---

## Fontes de Dados

| Fonte                     | Descrição                                                             | Formato   | Volume Estimado                    | Frequência         | Latência   |
| ------------------------- | --------------------------------------------------------------------- | --------- | ---------------------------------- | ------------------ | ---------- |
| Logs de Reprodução        | Eventos de reprodução de músicas contendo usuário, música e timestamp | JSON      | ~30.000 eventos/dia                | Streaming contínuo | Segundos   |
| Interações (likes, skips) | Ações dos usuários como curtidas e pulos de faixa                     | JSON      | ~10.000 eventos/dia                | Streaming contínuo | Segundos   |
| Usuários                  | Dados cadastrais dos usuários (idade, país, plano)                    | CSV / SQL | ~10.000 usuários                   | Batch diário       | Até 24h    |
| Catálogo de Músicas       | Metadados das músicas (artista, gênero, duração)                      | CSV       | ~50.000 registros (quase estático) | Batch semanal      | Até 7 dias |

---

## 2.1 Classificação dos Dados

Os dados do projeto podem ser classificados em duas categorias principais:

### Dados operacionais

Incluem o cadastro de usuários e o catálogo de músicas.
São dados estruturados, armazenados em bancos relacionais ou arquivos CSV, e processados em batch.

Esses dados representam o estado estático ou de baixa frequência de atualização do sistema.

### Dados de streaming

Incluem logs de reprodução e interações dos usuários.
São dados semi-estruturados, gerados continuamente em tempo real, com alta frequência e baixa latência.

Esses dados representam o comportamento dinâmico dos usuários na plataforma e possuem alto volume.

---

No protótipo, os dados serão simulados via scripts Python e/ou carregados a partir de datasets externos.

Quando gerados por scripts, poderão utilizar bibliotecas como:

* `faker` → para simular dados realistas
* `random` → para gerar variações de comportamento

---

## 2.2 Resumo das Fontes

* **Origem dos dados:** aplicação simulada (eventos) e datasets externos (CSV)
* **Formatos utilizados:** JSON (streaming), CSV e SQL (operacional)
* **Periodicidade:** tempo real (streaming) e batch (diário ou eventual)
* **Latência esperada:** segundos (streaming) e horas (batch)

---

## 2.3 Exemplos de Campos por Fonte

### Logs de Reprodução (JSON)

```
user_id
music_id
timestamp
device
session_id
```

### Interações (JSON)

```
user_id
music_id
action (like, skip)
timestamp
```

### Usuários (usuarios.csv / PostgreSQL)

```
user_id
idade
país
tipo_plano
```

### Catálogo de Músicas (musicas.csv)

```
music_id
artista
gênero
duração
```
