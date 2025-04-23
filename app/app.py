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

