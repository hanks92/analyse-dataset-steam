import pandas as pd

def handle_missing_data(df):
    # Gérer les données manquantes
    df['original_price'].fillna(df['original_price'].median(), inplace=True)
    df['discount_price'].fillna(df['discount_price'].median(), inplace=True)

    # Gérer les données textuelles manquantes
    df['name'].fillna('Non spécifié', inplace=True)

    # Supprimer les colonnes avec plus de 70% de données manquantes
    df.dropna(thresh=int(0.7*len(df)), axis=1, inplace=True)

    # Supprimer les lignes avec trop de valeurs manquantes
    df.dropna(thresh=df.shape[1] - 2, axis=0, inplace=True)

    return df
