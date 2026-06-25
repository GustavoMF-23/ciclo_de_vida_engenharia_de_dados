from faker import Faker
import pandas as pd
import random
import os

# Gera arquivo de usuários, a partir da função faker

fake = Faker("pt_BR")
planos = ["Free", "Premium", "Family"]

dados = []

for user_id in range(1, 10001):
    dados.append({
        "user_id": user_id,
        "nome": fake.name(),
        "email": fake.email(),
        "idade": random.randint(18, 70),
        "pais": fake.country(),
        "tipo_plano": random.choice(planos)
    })

os.makedirs("data/raw", exist_ok=True)

pd.DataFrame(dados).to_csv(
    "data/raw/users.csv",
    index=False
)
print(f"10.000 usuários eventos gerados com sucesso em user.csv")
