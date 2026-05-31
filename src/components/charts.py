import streamlit as st
import pandas as pd


def show_ai_hours_chart(df):
    st.markdown("#### ⏱️ Heures d’utilisation de l’IA")
    chart_data = df[["Weekly_GenAI_Hours"]].copy()
    st.bar_chart(chart_data.head(80))


def show_burnout_chart(df):
    st.markdown("#### 🔥 Répartition du risque de burnout")
    burnout_counts = df["Burnout_Risk_Level"].value_counts()
    st.bar_chart(burnout_counts)


def show_gpa_chart(df):
    st.markdown("#### 🎓 GPA avant vs après semestre")
    gpa = df[["Pre_Semester_GPA", "Post_Semester_GPA"]].head(80)
    st.line_chart(gpa)


def show_dependency_chart(df):
    st.markdown("#### 🧠 Dépendance perçue à l’IA")
    dependency = df["Perceived_AI_Dependency"].value_counts().sort_index()
    st.bar_chart(dependency)