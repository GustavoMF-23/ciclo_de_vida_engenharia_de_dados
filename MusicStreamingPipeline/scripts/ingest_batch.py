
import os
import pandas as pd
import sys # Import sys for explicit exit codes

# Carga dos dados de usuários e músicas - Ingest_batch.py
# Copia da camada Raw para a camada bronze

# ============================
# Caminhos
# ============================

RAW_PATH = "data/raw"
BRONZE_PATH = "data/bronze/batch"

# Cria a pasta Bronze caso não exista
os.makedirs(BRONZE_PATH, exist_ok=True)

# ============================
# Ingestão de usuários
# ============================

# Corrigindo a construção do caminho para ser mais robusta
users_path = os.path.join(RAW_PATH, "users.csv")

if os.path.exists(users_path):
    try:
        users_df = pd.read_csv(users_path)

        users_df.to_parquet(
            os.path.join(BRONZE_PATH, "users_bronze.parquet"),
            index=False
        )

        print(f"✓ Usuários carregados: {len(users_df)} registros")
    except Exception as e:
        print(f"Erro ao processar users.csv: {e}")
        sys.exit(1) # Força a saída com erro se houver problema no processamento
else:
    print(f"⚠ users.csv não encontrado em {users_path}.")
    sys.exit(1) # Força a saída com erro se o arquivo não for encontrado

# ============================
# Ingestão de músicas
# ============================

# Corrigindo a construção do caminho para ser mais robusta
music_path = os.path.join(RAW_PATH, "music.csv")

if os.path.exists(music_path):
    try:
        music_df = pd.read_csv(music_path)

        music_df.to_parquet(
            os.path.join(BRONZE_PATH, "music_bronze.parquet"),
            index=False
        )

        print(f"✓ Músicas carregadas: {len(music_df)} registros")
    except Exception as e:
        print(f"Erro ao processar music.csv: {e}")
        sys.exit(1) # Força a saída com erro se houver problema no processamento
else:
    print(f"⚠ music.csv não encontrado em {music_path}.")
    sys.exit(1) # Força a saída com erro se o arquivo não for encontrado

print("\nIngestão batch concluída com sucesso!")
