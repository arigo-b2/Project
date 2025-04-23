import streamlit as st
import numpy as np
import joblib
import streamlit.components.v1 as components

# Load model
model = joblib.load("models/rf_risk_model.pkl")

# Page settings
st.set_page_config(page_title="Deep Impact: Asteroid Risk Predictor", layout="wide", page_icon="☄️")

# Title and description
st.title("☄️ Deep Impact: Asteroid Threat Intelligence Dashboard")
st.markdown("Use machine learning to estimate the potential threat of a Near-Earth Object (NEO) based on its physical parameters.")
# Main content
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

# Manual scaling
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

# Display prediction
st.markdown("---")
st.subheader("📊 Predicted Risk Score")
st.metric("Risk Score", f"{predicted_risk:.8f}")
st.markdown(f"**Threat Level:** {risk_category}")

# NASA visual
st.markdown("### 🌌 NASA Asteroid 3D Viewer")
components.iframe("https://eyes.nasa.gov/apps/asteroids/#/watch/", height=700)

# Side-by-side NASA Eyes Views
st.markdown("### 🌌 Asteroid Views")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**🌠 Asteroid 2025 BP6 Close Approach**")
    components.iframe(
        "https://eyes.nasa.gov/apps/asteroids/#/2025_bp6?time=2025-01-25T23:27:43.516+00:00&rate=1",
        height=600
    )

with col2:
    st.markdown("**🌎 Planet Earth**")
    components.iframe(
        "https://eyes.nasa.gov/apps/asteroids/#/planets/earth",
        height=600
    )

