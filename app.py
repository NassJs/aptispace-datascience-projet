from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
import base64

def image_to_base64(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from io import BytesIO
import streamlit as st
import pandas as pd
from textwrap import dedent
from src.components.sidebar import show_sidebar
from src.components.charts import (
    show_ai_hours_chart,
    show_burnout_chart,
    show_gpa_chart,
    show_dependency_chart
)

st.set_page_config(
    page_title="AI Student Impact Dashboard",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


@st.cache_data
def load_data():
    return pd.read_csv("data/raw/ai_student_impact_dataset (1).csv")


df = load_data()

page = show_sidebar()


st.markdown("""
<style>
.stApp {
    background: #0b1120;
}

.main .block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.section-title {
    font-size: 26px;
    font-weight: 900;
    color: #f8fafc;
    margin: 30px 0 10px 0;
}

.section-text {
    color: #94a3b8;
    font-size: 15px;
    margin-bottom: 20px;
}

.info-card {
    background: rgba(15, 23, 42, 0.92);
    border: 1px solid rgba(148, 163, 184, 0.18);
    border-radius: 24px;
    padding: 24px;
    box-shadow: 0 18px 45px rgba(2, 6, 23, 0.35);
    margin-bottom: 20px;
}

.info-title {
    color: #f8fafc;
    font-size: 20px;
    font-weight: 800;
    margin-bottom: 8px;
}

.info-text {
    color: #cbd5e1;
    font-size: 15px;
    line-height: 1.6;
}

.badge {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 999px;
    background: rgba(56,189,248,0.12);
    color: #38bdf8;
    font-size: 13px;
    font-weight: 700;
    border: 1px solid rgba(56,189,248,0.25);
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)




if page == "🏠 Dashboard":

    hero_bg = image_to_base64("assets/images/bg.gif")
    about_img = image_to_base64("assets/images/bg4.jpg")
    ai_img = image_to_base64("assets/images/bg2.jpg")
    perf_img = image_to_base64("assets/images/bg3.jpg")
    well_img = image_to_base64("assets/images/bg1.jpg")

    st.markdown(f"""
<style>
.hero-site {{
    min-height: 540px;
    border-radius: 34px;
    background:
        linear-gradient(135deg, rgba(2,6,23,0.82), rgba(49,46,129,0.72)),
        url("data:image/gif;base64,{hero_bg}");
    background-size: cover;
    background-position: center;
    padding: 80px 60px;
    display: flex;
    align-items: center;
    box-shadow: 0 24px 65px rgba(0,0,0,0.40);
    margin-bottom: 45px;
}}

.hero-site h1 {{
    color: white;
    font-size: 58px;
    font-weight: 900;
    line-height: 1.1;
    max-width: 900px;
}}

.hero-site h1 span {{
    color: #38bdf8;
}}

.hero-site p {{
    color: #dbeafe;
    font-size: 19px;
    line-height: 1.8;
    max-width: 780px;
    margin-top: 18px;
}}

.hero-buttons {{
    margin-top: 32px;
}}

.hero-btn-primary,
.hero-btn-secondary {{
    display: inline-block;
    padding: 14px 22px;
    border-radius: 999px;
    margin-right: 12px;
    font-weight: 900;
}}

.hero-btn-primary {{
    background: linear-gradient(135deg, #38bdf8, #8b5cf6);
    color: white;
}}

.hero-btn-secondary {{
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.25);
    color: white;
}}

.section-header {{
    text-align: center;
    margin: 50px 0 28px;
}}

.section-header h2 {{
    color: white;
    font-size: 36px;
    font-weight: 900;
}}

.section-header p {{
    color: #94a3b8;
    font-size: 16px;
}}

.about-section {{
    display: grid;
    grid-template-columns: 0.9fr 1.1fr;
    gap: 35px;
    align-items: center;
    margin-bottom: 50px;
}}

.about-img {{
    border-radius: 30px;
    overflow: hidden;
    box-shadow: 0 20px 55px rgba(0,0,0,0.35);
}}

.about-img img {{
    width: 100%;
    display: block;
}}

.about-content,
.info-card {{
    background: rgba(15,23,42,0.92);
    border: 1px solid rgba(148,163,184,0.18);
    border-radius: 28px;
    padding: 30px;
    box-shadow: 0 18px 45px rgba(2,6,23,0.35);
}}

.about-content h2 {{
    color: #38bdf8;
    font-weight: 900;
}}

.about-content h3,
.info-title {{
    color: white;
    font-size: 24px;
    font-weight: 900;
}}

.about-content p,
.about-content li,
.info-text {{
    color: #cbd5e1;
    line-height: 1.8;
}}

.services-grid,
.image-summary-grid,
.learning-zone {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 22px;
}}

.info-card {{
    min-height: 260px;
    transition: 0.3s;
}}

.info-card:hover {{
    transform: translateY(-7px);
    border-color: rgba(56,189,248,0.45);
}}

.service-icon {{
    width: 58px;
    height: 58px;
    border-radius: 18px;
    background: linear-gradient(135deg, #38bdf8, #8b5cf6);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 30px;
    margin-bottom: 18px;
}}

.badge {{
    display: inline-block;
    padding: 8px 14px;
    border-radius: 999px;
    background: rgba(56,189,248,0.12);
    color: #67e8f9;
    font-size: 13px;
    font-weight: 800;
    border: 1px solid rgba(56,189,248,0.28);
    margin-bottom: 14px;
}}

.summary-img-card {{
    background: rgba(15,23,42,0.92);
    border-radius: 26px;
    overflow: hidden;
    border: 1px solid rgba(148,163,184,0.18);
    box-shadow: 0 18px 45px rgba(2,6,23,0.35);
}}

.summary-img-card img {{
    width: 100%;
    height: 190px;
    object-fit: cover;
}}

.summary-img-card div {{
    padding: 22px;
}}

.summary-img-card h3 {{
    color: white;
    font-size: 22px;
}}

.summary-img-card p {{
    color: #cbd5e1;
    line-height: 1.7;
}}

.learning-card {{
    background: linear-gradient(135deg, rgba(15,23,42,0.96), rgba(30,41,59,0.95));
    border: 1px solid rgba(148,163,184,0.18);
    border-radius: 26px;
    padding: 28px;
    min-height: 230px;
    box-shadow: 0 18px 45px rgba(2,6,23,0.35);
}}

.learning-card h3 {{
    color: white;
    font-size: 23px;
}}

.learning-card p {{
    color: #cbd5e1;
    line-height: 1.7;
}}

.analytics-card {{
    background: rgba(15,23,42,0.92);
    border: 1px solid rgba(148,163,184,0.18);
    border-radius: 26px;
    padding: 24px;
    box-shadow: 0 18px 45px rgba(2,6,23,0.35);
    margin-bottom: 22px;
}}

.analytics-title {{
    color: white;
    font-size: 22px;
    font-weight: 900;
    margin-bottom: 8px;
}}

.analytics-text {{
    color: #94a3b8;
    font-size: 14px;
    margin-bottom: 16px;
}}

.tip-box {{
    background: rgba(34,197,94,0.12);
    border-left: 6px solid #22c55e;
    border-radius: 20px;
    padding: 24px;
    color: #dcfce7;
    line-height: 1.7;
}}

.warning-box {{
    background: rgba(249,115,22,0.12);
    border-left: 6px solid #f97316;
    border-radius: 20px;
    padding: 24px;
    color: #fed7aa;
    line-height: 1.7;
}}

@media (max-width: 900px) {{
    .about-section,
    .services-grid,
    .image-summary-grid,
    .learning-zone {{
        grid-template-columns: 1fr;
    }}

    .hero-site {{
        padding: 50px 30px;
    }}

    .hero-site h1 {{
        font-size: 38px;
    }}
}}
</style>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="hero-site">
<div>
<h1>Comprendre ton rapport <span>à l’intelligence artificielle</span></h1>
<p>
Cette plateforme aide les étudiants à mieux comprendre comment l’usage de l’IA
peut influencer leurs habitudes d’étude, leurs performances, leur autonomie
et leur bien-être.
</p>
<div class="hero-buttons">
<span class="hero-btn-primary">🤖 Tester mon profil</span>
<span class="hero-btn-secondary">📊 Voir les analyses</span>
</div>
</div>
</div>
""", unsafe_allow_html=True)

    st.markdown(f"""
<div class="about-section">
<div class="about-img">
<img src="data:image/jpg;base64,{about_img}">
</div>
<div class="about-content">
<h2>À propos</h2>
<h3>Une plateforme pour mieux apprendre avec l’IA</h3>
<p>
L’objectif est d’aider les étudiants à utiliser l’intelligence artificielle comme un assistant
d’apprentissage, sans perdre leur autonomie ni remplacer leur réflexion personnelle.
</p>
<ul>
<li>✅ Comprendre son usage de l’IA</li>
<li>✅ Mesurer l’impact académique</li>
<li>✅ Prévenir la dépendance et le burnout</li>
<li>✅ Générer un planning personnalisé</li>
</ul>
</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="section-header">
<h2>🚀 Ce que tu peux faire ici</h2>
<p>Six fonctionnalités pour analyser, comprendre et mieux organiser ton apprentissage avec l’IA.</p>
</div>

<div class="services-grid">
<div class="info-card">
<div class="service-icon">🤖</div>
<span class="badge">Comprendre</span>
<div class="info-title">Ton usage de l’IA</div>
<div class="info-text">Découvre comment l’IA est utilisée dans les études.</div>
</div>

<div class="info-card">
<div class="service-icon">🎓</div>
<span class="badge">Analyser</span>
<div class="info-title">Impact académique</div>
<div class="info-text">Observe les liens entre usage IA et performances.</div>
</div>

<div class="info-card">
<div class="service-icon">🧠</div>
<span class="badge">Prévenir</span>
<div class="info-title">Risque de dépendance</div>
<div class="info-text">Identifie les signaux de vigilance.</div>
</div>

<div class="info-card">
<div class="service-icon">📅</div>
<span class="badge">Organiser</span>
<div class="info-title">Planning personnalisé</div>
<div class="info-text">Génère un emploi du temps adapté à ton profil.</div>
</div>

<div class="info-card">
<div class="service-icon">📊</div>
<span class="badge">Comparer</span>
<div class="info-title">Comparaison par filière</div>
<div class="info-text">Compare ton usage avec ta filière.</div>
</div>

<div class="info-card">
<div class="service-icon">📁</div>
<span class="badge">Explorer</span>
<div class="info-title">Dataset interactif</div>
<div class="info-text">Consulte, filtre et exporte les données.</div>
</div>
</div>
""", unsafe_allow_html=True)

    st.markdown(f"""
<div class="section-header">
<h2>🧠 Résumé intelligent</h2>
<p>Trois axes pour comprendre l’impact de l’IA sur les étudiants.</p>
</div>

<div class="image-summary-grid">
<div class="summary-img-card">
<img src="data:image/jpg;base64,{ai_img}">
<div>
<h3>Usage IA</h3>
<p>Temps passé avec l’IA, diversité des outils et assistance numérique.</p>
</div>
</div>

<div class="summary-img-card">
<img src="data:image/jpg;base64,{perf_img}">
<div>
<h3>Performance</h3>
<p>Évolution académique, productivité et autonomie.</p>
</div>
</div>

<div class="summary-img-card">
<img src="data:image/jpg;base64,{well_img}">
<div>
<h3>Bien-être</h3>
<p>Anxiété, dépendance perçue et surcharge mentale.</p>
</div>
</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="section-header">
<h2>🌍 L’IA dans la vie étudiante</h2>
<p>Une lecture plus humaine de l’impact de l’IA au quotidien.</p>
</div>

<div class="learning-zone">
<div class="learning-card">
<h3>🤖 Assistance intelligente</h3>
<p>L’IA aide à comprendre, reformuler, corriger ou structurer un devoir.</p>
</div>

<div class="learning-card">
<h3>📚 Apprentissage actif</h3>
<p>Le meilleur usage consiste à réfléchir avant d’utiliser l’IA.</p>
</div>

<div class="learning-card">
<h3>⚠️ Équilibre personnel</h3>
<p>Une utilisation excessive peut réduire l’autonomie.</p>
</div>
</div>
""", unsafe_allow_html=True)


elif page == "📊 Analytics":

    st.markdown("""
<div class="section-header">
<h2>📊 Analytics & Insights</h2>
<p>Analyse visuelle de l’usage IA, du burnout, du GPA et de la dépendance.</p>
</div>
""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
<div class="analytics-card">
<div class="analytics-title">🤖 Usage hebdomadaire de l’IA</div>
<div class="analytics-text">Distribution des heures d’utilisation de l’IA.</div>
""", unsafe_allow_html=True)
        show_ai_hours_chart(df)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("""
<div class="analytics-card">
<div class="analytics-title">🔥 Risque de burnout</div>
<div class="analytics-text">Répartition des niveaux de burnout.</div>
""", unsafe_allow_html=True)
        show_burnout_chart(df)
        st.markdown("</div>", unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
<div class="analytics-card">
<div class="analytics-title">🎓 GPA académique</div>
<div class="analytics-text">Évolution des performances académiques.</div>
""", unsafe_allow_html=True)
        show_gpa_chart(df)
        st.markdown("</div>", unsafe_allow_html=True)

    with col4:
        st.markdown("""
<div class="analytics-card">
<div class="analytics-title">🧠 Dépendance à l’IA</div>
<div class="analytics-text">Niveau de dépendance déclaré.</div>
""", unsafe_allow_html=True)
        show_dependency_chart(df)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
<div class="section-header">
<h2>🧠 Lecture intelligente des résultats</h2>
<p>Résumé automatique des principaux enseignements observés.</p>
</div>
""", unsafe_allow_html=True)

    top_major = (
        df.groupby("Major_Category")["Weekly_GenAI_Hours"]
        .mean()
        .sort_values(ascending=False)
        .index[0]
    )

    burnout_top = df["Burnout_Risk_Level"].value_counts().index[0]

    gpa_gain = df["Post_Semester_GPA"].mean() - df["Pre_Semester_GPA"].mean()

    r1, r2, r3 = st.columns(3)

    with r1:
        st.metric("Filière la plus IA", top_major)

    with r2:
        st.metric("Burnout dominant", burnout_top)

    with r3:
        st.metric("Évolution GPA", round(gpa_gain, 2))

    st.markdown("""
<div class="section-header">
<h2>🎯 Analyse croisée</h2>
<p>Comparaison de l’usage IA moyen selon les filières.</p>
</div>
""", unsafe_allow_html=True)

    ai_by_major = (
        df.groupby("Major_Category")["Weekly_GenAI_Hours"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    st.dataframe(ai_by_major, use_container_width=True)

    st.info(
        "Cette analyse permet de comprendre comment l’usage de l’IA varie selon les filières "
        "et comment il peut être lié à la performance, à l’autonomie et au bien-être étudiant."
    )


elif page == "🤖 Prediction IA":

    # =========================
    # IMAGES
    # =========================

    pred_bg = image_to_base64("assets/images/bg1.jpg")
    student_img = image_to_base64("assets/images/bg2.jpg")
    stress_img = image_to_base64("assets/images/bg3.jpg")
    planning_img = image_to_base64("assets/images/bg4.jpg")

    # =========================
    # STYLE
    # =========================

    st.markdown(f"""
<style>

.pred-hero {{
    min-height: 420px;
    border-radius: 35px;
    background:
        linear-gradient(135deg, rgba(2,6,23,0.84), rgba(49,46,129,0.78)),
        url("data:image/jpg;base64,{pred_bg}");
    background-size: cover;
    background-position: center;
    padding: 60px;
    display: flex;
    align-items: center;
    margin-bottom: 35px;
    box-shadow: 0 25px 60px rgba(0,0,0,0.35);
}}

.pred-badge {{
    display: inline-block;
    padding: 10px 18px;
    border-radius: 999px;
    background: rgba(56,189,248,0.18);
    border: 1px solid rgba(56,189,248,0.35);
    color: #67e8f9;
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 20px;
}}

.pred-hero h1 {{
    color: white;
    font-size: 52px;
    font-weight: 900;
    line-height: 1.1;
}}

.pred-hero p {{
    color: #dbeafe;
    font-size: 18px;
    line-height: 1.8;
    max-width: 780px;
}}

.pred-grid {{
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 22px;
    margin-bottom: 35px;
}}

.pred-card {{
    background: rgba(15,23,42,0.95);
    border-radius: 28px;
    padding: 22px;
    border: 1px solid rgba(148,163,184,0.15);
    box-shadow: 0 18px 45px rgba(2,6,23,0.35);
    transition: 0.3s;
}}

.pred-card:hover {{
    transform: translateY(-7px);
}}

.pred-image {{
    width: 100%;
    height: 180px;
    object-fit: cover;
    border-radius: 20px;
    margin-bottom: 18px;
}}

.pred-title {{
    color: white;
    font-size: 24px;
    font-weight: 900;
    margin-bottom: 10px;
}}

.pred-text {{
    color: #94a3b8;
    line-height: 1.7;
}}

.form-card {{
    background: rgba(15,23,42,0.94);
    border-radius: 30px;
    padding: 30px;
    border: 1px solid rgba(148,163,184,0.15);
    box-shadow: 0 18px 45px rgba(2,6,23,0.35);
    margin-top: 25px;
}}

.risk-box {{
    border-radius: 28px;
    padding: 35px;
    margin-top: 30px;
    color: white;
    box-shadow: 0 25px 60px rgba(0,0,0,0.35);
}}

.risk-low {{
    background: linear-gradient(135deg, #065f46, #16a34a);
}}

.risk-medium {{
    background: linear-gradient(135deg, #92400e, #f97316);
}}

.risk-high {{
    background: linear-gradient(135deg, #7f1d1d, #ef4444);
}}

.planning-card {{
    background: rgba(15,23,42,0.94);
    border-radius: 28px;
    padding: 28px;
    border: 1px solid rgba(148,163,184,0.15);
    margin-top: 30px;
}}

.result-title {{
    color: white;
    font-size: 30px;
    font-weight: 900;
}}

@media(max-width: 900px) {{

    .pred-grid {{
        grid-template-columns: 1fr;
    }}

    .pred-hero {{
        padding: 35px;
    }}

    .pred-hero h1 {{
        font-size: 35px;
    }}
}}

</style>
""", unsafe_allow_html=True)

    # =========================
    # HERO
    # =========================

    st.markdown(f"""
<div class="pred-hero">
<div>

<span class="pred-badge">
IA • ANALYSE • ORGANISATION • BIEN-ÊTRE
</span>

<h1>
Analyse ton équilibre avec l’intelligence artificielle
</h1>

<p>
Cette simulation intelligente évalue ton usage de l’IA,
ton autonomie, ton stress académique et ton organisation
afin de générer des conseils personnalisés,
des recommandations intelligentes et un planning étudiant.
</p>

</div>
</div>
""", unsafe_allow_html=True)

    # =========================
    # CARDS
    # =========================

    st.markdown(f"""
<div class="pred-grid">

<div class="pred-card">
<img src="data:image/jpg;base64,{student_img}" class="pred-image">

<div class="pred-title">
🤖 Usage IA
</div>

<div class="pred-text">
Analyse la manière dont tu utilises les outils IA
dans tes études et ton quotidien académique.
</div>
</div>

<div class="pred-card">
<img src="data:image/jpg;base64,{stress_img}" class="pred-image">

<div class="pred-title">
🧠 Stress & autonomie
</div>

<div class="pred-text">
Détecte les signaux liés à l’anxiété,
à la surcharge mentale et à la dépendance IA.
</div>
</div>

<div class="pred-card">
<img src="data:image/jpg;base64,{planning_img}" class="pred-image">

<div class="pred-title">
📅 Planning intelligent
</div>

<div class="pred-text">
Génère automatiquement un emploi du temps
personnalisé et téléchargeable en PDF.
</div>
</div>

</div>
""", unsafe_allow_html=True)

    # =========================
    # FORMULAIRE
    # =========================

    st.markdown('<div class="form-card">', unsafe_allow_html=True)

    st.markdown("## 🧪 Tester mon profil étudiant")

    col1, col2 = st.columns(2)

    with col1:

        major = st.selectbox(
            "🎓 Filière",
            sorted(df["Major_Category"].dropna().unique())
        )

        weekly_ai = st.slider(
            "🤖 Heures IA / semaine",
            0,
            40,
            8
        )

        dependency = st.slider(
            "🧩 Dépendance perçue à l’IA",
            1,
            10,
            4
        )

    with col2:

        study_hours = st.slider(
            "📚 Heures d’étude classique",
            1,
            36,
            10
        )

        anxiety = st.slider(
            "🧠 Niveau d’anxiété",
            1,
            10,
            4
        )

        tool_diversity = st.slider(
            "🛠️ Nombre d’outils IA utilisés",
            1,
            5,
            2
        )

    # =========================
    # BOUTON
    # =========================

    if st.button("🔍 Lancer l’analyse IA", use_container_width=True):

        score = 0

        # Usage IA
        if weekly_ai >= 25:
            score += 3
        elif weekly_ai >= 12:
            score += 2
        elif weekly_ai >= 6:
            score += 1

        # Dépendance
        if dependency >= 8:
            score += 3
        elif dependency >= 5:
            score += 2
        elif dependency >= 3:
            score += 1

        # Anxiété
        if anxiety >= 8:
            score += 3
        elif anxiety >= 5:
            score += 2
        elif anxiety >= 3:
            score += 1

        # Études classiques
        if study_hours <= 5:
            score += 2
        elif study_hours <= 10:
            score += 1

        # Diversité outils IA
        if tool_diversity >= 4:
            score += 1

        risk_percent = round((score / 12) * 100, 1)

        # =========================
        # RESULTAT
        # =========================

        if score >= 8:

            niveau = "ÉLEVÉ"
            css_class = "risk-high"

            message = """
            Ton profil montre plusieurs signaux de surcharge.
            Il est conseillé de réduire la dépendance à l’IA
            et renforcer l’apprentissage autonome.
            """

        elif score >= 5:

            niveau = "MODÉRÉ"
            css_class = "risk-medium"

            message = """
            Ton usage de l’IA reste correct
            mais certains comportements doivent être équilibrés.
            """

        else:

            niveau = "FAIBLE"
            css_class = "risk-low"

            message = """
            Ton usage semble globalement équilibré.
            L’IA est utilisée comme un support utile.
            """

        st.markdown(f"""
<div class="risk-box {css_class}">

<div class="result-title">
📊 Risque estimé : {niveau}
</div>

<br>

<h2>{risk_percent}%</h2>

<p>
{message}
</p>

</div>
""", unsafe_allow_html=True)

        st.progress(risk_percent / 100)

        # =========================
        # RECOMMANDATIONS
        # =========================

        st.markdown("## 🧠 Recommandations intelligentes")

        if dependency >= 7:
            st.warning("⚠️ Réduis les usages automatiques de l’IA.")

        if anxiety >= 7:
            st.warning("⚠️ Organise tes révisions plus tôt pour réduire le stress.")

        if study_hours <= 8:
            st.info("📚 Augmente progressivement tes heures d’étude sans IA.")

        if weekly_ai > 20:
            st.warning("⚠️ Essaie d’avoir des sessions sans assistant IA.")

        if score < 5:
            st.success("✅ Ton profil semble relativement équilibré.")

        # =========================
        # EMPLOI DU TEMPS
        # =========================

        st.markdown('<div class="planning-card">', unsafe_allow_html=True)

        st.markdown("## 📅 Emploi du temps conseillé")

        planning = pd.DataFrame({

            "Jour": [
                "Lundi",
                "Mardi",
                "Mercredi",
                "Jeudi",
                "Vendredi",
                "Samedi",
                "Dimanche"
            ],

            "Objectif": [
                "Révision",
                "Exercices",
                "Projet",
                "Révision",
                "Synthèse",
                "Repos actif",
                "Organisation"
            ],

            "Temps conseillé": [
                "2h",
                "2h30",
                "3h",
                "2h",
                "1h30",
                "1h",
                "45 min"
            ],

            "IA autorisée": [
                "30 min",
                "20 min",
                "40 min",
                "20 min",
                "30 min",
                "Non",
                "15 min"
            ]
        })

        st.dataframe(planning, use_container_width=True)

        # =========================
        # PDF
        # =========================

        buffer = BytesIO()

        doc = SimpleDocTemplate(
            buffer,
            pagesize=letter,
            rightMargin=30,
            leftMargin=30,
            topMargin=30,
            bottomMargin=20
        )

        styles = getSampleStyleSheet()
        elements = []

        elements.append(
            Paragraph(
                "<b>Emploi du temps personnalisé - IA & Études</b>",
                styles["Title"]
            )
        )

        elements.append(Spacer(1, 14))

        elements.append(
            Paragraph(
                f"""
                Filière : <b>{major}</b><br/>
                Niveau de risque : <b>{niveau}</b><br/>
                Score estimé : <b>{score}/12</b><br/>
                Probabilité : <b>{risk_percent}%</b>
                """,
                styles["BodyText"]
            )
        )

        elements.append(Spacer(1, 18))

        table_data = [planning.columns.tolist()] + planning.values.tolist()

        table = Table(table_data, repeatRows=1)

        table.setStyle(TableStyle([

            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#312e81")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

            ("FONTSIZE", (0, 0), (-1, -1), 9),

            ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#f8fafc")),

            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),

        ]))

        elements.append(table)

        doc.build(elements)

        pdf = buffer.getvalue()

        buffer.close()

        st.download_button(
            label="📄 Télécharger mon emploi du temps en PDF",
            data=pdf,
            file_name="emploi_du_temps_ia_etudiant.pdf",
            mime="application/pdf",
            use_container_width=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)






elif page == "📁 Dataset":

    st.markdown('<div class="section-title">📁 Dataset Explorer</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-text">Explore, filtre, analyse et télécharge les données utilisées dans le projet.</div>',
        unsafe_allow_html=True
    )

    st.write("")

    # KPIs dataset
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Lignes", df.shape[0])

    with col2:
        st.metric("Colonnes", df.shape[1])

    with col3:
        st.metric("Valeurs manquantes", int(df.isnull().sum().sum()))

    with col4:
        st.metric("Doublons", int(df.duplicated().sum()))

    st.divider()

    # Recherche + filtres
    st.markdown("### 🔎 Recherche et filtres")

    colA, colB, colC = st.columns(3)

    with colA:
        search = st.text_input("Rechercher", placeholder="Ex : STEM, High, Beginner...")

    with colB:
        major_filter = st.multiselect(
            "Filière",
            options=sorted(df["Major_Category"].dropna().unique()),
            default=sorted(df["Major_Category"].dropna().unique())
        )

    with colC:
        burnout_filter = st.multiselect(
            "Burnout",
            options=sorted(df["Burnout_Risk_Level"].dropna().unique()),
            default=sorted(df["Burnout_Risk_Level"].dropna().unique())
        )

    colD, colE = st.columns(2)

    with colD:
        year_filter = st.multiselect(
            "Année d’étude",
            options=sorted(df["Year_of_Study"].dropna().unique()),
            default=sorted(df["Year_of_Study"].dropna().unique())
        )

    with colE:
        policy_filter = st.multiselect(
            "Politique IA",
            options=sorted(df["Institutional_Policy"].dropna().unique()),
            default=sorted(df["Institutional_Policy"].dropna().unique())
        )

    filtered_df = df.copy()

    filtered_df = filtered_df[
        filtered_df["Major_Category"].isin(major_filter)
        & filtered_df["Burnout_Risk_Level"].isin(burnout_filter)
        & filtered_df["Year_of_Study"].isin(year_filter)
        & filtered_df["Institutional_Policy"].isin(policy_filter)
    ]

    if search:
        filtered_df = filtered_df[
            filtered_df.astype(str)
            .apply(
                lambda row: row.str.contains(search, case=False, na=False).any(),
                axis=1
            )
        ]

    st.success(f"{filtered_df.shape[0]} lignes trouvées sur {df.shape[0]}")

    st.divider()

    # Choix colonnes
    st.markdown("### 🧩 Colonnes à afficher")

    selected_columns = st.multiselect(
        "Sélectionner les colonnes",
        options=list(filtered_df.columns),
        default=list(filtered_df.columns[:8])
    )

    if selected_columns:
        display_df = filtered_df[selected_columns]
    else:
        display_df = filtered_df

    # Tableau
    st.markdown("### 📋 Tableau dynamique")

    st.dataframe(
        display_df,
        use_container_width=True,
        height=450
    )

    st.divider()

    # Statistiques rapides
    st.markdown("### 📊 Statistiques rapides")

    numeric_cols = filtered_df.select_dtypes(include="number").columns.tolist()

    if numeric_cols:
        selected_numeric = st.selectbox(
            "Choisir une variable numérique",
            numeric_cols
        )

        colS1, colS2, colS3, colS4 = st.columns(4)

        with colS1:
            st.metric("Moyenne", round(filtered_df[selected_numeric].mean(), 2))

        with colS2:
            st.metric("Minimum", round(filtered_df[selected_numeric].min(), 2))

        with colS3:
            st.metric("Maximum", round(filtered_df[selected_numeric].max(), 2))

        with colS4:
            st.metric("Écart-type", round(filtered_df[selected_numeric].std(), 2))

    st.divider()

    # Téléchargement
    st.markdown("### 📥 Export")

    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Télécharger les données filtrées",
        data=csv,
        file_name="ai_student_impact_filtered.csv",
        mime="text/csv",
        use_container_width=True
    )