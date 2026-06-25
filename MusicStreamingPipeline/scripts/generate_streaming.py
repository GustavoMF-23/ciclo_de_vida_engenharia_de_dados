import pandas as pd
from faker import Faker
import random
import json
import os
import uuid
from datetime import datetime, timedelta

# Gera o arquivo de simulações, a partir do arquivo de músicas e o de usuários
# Inicializa o Faker

fake = Faker("pt_BR")

# ==========================
# CONFIGURAÇÕES
# ==========================

NUM_EVENTOS = 50000          # Quantidade de eventos a gerar
NUM_USUARIOS = 10000         # Deve corresponder ao users.csv

# Cria a pasta caso não exista
os.makedirs("data/raw", exist_ok=True)

# Carrega o catálogo de músicas
music_df = pd.read_csv("data/raw/music.csv")

# Obtém os IDs reais das músicas
music_ids = music_df["music_id"].tolist()

# Distribuição das ações
acoes = ["play", "like", "skip"]
pesos = [0.80, 0.10, 0.10]

# Dispositivos possíveis
devices = [
    "mobile",
    "desktop",
    "tablet",
    "smart_tv"
]

# ==========================
# GERAÇÃO DOS EVENTOS
# ==========================

with open("data/raw/events.jsonl",
    "w",
    encoding="utf-8"
) as arquivo:

    for _ in range(NUM_EVENTOS):

        evento = {
            "user_id": random.randint(1, NUM_USUARIOS),

            # Escolhe uma música existente
            # "music_id": random.choice(music_ids),
  #          "music_id": random.choices(
  #              population=music_ids,
  #              weights=range(len(music_ids), 0, -1),
  #          )[0],
            "music_id": random.choice(
                 music_ids
           ),

            "action": random.choices(
                acoes,
                weights=pesos,
                k=1
            )[0],

            "timestamp": (
                datetime.now()
                - timedelta(
                    days=random.randint(0, 30),
                    hours=random.randint(0, 23),
                    minutes=random.randint(0, 59),
                    seconds=random.randint(0, 59),
                )
            ).isoformat(),

            "device": random.choice(devices),

            "session_id": str(uuid.uuid4())
        }

        arquivo.write(
            json.dumps(evento) + "\n"
        )

print(f"{NUM_EVENTOS} eventos gerados com sucesso em events.jsonl")
