import numpy as np
import pandas as pd


def load_raw_data(path):
    """
    Charge un fichier CSV et retourne un DataFrame.
    """
    df = pd.read_csv(path)
    return df


def clean_dates(df, column_name):
    """
    Convertit une colonne en format date.
    Si une date est invalide, elle devient NaT.
    """
    df_copy = df.copy()

    if column_name in df_copy.columns:
        df_copy[column_name] = pd.to_datetime(
            df_copy[column_name],
            errors="coerce"
        )

    return df_copy


def handle_outliers(df, columns, min_value, max_value):
    """
    Remplace les valeurs aberrantes par NaN.

    Exemple :
    si une valeur est < min_value ou > max_value,
    elle devient NaN.
    """
    df_copy = df.copy()

    for col in columns:
        if col in df_copy.columns:
            df_copy.loc[
                (df_copy[col] < min_value) | (df_copy[col] > max_value),
                col
            ] = np.nan

    return df_copy


def impute_missing_values(df, columns, method="median"):
    """
    Remplace les valeurs manquantes.

    Méthodes possibles :
    - median
    - mean
    - mode
    - interpolate
    """
    df_copy = df.copy()

    for col in columns:
        if col in df_copy.columns:

            if method == "median":
                df_copy[col] = df_copy[col].fillna(df_copy[col].median())

            elif method == "mean":
                df_copy[col] = df_copy[col].fillna(df_copy[col].mean())

            elif method == "mode":
                df_copy[col] = df_copy[col].fillna(df_copy[col].mode()[0])

            elif method == "interpolate":
                df_copy[col] = df_copy[col].interpolate()

            else:
                df_copy[col] = df_copy[col].fillna(df_copy[col].median())

    return df_copy


def save_clean_data(df, path):
    """
    Sauvegarde le DataFrame nettoyé en CSV.
    """
    df.to_csv(path, index=False)
    return path

def feature_engineering(df):
    """
    Crée quelques variables dérivées simples.
    """

    df_copy = df.copy()

    # Exemple : moyenne de stress et d'heures IA
    if 'Weekly_GenAI_Hours' in df_copy.columns:
        df_copy['AI_Usage_Level'] = pd.cut(
            df_copy['Weekly_GenAI_Hours'],
            bins=[0, 5, 15, 100],
            labels=['Faible', 'Moyen', 'Élevé']
        )

    return df_copy