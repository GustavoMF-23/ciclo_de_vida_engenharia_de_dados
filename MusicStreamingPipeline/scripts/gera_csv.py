
import pandas as pd

# Gera arquivos no formato .csv na camada Gold

arquivos = [
    "top_music",
    "top_artists",
    "plays_by_genre",
    "engagement",
    "engagement_artist",
    "active_users",
    "plays_by_day"
]

for arquivo in arquivos:

    df = pd.read_parquet(
        f"data/gold/{arquivo}.parquet"
    )

    df.to_csv(
        f"data/gold/{arquivo}.csv",
        index=False
    )
