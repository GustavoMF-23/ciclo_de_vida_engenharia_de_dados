import os
import pandas as pd

# Transformação da camada silver em Gold, gerando:
# Músicas mais tocadas
# Artistas mais tocados
# Reprodução por gênero
# Engajamento (likes, skips,play)
# usuários mais ativos
# Engajamento por artista

# ===================================
# CAMINHOS
# ===================================

SILVER_PATH = "data/silver"
GOLD_PATH = "data/gold"

os.makedirs(GOLD_PATH, exist_ok=True)

# ===================================
# CARREGAMENTO
# ===================================

events = pd.read_parquet(
    f"{SILVER_PATH}/events.parquet"
)

music = pd.read_parquet(
    f"{SILVER_PATH}/music.parquet"
)

users = pd.read_parquet(
    f"{SILVER_PATH}/users.parquet"
)

# ===================================
# JOIN PRINCIPAL
# ===================================

df = events.merge(
    music,
    on="music_id",
    how="left"
)

# ===================================
# TOP MÚSICAS
# ===================================

top_music = (
    df[df["action"] == "play"]
    .groupby(
        ["music_id", "title"],
        as_index=False
    )
    .size()
    .rename(
        columns={"size": "total_plays"}
    )
    .sort_values(
        "total_plays",
        ascending=False
    )
)

top_music.to_parquet(
    f"{GOLD_PATH}/top_music.parquet",
    index=False
)

# ===================================
# TOP ARTISTAS
# ===================================

top_artists = (
    df[df["action"] == "play"]
    .groupby(
        "artist",
        as_index=False
    )
    .size()
    .rename(
        columns={"size": "total_plays"}
    )
    .sort_values(
        "total_plays",
        ascending=False
    )
)

top_artists.to_parquet(
    f"{GOLD_PATH}/top_artists.parquet",
    index=False
)

# ===================================
# PLAYS POR GÊNERO
# ===================================

plays_by_genre = (
    df[df["action"] == "play"]
    .groupby(
        "genre",
        as_index=False
    )
    .size()
    .rename(
        columns={"size": "total_plays"}
    )
    .sort_values(
        "total_plays",
        ascending=False
    )
)

plays_by_genre.to_parquet(
    f"{GOLD_PATH}/plays_by_genre.parquet",
    index=False
)

# ===================================
# ENGAJAMENTO
# ===================================

engagement = (
    df.groupby(
        "action",
        as_index=False
    )
    .size()
    .rename(
        columns={"size": "total"}
    )
)

engagement.to_parquet(
    f"{GOLD_PATH}/engagement.parquet",
    index=False
)
# ===================================
# ENGAJAMENTO POR ARTISTA
# ===================================

engagement_artist = (
    df.pivot_table(
        index="artist",
        columns="action",
        aggfunc="size",
        fill_value=0
    )
    .reset_index()
)

# Garantir colunas mesmo se alguma ação não existir
for col in ["play", "like", "skip"]:
    if col not in engagement_artist.columns:
        engagement_artist[col] = 0

# Taxa de engajamento
engagement_artist["engagement_rate"] = (
    engagement_artist["like"] /
    engagement_artist["play"].replace(0, 1)
)

# Taxa de rejeição (skips)
engagement_artist["skip_rate"] = (
    engagement_artist["skip"] /
    engagement_artist["play"].replace(0, 1)
)

engagement_artist = engagement_artist.sort_values(
    "engagement_rate",
    ascending=False
)

engagement_artist.to_parquet(
    f"{GOLD_PATH}/engagement_artist.parquet",
    index=False
)

# ===================================
# USUÁRIOS MAIS ATIVOS
# ===================================

active_users = (
    df.groupby(
        "user_id",
        as_index=False
    )
    .size()
    .rename(
        columns={"size": "total_events"}
    )
    .sort_values(
        "total_events",
        ascending=False
    )
)

active_users.to_parquet(
    f"{GOLD_PATH}/active_users.parquet",
    index=False
)

# ===================================
# EVOLUÇÃO DIÁRIA
# ===================================

df["date"] = pd.to_datetime(
    df["timestamp"]
).dt.date

plays_by_day = (
    df[df["action"] == "play"]
    .groupby(
        "date",
        as_index=False
    )
    .size()
    .rename(
        columns={"size": "total_plays"}
    )
)

plays_by_day.to_parquet(
    f"{GOLD_PATH}/plays_by_day.parquet",
    index=False
)

print("Gold criada com sucesso!")
