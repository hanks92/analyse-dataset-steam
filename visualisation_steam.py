import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Créer un dossier pour stocker les images des graphiques
output_dir = "images_graphs"
os.makedirs(output_dir, exist_ok=True)

# Charger le dataset
file_path = "steam_games.csv"  # Mets ici le bon chemin
df = pd.read_csv(file_path)

# Évolution du Nombre de Jeux Publiés par Année
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
df_clean = df.dropna(subset=['release_date'])
df_clean.loc[:, 'release_year'] = df_clean['release_date'].dt.year
df_clean = df_clean[(df_clean['release_year'] >= 1990) & (df_clean['release_year'] <= 2025)]
games_per_year = df_clean['release_year'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x=games_per_year.index, y=games_per_year.values, marker='o', color="royalblue", linewidth=2)
plt.xticks(rotation=45)
plt.xlabel("Année de sortie")
plt.ylabel("Nombre de jeux publiés")
plt.title("Évolution du Nombre de Jeux Publiés sur Steam (1990 - 2025)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig(os.path.join(output_dir, "evolution_jeux_par_annee.png"), dpi=300, bbox_inches='tight')
plt.close()

# Répartition des Genres les Plus Populaires
df_clean['genre'] = df_clean['genre'].dropna()
all_genres = df_clean['genre'].str.split(',').explode()
top_genres = all_genres.value_counts().head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_genres.index, y=top_genres.values, hue=None, palette="viridis", legend=False)
plt.xlabel("Genres de jeux")
plt.ylabel("Nombre de jeux")
plt.title("Top 10 des Genres les Plus Représentés sur Steam")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig(os.path.join(output_dir, "top_genres.png"), dpi=300, bbox_inches='tight')
plt.close()

# Les Éditeurs les Plus Productifs
top_publishers = df_clean['publisher'].value_counts().head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_publishers.index, y=top_publishers.values, hue=None, palette="coolwarm", legend=False)
plt.xlabel("Éditeurs")
plt.ylabel("Nombre de jeux publiés")
plt.title("Top 10 des Éditeurs les Plus Productifs sur Steam")
plt.xticks(rotation=75)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig(os.path.join(output_dir, "top_publishers.png"), dpi=300, bbox_inches='tight')
plt.close()

# Distribution des Prix des Jeux (SANS LES CARRÉS ROUGES)
df_clean['original_price'] = df_clean['original_price'].replace(['Free', 'Free to Play'], '0')
df_clean['original_price'] = df_clean['original_price'].str.replace('[\$,]', '', regex=True)
df_clean['original_price'] = pd.to_numeric(df_clean['original_price'], errors='coerce')

plt.figure(figsize=(12, 6))
sns.kdeplot(df_clean['original_price'].dropna(), fill=True, color='darkred')  # Seulement la courbe KDE
plt.xlim(0, df_clean['original_price'].dropna().quantile(0.95))  # Exclure les valeurs extrêmes
plt.xlabel("Prix des jeux ($)")
plt.ylabel("Densité")
plt.title("Distribution des Prix des Jeux sur Steam")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig(os.path.join(output_dir, "distribution_prix.png"), dpi=300, bbox_inches='tight')
plt.close()

# Répartition des Évaluations des Jeux
df_clean['all_reviews'] = df_clean['all_reviews'].dropna().str.split(',').str[0]
top_reviews = df_clean['all_reviews'].value_counts()

plt.figure(figsize=(12, 6))
sns.barplot(x=top_reviews.index, y=top_reviews.values, hue=None, palette="Blues_r", legend=False)
plt.xlabel("Type d'évaluation")
plt.ylabel("Nombre de jeux")
plt.title("Répartition des Évaluations des Jeux sur Steam")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig(os.path.join(output_dir, "distribution_reviews.png"), dpi=300, bbox_inches='tight')
plt.close()

print(f"✅ Tous les graphiques améliorés ont été enregistrés dans '{output_dir}'")
