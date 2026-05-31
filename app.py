import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="AI et les etudiants",
    page_icon="🧠",
    layout="wide"
)

df = pd.read_csv("data/raw/ai_student_.csv")

# Style
st.markdown("""
<style>
.main {
    background-color: #f3f4f6;
}
.block-container {
    padding-top: 2rem;
}
h1, h2, h3, p, div {
    color: #000000;
}
.metric-card {
    background: linear-gradient(135deg, #e5e7eb, #d1d5db);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #9ca3af;
    box-shadow: 0px 4px 18px rgba(0,0,0,0.15);
}
.insight {
    background-color: #e5e7eb;
    padding: 18px;
    border-radius: 16px;
    border-left: 5px solid #38bdf8;
}
.warning-box {
    background-color: #e5e7eb;
    padding: 18px;
    border-radius: 16px;
    border-left: 5px solid #f59e0b;
}
.success-box {
    background-color: #e5e7eb;
    padding: 18px;
    border-radius: 16px;
    border-left: 5px solid #22c55e;
}
</style>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
# 🧠 AI et les etudiants
### Un dashboard analytique pour comprendre l’impact de l’IA générative sur les étudiants

Ce tableau de bord analyse les comportements étudiants face aux outils IA : usage, performance, dépendance et bien-être.
""")

st.divider()

# KPIs
students = df.shape[0]
features = df.shape[1]
avg_ai = df["Weekly_GenAI_Hours"].mean()
avg_gpa = df["Post_Semester_GPA"].mean()
avg_anxiety = df["Anxiety_Level_During_Exams"].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <h3>👥 Étudiants</h3>
        <h1>{students:,}</h1>
        <p>observations analysées</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <h3>📊 Variables</h3>
        <h1>{features}</h1>
        <p>dimensions étudiées</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <h3>🤖 Usage IA</h3>
        <h1>{avg_ai:.2f}h</h1>
        <p>par semaine en moyenne</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <h3>🎓 GPA moyen</h3>
        <h1>{avg_gpa:.2f}</h1>
        <p>après semestre</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# Executive summary
gpa_gain = df["Post_Semester_GPA"].mean() - df["Pre_Semester_GPA"].mean()
top_major = df.groupby("Major_Category")["Weekly_GenAI_Hours"].mean().idxmax()
burnout_top = df["Burnout_Risk_Level"].value_counts().idxmax()

st.markdown("## 🔎 Lecture rapide des résultats")

colA, colB, colC = st.columns(3)

with colA:
    st.markdown(f"""
    <div class="success-box">
        <h3>Performance</h3>
        <p>Le GPA moyen évolue de <b>{gpa_gain:.2f}</b> point(s) entre le début et la fin du semestre.</p>
    </div>
    """, unsafe_allow_html=True)

with colB:
    st.markdown(f"""
    <div class="insight">
        <h3>Filière la plus IA</h3>
        <p>La filière avec l’usage moyen d’IA le plus élevé est <b>{top_major}</b>.</p>
    </div>
    """, unsafe_allow_html=True)

with colC:
    st.markdown(f"""
    <div class="warning-box">
        <h3>Burnout</h3>
        <p>Le niveau de burnout le plus fréquent est <b>{burnout_top}</b>.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# Graphs
st.markdown("## 📈 Analyse visuelle")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Distribution de l’usage IA")
    fig, ax = plt.subplots(figsize=(4.5, 2.7))
    ax.hist(df["Weekly_GenAI_Hours"], bins=25)
    ax.set_xlabel("Heures IA / semaine")
    ax.set_ylabel("Nombre d’étudiants")
    ax.set_title("Répartition de l’usage IA")
    st.pyplot(fig)

    st.caption("On observe la distribution des étudiants selon leur temps d’utilisation hebdomadaire de l’IA.")

with col2:
    st.markdown("### IA moyenne par filière")
    major_ai = df.groupby("Major_Category")["Weekly_GenAI_Hours"].mean().sort_values(ascending=False)

    fig2, ax2 = plt.subplots(figsize=(4.5, 2.7))
    major_ai.plot(kind="bar", ax=ax2)
    ax2.set_ylabel("Heures IA moyennes")
    ax2.set_title("Usage IA selon la filière")
    plt.xticks(rotation=25)
    st.pyplot(fig2)

    st.caption("Ce graphique permet d’identifier les filières les plus exposées aux outils IA.")

st.divider()

# Burnout + GPA
col3, col4 = st.columns(2)

with col3:
    st.markdown("### Burnout et usage IA")
    burnout_ai = df.groupby("Burnout_Risk_Level")["Weekly_GenAI_Hours"].mean()

    fig3, ax3 = plt.subplots(figsize=(4.5, 2.7))
    burnout_ai.plot(kind="bar", ax=ax3)
    ax3.set_ylabel("Heures IA moyennes")
    ax3.set_title("Usage IA selon le burnout")
    plt.xticks(rotation=0)
    st.pyplot(fig3)

    st.caption("Cette analyse explore le lien possible entre usage intensif de l’IA et bien-être étudiant.")

with col4:
    st.markdown("### Évolution du GPA")
    gpa = df[["Pre_Semester_GPA", "Post_Semester_GPA"]].mean()

    fig4, ax4 = plt.subplots(figsize=(4.5, 2.7))
    gpa.plot(kind="bar", ax=ax4)
    ax4.set_ylabel("GPA moyen")
    ax4.set_title("Avant vs après semestre")
    plt.xticks(rotation=20)
    st.pyplot(fig4)

    st.caption("Ce graphique compare la performance académique moyenne avant et après le semestre.")

st.divider()

# AI dependency score
st.markdown("## 🧪 Indice de dépendance et d’impact IA")

dependency = df["Perceived_AI_Dependency"].mean()
tool_diversity = df["Tool_Diversity"].mean()

col5, col6 = st.columns(2)

with col5:
    st.markdown(f"""
    <div class="metric-card">
        <h3>Indice moyen de dépendance IA</h3>
        <h1>{dependency:.2f}/10</h1>
        <p>mesure déclarative de dépendance aux outils IA</p>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown(f"""
    <div class="metric-card">
        <h3>Diversité moyenne des outils IA</h3>
        <h1>{tool_diversity:.2f}/5</h1>
        <p>nombre moyen d’outils IA utilisés</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# Correlations
st.markdown("## 🧩 Variables les plus liées au GPA final")

numeric_df = df.select_dtypes(include="number")
corr = numeric_df.corr()

top_corr = (
    corr["Post_Semester_GPA"]
    .drop("Post_Semester_GPA")
    .abs()
    .sort_values(ascending=False)
    .head(5)
)

for var, val in top_corr.items():
    st.write(f"**{var}**")
    st.progress(float(val))
    st.caption(f"Corrélation absolue : {val:.2f}")

st.divider()

# Dataset preview
with st.expander("📁 Voir un aperçu du dataset"):
    st.dataframe(df.head(15), use_container_width=True)

# Conclusion
st.markdown("""
## ✅ Conclusion

Ce dashboard met en évidence plusieurs dimensions de l’impact de l’IA générative sur les étudiants :
performance académique, habitudes d’étude, dépendance, anxiété et burnout.

L’objectif n’est pas simplement de dire si l’IA est positive ou négative, mais de comprendre **dans quelles conditions elle peut devenir un outil utile ou un facteur de risque**.
""")