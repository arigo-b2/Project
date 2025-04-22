import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit.components.v1 as components

# Load model
model = joblib.load("models/rf_risk_model.pkl")

# Page settings
st.set_page_config(page_title="Deep Impact: Asteroid Risk Predictor", layout="wide", page_icon="☄️")
st.title("☄️ Deep Impact: Asteroid Threat Intelligence Dashboard")

st.markdown("Use machine learning to estimate the potential threat of a Near-Earth Object (NEO) based on its physical parameters.")

# Tabs for dashboard sections
tab1, tab2 = st.tabs(["🛰️ Live Prediction", "📊 Risk Explorer"])

with tab1:
    st.header("🚀 Enter Asteroid Parameters")
    col1, col2, col3 = st.columns(3)

    with col1:
        velocity = st.number_input("Velocity (km/s)", 0.0, 50.0, 15.0)
    with col2:
        magnitude = st.number_input("Absolute Magnitude (H)", 10.0, 35.0, 22.0)
    with col3:
        diameter = st.number_input("Average Diameter (km)", 0.01, 2.0, 0.1)

    # Calculate kinetic energy
    kinetic_energy = (diameter ** 3) * (velocity ** 2)

    # Manual scaling (based on training)
    def scale(val, min_val, max_val):
        return (val - min_val) / (max_val - min_val)

    features_scaled = np.array([
        scale(velocity, 0, 40),
        scale(magnitude, 10, 35),
        scale(diameter, 0.01, 1.0),
        scale(kinetic_energy, 0, 100)
    ]).reshape(1, -1)

    # Predict
    log_risk_score = model.predict(features_scaled)[0]
    predicted_risk = np.expm1(log_risk_score)

    # Risk interpretation
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

    st.markdown("---")
    st.subheader("📊 Predicted Risk Score")
    st.metric("Risk Score", f"{predicted_risk:.8f}")
    st.markdown(f"**Threat Level:** {risk_category}")

    # Visual interpretation
    st.markdown("### 🌌 NASA Asteroid 3D Viewer")
    components.iframe("https://eyes.nasa.gov/apps/asteroids/#/", height=500)

with tab2:
    st.header("📊 Explore Sample Risk Scores")

    sample_scores = [predicted_risk, 1e-6, 1e-3, 1e-2]
    labels = ["Your Input", "Safe Object", "Close Call", "High Risk"]

    fig, ax = plt.subplots()
    sns.barplot(x=labels, y=sample_scores, palette=["orange", "green", "yellow", "red"], ax=ax)
    ax.set_ylabel("Risk Score (Proxy)")
    ax.set_title("Risk Score Comparison")
    st.pyplot(fig)

    with st.expander("📘 About the Torino Scale"):
        st.markdown("""
        The [Torino Scale](https://cneos.jpl.nasa.gov/sentry/torino_scale.html) is a 0–10 scale used by astronomers to communicate asteroid impact risk:
        - 0 = No hazard
        - 2–4 = Merits attention
        - 5–7 = Threatening
        - 8–10 = Certain collision
        This model uses a proxy risk score based on physical energy and miss distance.
        """)