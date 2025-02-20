import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 📂 1️⃣ Créer un dossier pour stocker les images des graphiques
output_dir = "images_graphs"
os.makedirs(output_dir, exist_ok=True)

# 📥 2️⃣ Charger le dataset
file_path = "steam_games.csv"  # Mets ici le bon chemin
df = pd.read_csv(file_path)

# 📊 3️⃣ Évolution du Nombre de Jeux Publiés par Année
plt.figure(figsize=(12, 6))
sns.barplot(x=df['release_date'].value_counts().sort_index().index, 
            y=df['release_date'].value_counts().sort_index().values, 
            color='royalblue')
plt.xticks(rotation=45)
plt.xlabel("Année de sortie")
plt.ylabel("Nombre de jeux publiés")
plt.title("Évolution du Nombre de Jeux Publiés sur Steam par Année")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig(os.path.join(output_dir, "evolution_jeux_par_annee.png"), dpi=300, bbox_inches='tight')
plt.close()

# 🎮 4️⃣ Répartition des Genres les Plus Populaires
top_genres = df['genre'].value_counts().head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_genres.index, y=top_genres.values, hue=None, palette="viridis", legend=False)
plt.xlabel("Genres de jeux")
plt.ylabel("Nombre de jeux")
plt.title("Top 10 des Genres les Plus Représentés sur Steam")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig(os.path.join(output_dir, "top_genres.png"), dpi=300, bbox_inches='tight')
plt.close()

# 🏢 5️⃣ Éditeurs les Plus Productifs
top_publishers = df['publisher'].value_counts().head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_publishers.index, y=top_publishers.values, hue=None, palette="coolwarm", legend=False)
plt.xlabel("Éditeurs")
plt.ylabel("Nombre de jeux publiés")
plt.title("Top 10 des Éditeurs les Plus Productifs sur Steam")
plt.xticks(rotation=75)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig(os.path.join(output_dir, "top_publishers.png"), dpi=300, bbox_inches='tight')
plt.close()

# 💰 6️⃣ Distribution des Prix des Jeux
plt.figure(figsize=(12, 6))
sns.histplot(df['original_price'].dropna(), bins=50, kde=True, color='darkred')
plt.xlabel("Prix des jeux ($)")
plt.ylabel("Nombre de jeux")
plt.title("Répartition des Prix des Jeux sur Steam")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig(os.path.join(output_dir, "distribution_prix.png"), dpi=300, bbox_inches='tight')
plt.close()

# ⭐ 7️⃣ Répartition des Évaluations des Jeux
top_reviews = df['all_reviews'].value_counts()

plt.figure(figsize=(12, 6))
sns.barplot(x=top_reviews.index, y=top_reviews.values, hue=None, palette="Blues_r", legend=False)
plt.xlabel("Type d'évaluation")
plt.ylabel("Nombre de jeux")
plt.title("Répartition des Évaluations des Jeux sur Steam")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig(os.path.join(output_dir, "distribution_reviews.png"), dpi=300, bbox_inches='tight')
plt.close()

print(f"✅ Tous les graphiques ont été enregistrés dans le dossier '{output_dir}'")
