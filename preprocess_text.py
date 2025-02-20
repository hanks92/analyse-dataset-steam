import pandas as pd

def clean_text(df):
    # Nettoyage des colonnes textuelles
    df['name'] = df['name'].str.strip().str.lower()
    df['developer'] = df['developer'].str.strip().str.lower()
    df['publisher'] = df['publisher'].str.strip().str.lower()
    df['desc_snippet'] = df['desc_snippet'].str.strip().str.lower()

    # Remplir les valeurs manquantes par 'Non spécifié'
    df['developer'].fillna('Non spécifié', inplace=True)
    df['publisher'].fillna('Non spécifié', inplace=True)
    df['desc_snippet'].fillna('Non spécifié', inplace=True)

    # Tokenisation des tags populaires (si applicable)
    df['popular_tags'] = df['popular_tags'].apply(lambda x: x.split(',') if isinstance(x, str) else [])

    return df
