import subprocess
import logging
import time
import sys # Import sys to get the correct Python executable

# Orquestrador

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

pipeline = [

    "generate_users.py",
    "generate_musics.py",
    "generate_streaming.py",
    "ingest_batch.py",
    "ingest_streaming.py",
    "transform_silver.py",
    "transform_gold.py",
    "gera_csv.py"
]

for etapa in pipeline:

    logging.info(
        f"Iniciando {etapa}"
    )

    inicio = time.time()

    resultado = subprocess.run(
        [sys.executable, f"scripts/{etapa}"]
    )

    fim = time.time()

    if resultado.returncode != 0:

        logging.error(
            f"Falha em {etapa}"
        )

        raise Exception(
            f"Erro em {etapa}"
        )

    logging.info(
        f"{etapa} concluído em {fim-inicio:.2f}s"
    )

logging.info(
    "Pipeline concluído com sucesso"
)
