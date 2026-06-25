import os

# Carrega dados de streaming na camada bronze

SOURCE_FILE = "data/raw/events.jsonl"
DESTINATION_FILE = "data/bronze/streaming/events.jsonl"

os.makedirs(
    os.path.dirname(DESTINATION_FILE),
    exist_ok=True
)

with open(SOURCE_FILE, "r", encoding="utf-8") as source:
    with open(DESTINATION_FILE, "a", encoding="utf-8") as destination:

        for line in source:
            destination.write(line)

print("✓ Eventos adicionados à camada Bronze")
