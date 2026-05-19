import os, sys
sys.path.append('/home/aptitek/Documents/Aptispace/datascience/lab/projet')

# Installation automatique des dépendances requises dans le noyau Jupyter actuel
# %pip install -r ../requirements.txt


import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sys.path.append(os.path.abspath('..'))
from src import data_clean as dc
from src import utils_viz as uv

# Activation du style premium personnalisé (light ou dark)
uv.set_custom_style(theme='light')
# %matplotlib inline
print("Librairies de visualisation prêtes !")


df = pd.read_csv('../data/processed/ai_student_cleaned.csv')

# Le dataset "ai_student_cleaned" ne contient pas de colonne temporelle :
# on saute donc l'étape pd.to_datetime() et dc.feature_engineering().
print(f"Dimensions : {df.shape}")
df.head()


# A. Distribution univariée d'une variable clé : GPA post-semestre
uv.plot_histogram(df, "Post_Semester_GPA")


# B. Carte de chaleur des corrélations sur l'ensemble des colonnes numériques
uv.plot_correlation_matrix(df)


# C. Comparaison bivariée : GPA post-semestre selon la filière
uv.plot_boxplot(df, x="Major_Category", y="Post_Semester_GPA")

