import os
import sys
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.metrics import (
    root_mean_squared_error, mean_absolute_error, r2_score,
    accuracy_score, f1_score, classification_report,
)
from sklearn.preprocessing import LabelEncoder

sys.path.append(os.path.abspath('..'))
from src import data_clean as dc

print("Librairies prêtes pour l'évaluation des modèles !")


# --- Chargement et préparation ---
df = pd.read_csv('../data/processed/ai_student_cleaned.csv')
df_feat = dc.feature_engineering(df)

features = [
    "Pre_Semester_GPA", "Weekly_GenAI_Hours", "Traditional_Study_Hours",
    "Tool_Diversity", "Perceived_AI_Dependency", "Anxiety_Level_During_Exams",
    "Skill_Retention_Score", "Secteur_IA_Adoption_Rate",
    "Avg_Salary_Index", "Recommended_Study_Hours_Week",
    "AI_Usage_Level", "GPA_Squared",
]

# --- A. Évaluation Régression : prédire Post_Semester_GPA ---
X = df_feat[features]
y_reg = df_feat["Post_Semester_GPA"]
X_train, X_test, y_train, y_test = train_test_split(X, y_reg, test_size=0.2, random_state=42)

rf_reg = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
rf_reg.fit(X_train, y_train)
y_pred = rf_reg.predict(X_test)

print("=== Régression : Post_Semester_GPA ===")
print(f"MAE  : {mean_absolute_error(y_test, y_pred):.4f}")
print(f"RMSE : {root_mean_squared_error(y_test, y_pred):.4f}")
print(f"R²   : {r2_score(y_test, y_pred):.4f}")

# --- B. Évaluation Classification : prédire Burnout_Risk_Level ---
le = LabelEncoder()
y_clf = le.fit_transform(df_feat["Burnout_Risk_Level"])
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X, y_clf, test_size=0.2, random_state=42)

rf_clf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf_clf.fit(X_train_c, y_train_c)
y_pred_c = rf_clf.predict(X_test_c)

print("\n=== Classification : Burnout_Risk_Level ===")
print(f"Accuracy : {accuracy_score(y_test_c, y_pred_c):.4f}")
print(f"F1-macro : {f1_score(y_test_c, y_pred_c, average='macro'):.4f}")
print("\nRapport détaillé :")
print(classification_report(y_test_c, y_pred_c, target_names=le.classes_))


# --- Validation croisée K-Fold (k=5) sur la régression ---
# Pas de structure temporelle dans ce dataset : KFold classique est adapté.
kf = KFold(n_splits=5, shuffle=True, random_state=42)
rf_cv = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)

rmse_scores = -cross_val_score(
    rf_cv, X, y_reg,
    cv=kf,
    scoring="neg_root_mean_squared_error",
    n_jobs=-1,
)
r2_scores = cross_val_score(
    rf_cv, X, y_reg,
    cv=kf,
    scoring="r2",
    n_jobs=-1,
)

print("=== K-Fold (k=5) — Régression Post_Semester_GPA ===")
for i, (r, r2) in enumerate(zip(rmse_scores, r2_scores), 1):
    print(f"  Fold {i} → RMSE={r:.4f}  R²={r2:.4f}")
print(f"\n  Moyenne RMSE : {rmse_scores.mean():.4f} ± {rmse_scores.std():.4f}")
print(f"  Moyenne R²   : {r2_scores.mean():.4f} ± {r2_scores.std():.4f}")
