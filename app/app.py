import streamlit as st
import numpy as np
import joblib
import streamlit.components.v1 as components

# Load model
model = joblib.load("models/rf_risk_model.pkl")

# Page settings
st.set_page_config(page_title="Deep Impact: Asteroid Risk Predictor", layout="wide", page_icon="☄️")
st.title("☄️ Deep Impact: Asteroid Risk Intelligence Dashboard")
st.markdown("Use machine learning to estimate the potential risk of a Near-Earth Object (NEO) based on its physical parameters.")

# Tabs
tab1, tab2 = st.tabs(["🛰️ Live Risk Prediction", "📡 Top 10 Asteroid Visuals and Profiles"])

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
    Based on the input parameters — a **velocity of {velocity_mps:,.2f} m/s**, an **absolute magnitude of {magnitude:.2f}**, and an **average diameter of {diameter_m:,.2f} meters**, the asteroid’s **kinetic energy** (proportional to volume × velocity²) has been estimated using its average size and speed. This results in a predicted **risk score of {predicted_risk:.8f}**, which reflects the potential severity of impact if such an object were heading toward Earth. Given its physical characteristics, this asteroid could carry significant momentum — and depending on its composition, entry angle, and atmospheric interaction, it may either disintegrate or survive entry and cause considerable damage. The object is classified as a **{risk_category}** risk under the assumption of an Earth-impacting orbit. {risk_summary_line}
    """

    # Display: side by side
    st.markdown("---")
    left, right = st.columns([1, 4])
    with left:
        st.subheader("☄️ Risk Level")
        st.metric("Classification", risk_category)
    with right:
        st.subheader("🔭 Risk Assessment")
        st.markdown(interpretation)
