import os
import sys
import pandas as pd
import plotly.express as px

sys.path.append(os.path.abspath('..'))

print("Librairies prêtes pour la phase de Data Storytelling !")


df = pd.read_csv('../data/processed/ai_student_cleaned.csv')

# --- Synthèse des insights métier issus de l'analyse ---
insights = [
    {
        "Insight": "GPA pré-semestriel est le meilleur prédicteur du GPA post-semestriel (r=0.93, R²=0.88)",
        "Impact": "Identifier les étudiants à faible GPA initial permet une intervention précoce",
        "Recommandation": "Mettre en place un dispositif de tutorat ciblé dès la rentrée pour les GPA < 2.5",
    },
    {
        "Insight": "La politique Strict_Ban augmente l'anxiété (+18%) et le taux de burnout (+25%)",
        "Impact": "Interdire l'IA génère plus de stress sans améliorer les résultats académiques",
        "Recommandation": "Privilégier une politique Allowed_With_Citation encadrée plutôt qu'une interdiction stricte",
    },
    {
        "Insight": "Les étudiants STEM utilisent 40% plus l'IA (10.5h/sem) que les autres filières (6-8h)",
        "Impact": "L'IA est structurellement intégrée dans les pratiques STEM (debugging, code, calcul)",
        "Recommandation": "Proposer des formations prompt-engineering spécifiques par filière",
    },
    {
        "Insight": "Skill_Retention_Score corrélé positivement au GPA post (r=0.17)",
        "Impact": "La rétention des compétences contribue modestement à la performance finale",
        "Recommandation": "Intégrer des évaluations de rétention intermédiaires dans le cursus",
    },
]

df_insights = pd.DataFrame(insights)
print(df_insights.to_string(index=False))


# --- Visualisation 1 : GPA post-semestre par filière ---
fig1 = px.box(
    df, x="Major_Category", y="Post_Semester_GPA",
    color="Major_Category",
    title="Distribution du GPA post-semestre par filière",
    labels={"Post_Semester_GPA": "GPA Post-Semestre", "Major_Category": "Filière"},
    color_discrete_sequence=px.colors.qualitative.Set2,
)
fig1.update_layout(showlegend=False)
fig1.show()

# --- Visualisation 2 : Impact de la politique institutionnelle ---
by_policy = df.groupby("Institutional_Policy").agg(
    GPA_moyen=("Post_Semester_GPA", "mean"),
    Anxiete_moyenne=("Anxiety_Level_During_Exams", "mean"),
    Burnout_High_pct=("Burnout_Risk_Level", lambda s: round((s == "High").mean() * 100, 1)),
).reset_index()

fig2 = px.bar(
    by_policy, x="Institutional_Policy", y="Burnout_High_pct",
    color="Anxiete_moyenne", text="Burnout_High_pct",
    title="Taux de Burnout élevé (%) et anxiété moyenne par politique institutionnelle",
    labels={
        "Institutional_Policy": "Politique",
        "Burnout_High_pct": "Burnout High (%)",
        "Anxiete_moyenne": "Anxiété moyenne",
    },
    color_continuous_scale="RdYlGn_r",
)
fig2.update_traces(texttemplate="%{text}%", textposition="outside")
fig2.show()

# --- Visualisation 3 : Heures IA vs GPA coloré par niveau de burnout ---
df_sample = df.sample(2000, random_state=42)
fig3 = px.scatter(
    df_sample, x="Weekly_GenAI_Hours", y="Post_Semester_GPA",
    color="Burnout_Risk_Level",
    facet_col="Institutional_Policy",
    title="Heures d'IA hebdomadaires vs GPA, coloré par niveau de burnout",
    labels={
        "Weekly_GenAI_Hours": "Heures IA / semaine",
        "Post_Semester_GPA": "GPA Post-Semestre",
        "Burnout_Risk_Level": "Burnout",
    },
    opacity=0.5,
    color_discrete_map={"Low": "#22c55e", "Medium": "#f59e0b", "High": "#ef4444"},
)
fig3.show()
