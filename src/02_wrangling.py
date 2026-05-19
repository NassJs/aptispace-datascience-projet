import os
import sys
import pandas as pd
import numpy as np

# Ajout du dossier parent pour importer 'src'
sys.path.append(os.path.abspath('..'))
from src import data_clean as dc

# Configuration de l'affichage pandas pour une meilleure lisibilité
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

print(f"Librairies prêtes pour le Wrangling ! (pandas {pd.__version__}, numpy {np.__version__})")

# ---------------------------------------------------------------------------
# 1. Chargement du dataset enrichi issu de l'étape 01_acquisition
# ---------------------------------------------------------------------------
raw_data_path = '../data/raw/ai_student_enriched.csv'
if not os.path.exists(raw_data_path):
    # Fallback sur le brut non enrichi si l'étape 01 n'a pas été exécutée
    raw_data_path = '../data/raw/ai_student_.csv'
df_raw = dc.load_raw_data(raw_data_path)

# ---------------------------------------------------------------------------
# 2. Audit rapide : structure, valeurs manquantes, doublons
# ---------------------------------------------------------------------------
print("\n--- Audit du dataset ---")
df_raw.info()
print("\nValeurs manquantes par colonne :")
print(df_raw.isnull().sum())
print(f"\nDoublons : {df_raw.duplicated().sum()}")

# ---------------------------------------------------------------------------
# 3. Nettoyage des dates : non applicable
#    Le dataset ai_student_ ne contient aucune colonne temporelle.
# ---------------------------------------------------------------------------
df_clean = df_raw.copy()
print("\nAucune colonne temporelle à convertir — étape clean_dates ignorée.")

# ---------------------------------------------------------------------------
# 4. Traitement des outliers sur les colonnes numériques clés
#    - GPA (Pre / Post) : intervalle plausible [0.0, 4.0]
#    - Skill_Retention_Score : intervalle plausible [0.0, 100.0]
#    - Weekly_GenAI_Hours : intervalle plausible [0.0, 60.0]
# ---------------------------------------------------------------------------
df_no_outliers = dc.handle_outliers(df_clean, ['Pre_Semester_GPA', 'Post_Semester_GPA'], 0.0, 4.0)
df_no_outliers = dc.handle_outliers(df_no_outliers, ['Skill_Retention_Score'], 0.0, 100.0)
df_no_outliers = dc.handle_outliers(df_no_outliers, ['Weekly_GenAI_Hours'], 0.0, 60.0)

print("\n--- Résumé statistique après traitement des outliers ---")
print(df_no_outliers[['Pre_Semester_GPA', 'Post_Semester_GPA',
                      'Skill_Retention_Score', 'Weekly_GenAI_Hours']].describe())

# ---------------------------------------------------------------------------
# 5. Imputation des valeurs manquantes éventuellement créées par handle_outliers
# ---------------------------------------------------------------------------
cols_to_impute = ['Pre_Semester_GPA', 'Post_Semester_GPA',
                  'Skill_Retention_Score', 'Weekly_GenAI_Hours']
df_final = dc.impute_missing_values(df_no_outliers, cols_to_impute, 'median')

print("\nValeurs manquantes restantes après imputation :")
print(df_final.isnull().sum().sum(), "au total.")

# ---------------------------------------------------------------------------
# 6. Sauvegarde du dataset nettoyé
# ---------------------------------------------------------------------------
os.makedirs('../data/processed', exist_ok=True)
processed_path = '../data/processed/ai_student_cleaned.csv'
df_final.to_csv(processed_path, index=False)
print(f"\nDonnées propres sauvegardées dans : {processed_path}")
print(f"Dimensions finales : {df_final.shape}")
