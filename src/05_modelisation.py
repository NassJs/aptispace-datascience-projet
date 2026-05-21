import os
import sys
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor
import tensorflow as tf
from tensorflow.keras import layers, models

sys.path.append(os.path.abspath('..'))
from src import data_clean as dc

print("Librairies de modélisation importées avec succès !")
print("Version TensorFlow :", tf.__version__)


# Chargement des données nettoyées et feature engineering
df = pd.read_csv('../data/processed/ai_student_cleaned.csv')
df_feat = dc.feature_engineering(df)
print(f"Dimensions : {df_feat.shape}")

# Cible : GPA post-semestre (régression supervisée)
target = "Post_Semester_GPA"

features = [
    "Pre_Semester_GPA",
    "Weekly_GenAI_Hours",
    "Traditional_Study_Hours",
    "Tool_Diversity",
    "Perceived_AI_Dependency",
    "Anxiety_Level_During_Exams",
    "Skill_Retention_Score",
    "Secteur_IA_Adoption_Rate",
    "Avg_Salary_Index",
    "Recommended_Study_Hours_Week",
    "AI_Usage_Level",
    "GPA_Squared",
]

from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error, r2_score

X = df_feat[features]
y = df_feat[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Train : {X_train.shape[0]} lignes | Test : {X_test.shape[0]} lignes")

# Entraînement du RandomForest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
rf_model.fit(X_train, y_train)

# Évaluation
y_pred = rf_model.predict(X_test)
print(f"\nRMSE test : {root_mean_squared_error(y_test, y_pred):.4f}")
print(f"R²   test : {r2_score(y_test, y_pred):.4f}")

# Importance des variables
importances = pd.Series(rf_model.feature_importances_, index=features).sort_values(ascending=False)
print("\nImportance des variables :")
print(importances.round(3))


# Génération fictive d'un jeu d'images simples (64x64 pixels) de cercles (Classe 0) vs rectangles (Classe 1)
def generate_dummy_images(num_samples=100):
    images = np.zeros((num_samples, 64, 64, 3), dtype=np.float32)
    labels = np.zeros(num_samples, dtype=np.int32)
    for i in range(num_samples):
        label = np.random.choice([0, 1])
        labels[i] = label
        images[i, :, :, :] = 0.2 + np.random.normal(0, 0.01, (64, 64, 3))
        if label == 1:
            images[i, 10:30, 10:30, 0] = 0.8
        else:
            images[i, 20:40, 20:40, 1] = 0.8
    return images, labels

X_images, y_labels = generate_dummy_images(100)
split = int(0.8 * len(X_images))
X_img_train = X_images[:split]
y_img_train = y_labels[:split]

print(f"Dataset d'images brutes généré. Dimensions Train : {X_img_train.shape}")


# Architecture CNN
cnn_model = models.Sequential([
    layers.Conv2D(16, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(16, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

cnn_model.summary()


# Entraînement CNN
cnn_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
cnn_model.fit(X_img_train, y_img_train, epochs=2, batch_size=32, verbose=1)
print("CNN entraîné avec succès !")
