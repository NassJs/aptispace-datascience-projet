import plotly.express as px
import streamlit as st


def plot_ai_usage_by_major(df):
    data = (
        df.groupby("Major_Category")["Weekly_GenAI_Hours"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        data,
        x="Major_Category",
        y="Weekly_GenAI_Hours",
        title="Usage moyen de l’IA par filière",
    )

    st.plotly_chart(fig, use_container_width=True)


def plot_burnout_distribution(df):
    data = df["Burnout_Risk_Level"].value_counts().reset_index()
    data.columns = ["Burnout", "Nombre"]

    fig = px.pie(
        data,
        names="Burnout",
        values="Nombre",
        title="Répartition du risque de burnout",
    )

    st.plotly_chart(fig, use_container_width=True)


def plot_gpa_evolution(df):
    avg_pre = df["Pre_Semester_GPA"].mean()
    avg_post = df["Post_Semester_GPA"].mean()

    data = {
        "Période": ["Avant semestre", "Après semestre"],
        "GPA moyen": [avg_pre, avg_post],
    }

    fig = px.bar(
        data,
        x="Période",
        y="GPA moyen",
        title="Évolution moyenne du GPA",
    )

    st.plotly_chart(fig, use_container_width=True)


def plot_dependency_distribution(df):
    fig = px.histogram(
        df,
        x="Perceived_AI_Dependency",
        title="Distribution de la dépendance perçue à l’IA",
    )

    st.plotly_chart(fig, use_container_width=True)