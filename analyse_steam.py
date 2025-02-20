import pandas as pd
import matplotlib.pyplot as plt
from preprocess_text import clean_text
from handle_missing_data import handle_missing_data

# Charger le fichier CSV
df = pd.read_csv("data/steam_games.csv", encoding='utf-8')

# Afficher les 5 premières lignes
print("📌 Aperçu des premières lignes du dataset :")
print(df.head())

# Pré-traitement des champs textuels (nettoyage des colonnes texte)
df = clean_text(df)

# Gestion des données manquantes
df = handle_missing_data(df)

# Afficher un aperçu après nettoyage
print("\n📌 Aperçu après nettoyage des données :")
print(df.head())

# Synthèse des statistiques descriptives (moyenne, médiane, min, max)
print("\n📊 Statistiques descriptives des données numériques :")
print(df.describe())

# Visualisation de la distribution des genres de jeux
genre_counts = df['genre'].value_counts()
genre_counts.plot(kind='bar', color='skyblue')
plt.title('Distribution des genres de jeux')
plt.xlabel('Genre')
plt.ylabel('Nombre de jeux')
plt.show()
