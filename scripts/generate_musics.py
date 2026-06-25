import os
import pandas as pd

# Carrega o dataset de músicas original obtido no Kaggle e seleciona as colunas
# track_id, track_name, track_artist, track_album_name, playlist_genre,
# track_album_release_date e duration_ms

musicas = pd.read_csv("data/spotify_songs.csv")
total_antes = len(musicas)


# Seleciona e renomeia as colunas desejadas
music = musicas[
    [
        "track_id",
        "track_name",
        "track_artist",
        "track_album_name",
        "playlist_genre",
        "track_album_release_date",
        "duration_ms",
    ]
].rename(
    columns={
        "track_id": "music_id",
        "track_name": "title",
        "track_artist": "artist",
        "track_album_name": "album",
        "playlist_genre": "genre",
        "track_album_release_date": "release_date",
    }
)

# Remove possíveis duplicatas
music = music.drop_duplicates(subset=["music_id"])

# Salva o resultado
# music.to_csv("music.csv", index=False)
os.makedirs("data/raw", exist_ok=True)

pd.DataFrame(music).to_csv(
    "data/raw/music.csv",
    index=False
)

total_depois = len(music)
print(f"Total de músicas antes: {total_antes}")
print(f"Total de músicas após remoção de duplicatas: {total_depois}")
# print(f"Duplicatas removidas: {total_antes - total_depois}")
