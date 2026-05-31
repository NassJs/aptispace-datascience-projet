import streamlit as st


def section_header(title, subtitle):
    st.markdown(
        f"""
        <div class="section-header">
            <h2>{title}</h2>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def info_card(icon, badge, title, text):
    st.markdown(
        f"""
        <div class="info-card">
            <div class="service-icon">{icon}</div>
            <span class="badge">{badge}</span>
            <div class="info-title">{title}</div>
            <div class="info-text">{text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )