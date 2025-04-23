import os
import numpy as np
import joblib
import streamlit as st
import streamlit.components.v1 as components
from dotenv import load_dotenv
from asteroid_profiles import get_asteroid_data

load_dotenv()
DATA_PATH_RAW = os.getenv("DATA_PATH_RAW")

# Load model
model = joblib.load("models/rf_risk_model.pkl")

# Page settings
st.set_page_config(page_title="Deep Impact: Asteroid Risk Predictor", layout="wide", page_icon="☄️")
st.title("☄️ Deep Impact: Asteroid Risk Intelligence Dashboard")
st.markdown(
    """
    <div style='
        background-color: #161b22;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4FC3F7;
        font-size: 16px;
        line-height: 1.6;
        color: #dddddd;
    '>
        <strong>Welcome to Deep Impact</strong> — a machine learning–powered dashboard for analyzing the potential threat posed by Near-Earth Objects (NEOs).
        This tool predicts a kinetic-energy–based risk score using inputs like velocity, magnitude, and diameter, simulating how catastrophic an asteroid would be if it were on a collision course with Earth.
        The project uses real asteroid parameters, physics-based approximations of impact energy, and a trained Random Forest model to classify threat levels ranging from negligible to highly hazardous.
        Use the form below to test out hypothetical asteroid scenarios and compare their outcomes with real celestial objects tracked by NASA. 🌎🛰️ """,
    unsafe_allow_html=True
)

st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

# Tabs
tab1, tab2 = st.tabs(["🛰️ Live Risk Prediction", "📡 Top 5 Asteroid Visuals and Profiles"])

with tab1:
    # Input: shown in meters / m/s
    col1, col2, col3 = st.columns(3)
    with col1:
        velocity_mps = st.number_input("Velocity (m/s)", min_value=0.0, max_value=50000.0, value=15000.0,
                                       help="Speed at which the asteroid is traveling relative to Earth (in meters per second).")
    with col2:
        magnitude = st.number_input("Absolute Magnitude (H)", min_value=10.0, max_value=35.0, value=22.0,
                                    help="Brightness of the asteroid — lower values indicate larger, more reflective bodies.")
    with col3:
        diameter_m = st.number_input("Average Diameter (m)", min_value=10.0, max_value=2000.0, value=100.0,
                                     help="Estimated average physical diameter of the asteroid (in meters).")

    # Convert to km and km/s for model
    velocity_kms = velocity_mps / 1000
    diameter_km = diameter_m / 1000

    # Calculate kinetic energy (proportional proxy)
    kinetic_energy = (diameter_km ** 3) * (velocity_kms ** 2)

    # Manual scaling
    def scale(val, min_val, max_val):
        return (val - min_val) / (max_val - min_val)

    features_scaled = np.array([
        scale(velocity_kms, 0, 40),
        scale(magnitude, 10, 35),
        scale(diameter_km, 0.01, 1.0),
        scale(kinetic_energy, 0, 100)
    ]).reshape(1, -1)

    # Predict risk
    log_risk_score = model.predict(features_scaled)[0]
    predicted_risk = np.expm1(log_risk_score)

    # Interpret risk
    def interpret_risk(score):
        if score < 1e-5:
            return "🟢 Very Low"
        elif score < 1e-3:
            return "🟡 Low"
        elif score < 1e-2:
            return "🟠 Elevated"
        else:
            return "🔴 High"

    risk_category = interpret_risk(predicted_risk)

    # Risk-specific closing line
    risk_conclusions = {
        "🟢 Very Low": "This means the object lacks sufficient mass and velocity to pose any credible danger, even in the event of an Earth-crossing orbit.",
        "🟡 Low": "This means the object is relatively harmless under most scenarios, but should still be observed in case of future orbital shifts or Earth resonance.",
        "🟠 Elevated": "This means the object could become hazardous under the right conditions — such as a shallow atmospheric entry angle or a trajectory leading toward densely populated areas.",
        "🔴 High": "This means that if the object were on a collision course with Earth, it would likely retain enough energy to cause widespread devastation upon impact, especially in vulnerable regions."
    }
    risk_summary_line = risk_conclusions[risk_category]

    # Physics-based explanation
    interpretation = f"""
    Based on the input parameters — a **velocity of {velocity_mps:,.2f} m/s**, an **absolute magnitude of {magnitude:.2f}**, and an **average diameter of {diameter_m:,.2f} meters**, the asteroid’s **kinetic energy** has been estimated using its average size and speed. This results in a predicted **risk score of {predicted_risk:.8f}**, which reflects the potential severity of impact if such an object were heading toward Earth. Given its physical characteristics, this asteroid could carry significant momentum — and depending on its composition, entry angle, and atmospheric interaction, it may either disintegrate or survive entry and cause considerable damage. The object is classified as a **{risk_category}** risk under the assumption of an Earth-impacting orbit. {risk_summary_line}\n\n
    """

    # Display: side by side
    st.markdown("---")
    left, right = st.columns([1, 2])

    with left:
        st.subheader("☄️ Risk Level Classification")
        st.metric("Category", risk_category)
    with right:
        st.subheader("🔭 Risk Assessment")
        st.markdown(interpretation)

    st.markdown("---")
    
    # NASA visual
    intro_col, iframe_col = st.columns([1, 2])

    with intro_col:
        st.markdown("### 🌌 About the Project")
        st.markdown(
            """
            Welcome to **Deep Impact** — a machine learning–powered dashboard for analyzing the potential threat posed by Near-Earth Objects (NEOs).  

            This tool predicts a kinetic-energy–based risk score using inputs like velocity, magnitude, and diameter, simulating how catastrophic an asteroid would be **if** it were on a collision course with Earth.  

            The project uses real asteroid parameters, physics-based approximations of impact energy, and a trained Random Forest model to classify threat levels ranging from negligible to highly hazardous.  

            Use the form above to test out various hypothetical asteroid scenarios and compare their outcomes with real celestial objects tracked by NASA.
            """
        )

    with iframe_col:
        components.iframe("https://eyes.nasa.gov/apps/asteroids/#/watch/", height=700)

    st.markdown("---")
    

with tab2:
    asteroid_data = get_asteroid_data()
    for i, asteroid in enumerate(asteroid_data):
        col1, col2 = st.columns(2)

        if i % 2 == 0:
            with col1:
                components.iframe(f"https://eyes.nasa.gov/apps/asteroids/#/{asteroid['slug']}", height=500)
            with col2:
                st.markdown(f"### 🛰️ Asteroid Profile: **{asteroid['name']}**")
                st.markdown(f"<div style='text-align: justify; line-height: 1.6;'>{asteroid['desc']}</div>", unsafe_allow_html=True)

        else:
            with col1:
                st.markdown(f"### 🛰️ Asteroid Profile: **{asteroid['name']}**")
                st.markdown(f"<div style='text-align: justify; line-height: 1.6;'>{asteroid['desc']}</div>", unsafe_allow_html=True)
            with col2:
                components.iframe(f"https://eyes.nasa.gov/apps/asteroids/#/{asteroid['slug']}", height=500)

        st.markdown("---")
