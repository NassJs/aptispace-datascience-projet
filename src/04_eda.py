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
print(df.describe())

# Agrégation par filière : moyenne du GPA post-semestre et heures GenAI hebdo
print(df.groupby("Major_Category")[["Post_Semester_GPA", "Weekly_GenAI_Hours", "Skill_Retention_Score"]].mean().round(2))


# Variable dérivée 1 : delta de GPA entre avant et après le semestre
df_feat = df.copy()
df_feat["GPA_delta"] = df_feat["Post_Semester_GPA"] - df_feat["Pre_Semester_GPA"]

# Variable dérivée 2 : intensité d'usage de l'IA (catégorielle)
df_feat["GenAI_intensity"] = pd.cut(
    df_feat["Weekly_GenAI_Hours"],
    bins=[-0.01, 5, 15, 60],
    labels=["Low", "Medium", "High"],
)

# Variable dérivée 3 : ratio temps d'étude traditionnel / temps IA
df_feat["Study_vs_AI_ratio"] = df_feat["Traditional_Study_Hours"] / (df_feat["Weekly_GenAI_Hours"] + 1)

print(df_feat[["GPA_delta", "GenAI_intensity", "Study_vs_AI_ratio"]].head())


# Corrélations de Pearson sur les variables numériques d'intérêt
cols_interet = [
    "Pre_Semester_GPA", "Post_Semester_GPA", "GPA_delta",
    "Weekly_GenAI_Hours", "Traditional_Study_Hours", "Study_vs_AI_ratio",
    "Skill_Retention_Score", "Anxiety_Level_During_Exams",
]
correlations = df_feat[cols_interet].corr()
print("Matrice de corrélation de Pearson :")
print(correlations.round(2))

