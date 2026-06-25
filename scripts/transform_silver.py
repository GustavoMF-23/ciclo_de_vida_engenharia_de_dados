import os
import pandas as pd


# Transforma a camada bronze em silver, com os tratamentos abaixo:
# remoção de duplicatas
# tratamento de  valores ausentes
#	conversão de datas
#	validação de tipos de dados

# ===================================
# CAMINHOS
# ===================================

BRONZE_BATCH = "data/bronze/batch"
BRONZE_STREAM = "data/bronze/streaming"

SILVER_PATH = "data/silver"

os.makedirs(SILVER_PATH, exist_ok=True)

# ===================================
# FUNÇÃO DE LIMPEZA GENÉRICA
# ===================================

def clean_dataframe(df):

    print(f"\nRegistros originais: {len(df)}")

    # 1. Remove duplicatas
    df = df.drop_duplicates()

    # 2. Remove espaços extras
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # 3. Trata valores ausentes
    for col in df.columns:

        if df[col].dtype == "object":

            df[col] = (
                df[col]
                .fillna("Desconhecido")
                .astype(str)
            )   
        else:

            df[col] = df[col].fillna(0)

    print(f"Registros após limpeza: {len(df)}")

    return df

# ===================================
# USERS
# ===================================

print("\nTransformando USERS...")

users = pd.read_parquet(
    f"{BRONZE_BATCH}/users_bronze.parquet"
)

users = clean_dataframe(users)

# valida tipos
users["user_id"] = users["user_id"].astype(int)

if "idade" in users.columns:
    users["idade"] = users["idade"].astype(int)

users.to_parquet(
    f"{SILVER_PATH}/users.parquet",
    index=False
)

print("Users Silver criada")

# ===================================
# MUSIC
# ===================================

print("\nTransformando MUSIC...")

music = pd.read_parquet(
    f"{BRONZE_BATCH}/music_bronze.parquet"
)

music = clean_dataframe(music)

# valida tipos
if "duration_ms" in music.columns:
    music["duration_ms"] = (
        pd.to_numeric(
            music["duration_ms"],
            errors="coerce"
        )
        .fillna(0)
        .astype(int)
    )
print("\n=== DTYPES ===")
print(music.dtypes)

text_cols = [
    "music_id",
    "title",
    "artist",
    "album",
    "genre",
    "release_date"
]

for col in text_cols:

    music[col] = (
        music[col]
        .replace(0, "Desconhecido")
        .fillna("Desconhecido")
        .astype(str)
    )
print("\nDEPOIS DA CORREÇÃO")

    
music.to_parquet(
    f"{SILVER_PATH}/music.parquet",
    index=False
)

print("Music Silver criada")

# ===================================
# EVENTS
# ===================================

print("\nTransformando EVENTS...")

events = pd.read_json(
    f"{BRONZE_STREAM}/events.jsonl",
    lines=True
)

events = clean_dataframe(events)

# converte timestamp
events["timestamp"] = pd.to_datetime(
    events["timestamp"],
    errors="coerce"
)

# remove timestamps inválidos
events = events.dropna(
    subset=["timestamp"]
)

# valida tipos
events["user_id"] = events["user_id"].astype(int)

events["music_id"] = events["music_id"].astype(str)

events.to_parquet(
    f"{SILVER_PATH}/events.parquet",
    index=False
)

print("Events Silver criada")

# ===================================
# QUALIDADE DOS DADOS
# ===================================

print("\nExecutando validações...")

print(
    "Users únicos:",
    users["user_id"].nunique()
)

print(
    "Músicas únicas:",
    music["music_id"].nunique()
)

print(
    "Eventos:",
    len(events)
)

print(
    "Data mínima:",
    events["timestamp"].min()
)

print(
    "Data máxima:",
    events["timestamp"].max()
)

print("\nTransformação Silver concluída com sucesso!")
