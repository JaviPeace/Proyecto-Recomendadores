
import pandas as pd
import random
from collections import Counter

# Simulación de jugadores
players = pd.DataFrame({
    'PLAYER': [f'Player_{{i}}' for i in range(1, 31)],
    'TEAM': random.choices(['Team_A', 'Team_B', 'Team_C'], k=30),
    'NAT': random.choices(['ARG', 'BRA', 'FRA', 'GER', 'ESP'], k=30),
    'AGE': random.choices(range(18, 35), k=30),
    'POS': random.choices(['ST', 'CM', 'GK', 'DEF'], k=30),
    'RANK': list(range(1, 31))
})

# Modelo 1: Random
def recommend_random(df, k=5):
    return df.sample(n=k)

# Modelo 2: Most Popular (por frecuencia de aparición en un equipo)
def recommend_most_popular(df, k=5):
    team_counts = df['TEAM'].value_counts()
    top_team = team_counts.idxmax()
    return df[df['TEAM'] == top_team].head(k)

# Modelo 3: Diversidad basada en nacionalidad y edad (modelo simplificado)
def recommend_diverse(df, k=5):
    df = df.copy()
    df['score'] = df.apply(lambda row: row['AGE'] / 100 + len(set(df['NAT'])) / len(df), axis=1)
    return df.sort_values(by='score', ascending=False).head(k)

# Aplicar modelos
rec_random = recommend_random(players)
rec_popular = recommend_most_popular(players)
rec_diverse = recommend_diverse(players)

# Mostrar resultados
print("Random:\n", rec_random[['PLAYER', 'TEAM', 'NAT', 'AGE']])
print("\nMost Popular:\n", rec_popular[['PLAYER', 'TEAM', 'NAT', 'AGE']])
print("\nDiversity-Oriented:\n", rec_diverse[['PLAYER', 'TEAM', 'NAT', 'AGE']])
