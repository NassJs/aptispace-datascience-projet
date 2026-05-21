import os, sys
sys.path.append('/home/aptitek/Documents/Aptispace/datascience/lab/projet')

# Installation automatique des dépendances requises dans le noyau Jupyter actuel
# %pip install -r ../requirements.txt


import os
import sys
import pandas as pd
import numpy as np

sys.path.append(os.path.abspath('..'))
from src import data_clean as dc

print("Librairies importées pour l'EDA !")


df = pd.read_csv('../data/processed/ai_student_cleaned.csv')

# Pas de colonne temporelle dans ce dataset : on saute pd.to_datetime().
print(f"Dimensions : {df.shape}")
df.head()


# Résumé statistique global des variables numériques
print("=== Statistiques descriptives globales ===")
print(df.describe().round(2))

# Agrégation par filière : moyenne du GPA, heures GenAI, rétention
print("\n=== Profil moyen par filière (Major_Category) ===")
by_major = df.groupby("Major_Category")[[
    "Pre_Semester_GPA", "Post_Semester_GPA",
    "Weekly_GenAI_Hours", "Traditional_Study_Hours",
    "Skill_Retention_Score", "Anxiety_Level_During_Exams",
]].mean().round(2)
print(by_major)

# Agrégation par politique institutionnelle : impact sur le GPA et l'anxiété
print("\n=== Effet de la politique institutionnelle ===")
by_policy = df.groupby("Institutional_Policy").agg(
    n_students=("Student_ID", "count"),
    gpa_post_mean=("Post_Semester_GPA", "mean"),
    genai_hours_mean=("Weekly_GenAI_Hours", "mean"),
    anxiety_mean=("Anxiety_Level_During_Exams", "mean"),
    burnout_high_rate=("Burnout_Risk_Level", lambda s: (s == "High").mean()),
).round(3)
print(by_policy)


# Application de la feature_engineering définie dans src/data_clean.py
df_feat = dc.feature_engineering(df)

# Colonnes ajoutées par la fonction
new_cols = [c for c in df_feat.columns if c not in df.columns]
print("Variables dérivées créées :", new_cols)
print(df_feat[new_cols + ["Pre_Semester_GPA", "Weekly_GenAI_Hours"]].head())


# Matrice de corrélation de Pearson sur les variables numériques clés
cols = [
    "Pre_Semester_GPA", "Post_Semester_GPA", "GPA_Squared",
    "Weekly_GenAI_Hours", "AI_Usage_Level",
    "Traditional_Study_Hours", "Tool_Diversity",
    "Perceived_AI_Dependency", "Anxiety_Level_During_Exams",
    "Skill_Retention_Score",
]
correlations = df_feat[cols].corr(method="pearson").round(2)
print("=== Matrice de corrélation de Pearson ===")
print(correlations)

# Top 5 corrélations les plus fortes avec la cible Post_Semester_GPA
print("\n=== Top corrélations avec Post_Semester_GPA ===")
target_corr = correlations["Post_Semester_GPA"].drop("Post_Semester_GPA").abs().sort_values(ascending=False)
print(target_corr.head(5))

