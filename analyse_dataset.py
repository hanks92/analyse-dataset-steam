import pandas as pd

# 1️⃣ Charger le dataset
file_path = "steam_games.csv" 
df = pd.read_csv(file_path)

# 2️⃣ Afficher les 5 premières lignes pour un aperçu
print("🔹 Aperçu du dataset :")
print(df.head())

# 3️⃣ Vérifier la taille du dataset
print("\n🔹 Taille du dataset :")
print(f"Nombre de lignes: {df.shape[0]}, Nombre de colonnes: {df.shape[1]}")

# 4️⃣ Lister les colonnes et leurs types de données
print("\n🔹 Types des colonnes :")
print(df.dtypes)

# 5️⃣ Vérifier la présence de valeurs manquantes
print("\n🔹 Valeurs manquantes :")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])

# 6️⃣ Vérifier les valeurs uniques dans certaines colonnes clés
columns_to_check = ["genre", "developer", "publisher"]
for col in columns_to_check:
    if col in df.columns:
        print(f"\n🔹 Valeurs uniques dans {col}:")
        print(df[col].unique()[:10])  # Affiche les 10 premières valeurs uniques
