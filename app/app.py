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
