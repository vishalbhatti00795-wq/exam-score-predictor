
import os
import pickle
import warnings

import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

warnings.filterwarnings("ignore")

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="EXAMAI | Exam Score Predictor",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# CUSTOM CSS — PREMIUM BLACK + CRIMSON RED
# ============================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

    :root {
        --black: #050505;
        --black-2: #0b0b0b;
        --card: #111111;
        --card-2: #151515;
        --border: #292929;
        --red: #e5092f;
        --red-dark: #b3001b;
        --muted: #a7a7a7;
        --white: #ffffff;
    }

    * { font-family: 'Inter', sans-serif; }

    .stApp {
        background:
            radial-gradient(circle at 8% 5%, rgba(229,9,47,.13), transparent 25%),
            radial-gradient(circle at 92% 18%, rgba(179,0,27,.10), transparent 24%),
            linear-gradient(180deg, #050505 0%, #080808 55%, #050505 100%);
        color: var(--white);
    }

    [data-testid="stHeader"] {
        background: rgba(5,5,5,.78);
        backdrop-filter: blur(14px);
    }

    [data-testid="stMainBlockContainer"] {
        max-width: 1450px;
        padding-top: 1.2rem;
        padding-bottom: 3rem;
    }

    /* Hide Streamlit chrome */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    [data-testid="stToolbar"] { visibility: hidden; }

    /* Header */
    .topbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 14px 0 20px 0;
        border-bottom: 1px solid rgba(255,255,255,.07);
        margin-bottom: 25px;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .brand-mark {
        width: 42px;
        height: 42px;
        border-radius: 13px;
        display: grid;
        place-items: center;
        font-size: 19px;
        font-weight: 900;
        background: linear-gradient(145deg, #f21c43, #8e0018);
        box-shadow: 0 0 28px rgba(229,9,47,.32);
    }

    .brand-name {
        font-size: 20px;
        font-weight: 900;
        letter-spacing: 1.5px;
        line-height: 1;
    }

    .brand-sub {
        color: #929292;
        font-size: 11px;
        margin-top: 4px;
    }

    .nav {
        display: flex;
        gap: 28px;
        align-items: center;
        color: #a9a9a9;
        font-size: 13px;
        font-weight: 600;
    }

    .nav span:first-child { color: #fff; }

    .status {
        display: inline-flex;
        align-items: center;
        gap: 7px;
        border: 1px solid rgba(229,9,47,.35);
        background: rgba(229,9,47,.07);
        color: #ff4966;
        padding: 8px 12px;
        border-radius: 999px;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: .7px;
    }

    .pulse {
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background: #ff294e;
        box-shadow: 0 0 10px #ff294e;
    }

    /* Hero */
    .hero {
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255,255,255,.07);
        border-radius: 28px;
        padding: 52px 52px 48px;
        background:
            linear-gradient(135deg, rgba(229,9,47,.12), transparent 48%),
            linear-gradient(180deg, rgba(255,255,255,.035), rgba(255,255,255,.012));
        box-shadow: inset 0 1px rgba(255,255,255,.04), 0 20px 70px rgba(0,0,0,.35);
    }

    .hero:after {
        content: "";
        position: absolute;
        width: 380px;
        height: 380px;
        right: -130px;
        top: -190px;
        border-radius: 50%;
        background: rgba(229,9,47,.16);
        filter: blur(85px);
    }

    .eyebrow {
        display: inline-block;
        border: 1px solid rgba(229,9,47,.35);
        background: rgba(229,9,47,.08);
        color: #ff4b68;
        padding: 8px 13px;
        border-radius: 999px;
        font-size: 10px;
        font-weight: 800;
        letter-spacing: 1.4px;
    }

    .hero h1 {
        font-size: clamp(38px, 5vw, 68px);
        line-height: 1.02;
        letter-spacing: -2.8px;
        margin: 20px 0 16px;
        max-width: 800px;
        font-weight: 900;
    }

    .hero h1 span { color: var(--red); }

    .hero p {
        color: #a9a9a9;
        font-size: 16px;
        line-height: 1.75;
        max-width: 720px;
        margin: 0;
    }

    /* Cards */
    .section-title {
        font-size: 21px;
        font-weight: 800;
        margin: 32px 0 4px;
    }

    .section-sub {
        color: #858585;
        font-size: 12px;
        margin-bottom: 17px;
    }

    .card {
        background: linear-gradient(145deg, rgba(255,255,255,.035), rgba(255,255,255,.012));
        border: 1px solid rgba(255,255,255,.08);
        border-radius: 22px;
        padding: 24px;
        box-shadow: 0 18px 50px rgba(0,0,0,.23);
    }

    .card-title {
        font-size: 17px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .card-subtitle {
        color: #818181;
        font-size: 12px;
        margin-bottom: 22px;
    }

    .mini-label {
        color: #8f8f8f;
        text-transform: uppercase;
        font-size: 9px;
        font-weight: 800;
        letter-spacing: 1.4px;
        margin: 19px 0 10px;
    }

    /* Streamlit widgets */
    label, [data-testid="stWidgetLabel"] p {
        color: #d5d5d5 !important;
        font-weight: 600 !important;
        font-size: 12px !important;
    }

    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div {
        background: #101010 !important;
        border-color: #2c2c2c !important;
        border-radius: 12px !important;
    }

    div[data-baseweb="select"] > div:hover,
    div[data-baseweb="input"] > div:hover {
        border-color: rgba(229,9,47,.55) !important;
    }

    input, textarea {
        color: #fff !important;
    }

    [data-testid="stSlider"] [role="slider"] {
        background: var(--red) !important;
    }

    .stButton > button {
        width: 100%;
        min-height: 52px;
        border: 0 !important;
        border-radius: 14px !important;
        color: white !important;
        font-weight: 800 !important;
        letter-spacing: .3px;
        background: linear-gradient(135deg, #ed1238, #a8001c) !important;
        box-shadow: 0 12px 35px rgba(229,9,47,.22);
        transition: .2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 42px rgba(229,9,47,.34);
    }

    /* Result */
    .result-card {
        min-height: 430px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        background:
            radial-gradient(circle at 50% 30%, rgba(229,9,47,.14), transparent 42%),
            linear-gradient(145deg, #111111, #090909);
        border: 1px solid rgba(229,9,47,.25);
        border-radius: 24px;
        box-shadow: 0 0 60px rgba(229,9,47,.08);
    }

    .result-kicker {
        color: #ff4865;
        font-size: 10px;
        font-weight: 900;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .score {
        font-size: 82px;
        line-height: 1;
        font-weight: 900;
        letter-spacing: -4px;
        margin: 15px 0 4px;
        text-shadow: 0 0 35px rgba(229,9,47,.24);
    }

    .score small {
        font-size: 18px;
        letter-spacing: 0;
        color: #777;
        font-weight: 600;
    }

    .category {
        display: inline-block;
        margin-top: 10px;
        padding: 9px 17px;
        border-radius: 999px;
        background: rgba(229,9,47,.1);
        border: 1px solid rgba(229,9,47,.32);
        color: #ff4966;
        font-size: 12px;
        font-weight: 800;
    }

    .explanation {
        max-width: 470px;
        color: #919191;
        font-size: 12px;
        line-height: 1.7;
        margin: 15px auto 0;
    }

    /* KPI cards */
    .kpi {
        background: #101010;
        border: 1px solid #252525;
        border-radius: 17px;
        padding: 17px;
        min-height: 95px;
    }

    .kpi-label {
        color: #777;
        font-size: 9px;
        text-transform: uppercase;
        letter-spacing: 1.1px;
        font-weight: 800;
    }

    .kpi-value {
        font-size: 20px;
        font-weight: 800;
        margin-top: 8px;
    }

    .kpi-value.red { color: #ff3d5d; }

    .metric-card {
        text-align: center;
        background: #101010;
        border: 1px solid #252525;
        border-radius: 17px;
        padding: 18px 10px;
    }

    .metric-value {
        font-size: 23px;
        font-weight: 900;
        color: #fff;
    }

    .metric-label {
        color: #777;
        font-size: 9px;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 5px;
    }

    /* Footer */
    .footer {
        margin-top: 45px;
        padding-top: 22px;
        border-top: 1px solid rgba(255,255,255,.07);
        text-align: center;
        color: #656565;
        font-size: 10px;
        line-height: 1.8;
    }

    .footer strong { color: #bdbdbd; }

    @media (max-width: 850px) {
        .hero { padding: 35px 25px; }
        .nav { display: none; }
        .hero h1 { letter-spacing: -1.7px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# MODEL LOADING
# ============================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "best_xgb_model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "label_encoders.pkl")


@st.cache_resource
def load_artifacts():
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    with open(ENCODER_PATH, "rb") as f:
        encoders = pickle.load(f)

    return model, encoders


# ============================================================
# HELPERS
# ============================================================
def performance_category(score):
    if score >= 90:
        return "Outstanding", "Exceptional predicted academic performance."
    if score >= 80:
        return "Excellent", "The model predicts strong academic performance."
    if score >= 70:
        return "Good", "The model predicts a solid academic performance."
    if score >= 60:
        return "Average", "The model predicts moderate academic performance."
    return "Needs Improvement", "The model predicts room for improvement in expected performance."


def make_gauge(score):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            number={
                "font": {"size": 42, "color": "white"},
                "suffix": "",
            },
            gauge={
                "axis": {
                    "range": [0, 100],
                    "tickwidth": 0,
                    "tickcolor": "rgba(0,0,0,0)",
                    "tickfont": {"color": "#666"},
                },
                "bar": {"color": "#e5092f", "thickness": 0.22},
                "bgcolor": "#1a1a1a",
                "borderwidth": 0,
                "steps": [
                    {"range": [0, 100], "color": "#151515"},
                ],
            },
            domain={"x": [0.08, 0.92], "y": [0.05, 0.95]},
        )
    )
    fig.update_layout(
        height=255,
        margin=dict(l=10, r=10, t=10, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        font={"color": "white"},
    )
    return fig


# ============================================================
# HEADER
# ============================================================
st.markdown(
    """
    <div class="topbar">
        <div class="brand">
            <div class="brand-mark">E</div>
            <div>
                <div class="brand-name">EXAMAI</div>
                <div class="brand-sub">AI-Powered Exam Score Predictor</div>
            </div>
        </div>
        <div class="nav">
            <span>Dashboard</span>
            <span>Prediction</span>
            <span>About Model</span>
            <span class="status"><i class="pulse"></i> MODEL ONLINE</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# HERO
# ============================================================
st.markdown(
    """
    <section class="hero">
        <div class="eyebrow">XGBOOST &nbsp;•&nbsp; MACHINE LEARNING &nbsp;•&nbsp; PREDICTIVE ANALYTICS</div>
        <h1>Predict Your Exam Score<br>with <span>AI.</span></h1>
        <p>
            Analyze academic, attendance, lifestyle, and learning-environment factors
            to estimate exam performance using a tuned XGBoost regression model.
        </p>
    </section>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# LOAD MODEL
# ============================================================
try:
    model, encoders = load_artifacts()
except FileNotFoundError:
    st.error(
        "Model files not found. Place `best_xgb_model.pkl` and `label_encoders.pkl` "
        "in the same folder as `app.py`."
    )
    st.stop()
except Exception as e:
    st.error(f"Unable to load the model artifacts: {type(e).__name__}.")
    st.stop()

# Exact features used by the saved XGBoost model
FEATURES = [
    "study_hours",
    "class_attendance",
    "sleep_hours",
    "sleep_quality",
    "study_method",
    "facility_rating",
]

# Confirm the saved model's expected feature names where available.
if hasattr(model, "feature_names_in_"):
    FEATURES = list(model.feature_names_in_)

# ============================================================
# PREDICTION FORM
# ============================================================
st.markdown('<div class="section-title">Student Prediction</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-sub">Enter the factors used by the trained model to generate an estimated score.</div>',
    unsafe_allow_html=True,
)

left, right = st.columns([1.03, 0.97], gap="large")

with left:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">Student Profile</div>
            <div class="card-subtitle">Provide the student's current academic and lifestyle information.</div>
            <div class="mini-label">Academic Factors</div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2)
    with c1:
        study_hours = st.slider(
            "Study Hours / Day",
            min_value=0.0,
            max_value=24.0,
            value=5.0,
            step=0.5,
            help="Average number of hours spent studying per day.",
        )
    with c2:
        attendance = st.slider(
            "Class Attendance (%)",
            min_value=0.0,
            max_value=100.0,
            value=80.0,
            step=1.0,
        )

    st.markdown('<div class="mini-label">Lifestyle</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        sleep_hours = st.slider(
            "Sleep Hours / Night",
            min_value=0.0,
            max_value=16.0,
            value=7.0,
            step=0.5,
        )
    with c2:
        sleep_quality = st.selectbox(
            "Sleep Quality",
            options=list(encoders["sleep_quality"].classes_),
            index=list(encoders["sleep_quality"].classes_).index("good")
            if "good" in encoders["sleep_quality"].classes_
            else 0,
        )

    st.markdown('<div class="mini-label">Learning Environment</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        study_method = st.selectbox(
            "Study Method",
            options=list(encoders["study_method"].classes_),
            index=list(encoders["study_method"].classes_).index("self-study")
            if "self-study" in encoders["study_method"].classes_
            else 0,
        )
    with c2:
        facility_rating = st.selectbox(
            "Facility Rating",
            options=list(encoders["facility_rating"].classes_),
            index=list(encoders["facility_rating"].classes_).index("medium")
            if "medium" in encoders["facility_rating"].classes_
            else 0,
        )

    st.markdown("</div>", unsafe_allow_html=True)
    predict_clicked = st.button("⚡  PREDICT EXAM SCORE", use_container_width=True)

with right:
    if predict_clicked:
        try:
            # Encode only the categorical variables actually used by the trained model.
            encoded_sleep_quality = encoders["sleep_quality"].transform([sleep_quality])[0]
            encoded_study_method = encoders["study_method"].transform([study_method])[0]
            encoded_facility_rating = encoders["facility_rating"].transform([facility_rating])[0]

            input_data = pd.DataFrame(
                [[
                    study_hours,
                    attendance,
                    sleep_hours,
                    encoded_sleep_quality,
                    encoded_study_method,
                    encoded_facility_rating,
                ]],
                columns=FEATURES,
            )

            prediction = float(model.predict(input_data)[0])
            prediction = float(np.clip(prediction, 0, 100))
            category, explanation = performance_category(prediction)

            st.session_state["prediction"] = prediction
            st.session_state["category"] = category
            st.session_state["explanation"] = explanation
            st.session_state["input_data"] = input_data.copy()
            st.session_state["raw_inputs"] = {
                "Study Hours": study_hours,
                "Attendance": attendance,
                "Sleep Hours": sleep_hours,
                "Sleep Quality": sleep_quality,
                "Study Method": study_method,
                "Facility Rating": facility_rating,
            }

        except Exception:
            st.error(
                "Prediction could not be generated because the supplied values do not "
                "match the saved model's preprocessing configuration."
            )

    if "prediction" not in st.session_state:
        st.markdown(
            """
            <div class="result-card">
                <div class="result-kicker">AI Prediction</div>
                <div style="font-size:30px;font-weight:800;margin-top:14px;">Ready to analyze</div>
                <div class="explanation">
                    Enter the student information and click
                    <b style="color:#ddd;">Predict Exam Score</b> to generate
                    an AI-powered estimate.
                </div>
                <div style="margin-top:26px;color:#555;font-size:38px;">◎</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        prediction = st.session_state["prediction"]
        category = st.session_state["category"]
        explanation = st.session_state["explanation"]

        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-kicker">Predicted Exam Score</div>
                <div class="score">{prediction:.1f} <small>/ 100</small></div>
                <div class="category">{category}</div>
                <div class="explanation">{explanation}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.plotly_chart(make_gauge(prediction), use_container_width=True, config={"displayModeBar": False})

# ============================================================
# POST-PREDICTION SECTIONS
# ============================================================
if "prediction" in st.session_state:
    st.markdown('<div class="section-title">Prediction Breakdown</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">A quick view of the profile submitted to the model.</div>',
        unsafe_allow_html=True,
    )

    raw = st.session_state["raw_inputs"]
    cols = st.columns(6)
    cards = [
        ("Study Hours", f"{raw['Study Hours']:.1f} hrs"),
        ("Attendance", f"{raw['Attendance']:.0f}%"),
        ("Sleep", f"{raw['Sleep Hours']:.1f} hrs"),
        ("Sleep Quality", str(raw["Sleep Quality"]).title()),
        ("Study Method", str(raw["Study Method"]).title()),
        ("Facility", str(raw["Facility Rating"]).title()),
    ]

    for col, (label, value) in zip(cols, cards):
        with col:
            st.markdown(
                f"""
                <div class="kpi">
                    <div class="kpi-label">{label}</div>
                    <div class="kpi-value">{value}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# ============================================================
# MODEL INFORMATION
# ============================================================
st.markdown('<div class="section-title">About the AI Model</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-sub">The application uses the saved tuned model from the project notebook.</div>',
    unsafe_allow_html=True,
)

m1, m2, m3, m4 = st.columns(4)

metrics = [
    ("Algorithm", "XGBoost"),
    ("Task", "Regression"),
    ("Best R²", "0.7290"),
    ("RMSE", "9.8454"),
]

for col, (label, value) in zip([m1, m2, m3, m4], metrics):
    with col:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-value">{value}</div>
                <div class="metric-label">{label}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    """
    <div style="height:10px"></div>
    <div class="card">
        <div class="card-title">Best Model Configuration</div>
        <div class="card-subtitle">
            Selected through 3-fold GridSearchCV in the project notebook.
        </div>
    """,
    unsafe_allow_html=True,
)

p1, p2, p3, p4 = st.columns(4)
params = [
    ("Learning Rate", "0.05"),
    ("Max Depth", "3"),
    ("Estimators", "300"),
    ("Subsample", "0.8"),
]
for col, (label, value) in zip([p1, p2, p3, p4], params):
    with col:
        st.markdown(
            f"""
            <div class="kpi">
                <div class="kpi-label">{label}</div>
                <div class="kpi-value red">{value}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# FEATURE IMPORTANCE
# ============================================================
if hasattr(model, "feature_importances_"):
    st.markdown('<div class="section-title">What Influences the Prediction?</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">Feature importance extracted directly from the saved XGBoost model.</div>',
        unsafe_allow_html=True,
    )

    importance_df = pd.DataFrame({
        "Feature": FEATURES,
        "Importance": model.feature_importances_,
    }).sort_values("Importance", ascending=True)

    importance_df["Feature"] = (
        importance_df["Feature"]
        .str.replace("_", " ")
        .str.title()
    )

    fig = px.bar(
        importance_df,
        x="Importance",
        y="Feature",
        orientation="h",
        text="Importance",
    )
    fig.update_traces(
        marker_color="#e5092f",
        texttemplate="%{text:.1%}",
        textposition="outside",
        cliponaxis=False,
    )
    fig.update_layout(
        height=370,
        margin=dict(l=10, r=55, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#bdbdbd", family="Inter"),
        xaxis=dict(
            showgrid=True,
            gridcolor="rgba(255,255,255,.06)",
            zeroline=False,
            tickformat=".0%",
            title="Relative Importance",
        ),
        yaxis=dict(title="", tickfont=dict(size=11)),
    )
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

# ============================================================
# FOOTER
# ============================================================
st.markdown(
    """
    <div class="footer">
        <strong>EXAMAI</strong> · AI-powered academic performance prediction<br>
        Built with Python · Streamlit · XGBoost<br>
        Predictions are estimates generated by a machine learning model and should
        not be considered guaranteed exam results.
    </div>
    """,
    unsafe_allow_html=True,
)
