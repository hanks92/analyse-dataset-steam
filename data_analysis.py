import pandas as pd

# Charger les données
df = pd.read_csv('data/jeux_video.csv')

# Traitement des champs texte
df['name'] = df['name'].str.lower().str.strip()
df['developer'] = df['developer'].fillna('Non spécifié')
df['publisher'] = df['publisher'].fillna('Non spécifié')

# Gestion des données manquantes
df['price'] = df['price'].replace('Free', '0').apply(lambda x: float(x.replace('$', '').replace(',', '').strip()) if isinstance(x, str) else x)

# Calcul des évaluations moyennes
df['average_reviews'] = df['recent_reviews'].apply(lambda x: float(x.split('%')[0]) if isinstance(x, str) else None)

# Analyse des tendances
best_reviewed_games = df[['name', 'average_reviews']].dropna().sort_values(by='average_reviews', ascending=False).head(10)

# Sauvegarder les résultats pour utilisation dans le rapport ou la visualisation
best_reviewed_games.to_csv('results/best_reviewed_games.csv', index=False)
