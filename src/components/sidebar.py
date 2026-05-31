import streamlit as st

def show_sidebar():
    with st.sidebar:
        st.markdown("""
        <style>
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #020617 0%, #0f172a 45%, #111827 100%);
            border-right: 1px solid rgba(148, 163, 184, 0.12);
            box-shadow: 12px 0 40px rgba(0,0,0,0.28);
        }

        [data-testid="stSidebar"] > div:first-child {
            padding-top: 18px;
            padding-left: 16px;
            padding-right: 16px;
        }

        [data-testid="stSidebar"] * {
            color: #e5e7eb;
        }

        .side-shell {
            position: relative;
            overflow: hidden;
            border-radius: 28px;
            padding: 18px 16px 16px 16px;
            background: linear-gradient(180deg, rgba(15,23,42,0.9), rgba(2,6,23,0.86));
            border: 1px solid rgba(148,163,184,0.14);
            box-shadow: 0 22px 50px rgba(0,0,0,0.32);
        }

        .side-shell::before {
            content: "";
            position: absolute;
            inset: -40px auto auto -40px;
            width: 140px;
            height: 140px;
            background: radial-gradient(circle, rgba(56,189,248,0.26) 0%, rgba(56,189,248,0.04) 55%, transparent 72%);
            pointer-events: none;
        }

        .side-shell::after {
            content: "";
            position: absolute;
            right: -50px;
            bottom: -50px;
            width: 160px;
            height: 160px;
            background: radial-gradient(circle, rgba(168,85,247,0.22) 0%, rgba(168,85,247,0.04) 55%, transparent 72%);
            pointer-events: none;
        }

        .side-brand {
            display: flex;
            align-items: center;
            gap: 14px;
            margin-bottom: 18px;
            padding-bottom: 18px;
            border-bottom: 1px solid rgba(148,163,184,0.14);
            position: relative;
            z-index: 2;
        }

        .side-logo {
            width: 54px;
            height: 54px;
            border-radius: 18px;
            background: linear-gradient(135deg, #38bdf8 0%, #8b5cf6 55%, #ec4899 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 26px;
            box-shadow: 0 14px 35px rgba(139,92,246,0.28);
            flex: 0 0 auto;
        }

        .side-brand-text {
            min-width: 0;
        }

        .side-title {
            font-size: 20px;
            font-weight: 900;
            line-height: 1.05;
            color: #ffffff;
            letter-spacing: 0.2px;
        }

        .side-subtitle {
            margin-top: 6px;
            font-size: 12.5px;
            line-height: 1.55;
            color: #94a3b8;
        }

        .side-section {
            margin: 18px 0 10px 2px;
            font-size: 11px;
            font-weight: 900;
            letter-spacing: 1.8px;
            text-transform: uppercase;
            color: #64748b;
            position: relative;
            z-index: 2;
        }

        div[data-baseweb="radio"] {
            position: relative;
            z-index: 2;
        }

        div.row-widget.stRadio > div {
            gap: 10px;
        }

        div[role="radiogroup"] {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        div[role="radiogroup"] label {
            background: rgba(15, 23, 42, 0.75);
            border: 1px solid rgba(148, 163, 184, 0.12);
            border-radius: 16px;
            padding: 12px 14px;
            transition: all 0.25s ease;
            backdrop-filter: blur(10px);
        }

        div[role="radiogroup"] label:hover {
            transform: translateX(4px);
            border-color: rgba(56, 189, 248, 0.35);
            background: rgba(14, 165, 233, 0.14);
            box-shadow: 0 10px 25px rgba(2, 6, 23, 0.22);
        }

        div[role="radiogroup"] label p {
            font-size: 14px;
            font-weight: 700;
            color: #e2e8f0 !important;
            margin: 0;
        }

        input[type="radio"] + div {
            border-radius: 14px;
        }

        input[type="radio"]:checked + div {
            background: linear-gradient(135deg, rgba(56,189,248,0.26), rgba(139,92,246,0.22)) !important;
            border-radius: 14px;
        }

        div[role="radiogroup"] label > div:first-child {
            display: none !important;
        }

        .side-card {
            margin-top: 18px;
            padding: 16px;
            border-radius: 18px;
            background: linear-gradient(135deg, rgba(56,189,248,0.10), rgba(139,92,246,0.12));
            border: 1px solid rgba(148, 163, 184, 0.14);
            position: relative;
            z-index: 2;
        }

        .side-card-title {
            font-size: 13px;
            font-weight: 900;
            color: #ffffff;
            margin-bottom: 8px;
            letter-spacing: 0.2px;
        }

        .side-card-text {
            font-size: 12px;
            line-height: 1.65;
            color: #cbd5e1;
        }

        .side-mini {
            margin-top: 14px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            position: relative;
            z-index: 2;
        }

        .mini-box {
            padding: 12px 10px;
            border-radius: 16px;
            background: rgba(15,23,42,0.75);
            border: 1px solid rgba(148,163,184,0.12);
            text-align: center;
        }

        .mini-num {
            font-size: 18px;
            font-weight: 900;
            color: #ffffff;
            line-height: 1.1;
        }

        .mini-label {
            margin-top: 4px;
            font-size: 11px;
            color: #94a3b8;
            line-height: 1.2;
        }

        .side-footer {
            margin-top: 16px;
            padding-top: 14px;
            border-top: 1px solid rgba(148,163,184,0.14);
            font-size: 11px;
            color: #64748b;
            line-height: 1.6;
            text-align: center;
            position: relative;
            z-index: 2;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="side-shell">
            <div class="side-brand">
                <div class="side-logo">✦</div>
                <div class="side-brand-text">
                    <div class="side-title">AI Student<br>Impact</div>
                    <div class="side-subtitle">
                        Analyse de l’usage de l’IA, du niveau d’autonomie et du bien-être étudiant.
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="side-section">Navigation</div>', unsafe_allow_html=True)

        page = st.radio(
            "Navigation",
            [
                "🏠 Dashboard",
                "📊 Analytics",
                "🤖 Prediction IA",
                "📁 Dataset"
            ],
            label_visibility="collapsed"
        )

        st.markdown('<div class="side-section">Aperçu</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="side-card">
            <div class="side-card-title">Objectif</div>
            <div class="side-card-text">
                Visualiser l’impact de l’IA sur les performances, l’autonomie, la dépendance
                et l’organisation des étudiants.
            </div>
        </div>

        <div class="side-mini">
            <div class="mini-box">
                <div class="mini-num">4</div>
                <div class="mini-label">Pages</div>
            </div>
            <div class="mini-box">
                <div class="mini-num">AI</div>
                <div class="mini-label">Focus</div>
            </div>
        </div>

       
        </div>
        """, unsafe_allow_html=True)

    return page