## ☄️ Deep Impact: Machine Learning–Powered Asteroid Collision Risk Analyser

### 🌍 Overview

This project uses real-world NASA Near-Earth Object (NEO) data to build a machine learning model that estimates the threat level posed by asteroids approaching Earth. Using physics-inspired features such as kinetic energy, brightness, and estimated diameter, the model predicts a log-transformed threat score representing potential impact severity.

### 🧠 Core Features
- **Data Collection**: Fetches real asteroid datasets from the NASA Near Earth Object (NeoWs) API
- **Feature Engineering**: Computes physics-inspired attributes such as:
    - Kinetic energy (volume × velocity²)
    - Scaled Absolute Magnitude
    - Normalized asteroid size
- **Risk Prediction Model**:
    - Trains a Random Forest Regressor
    - Predicts a log-transformed threat score representing impact severity
- **Model Performance**:
    - Evaluated using MAE, RMSE, and R²
    - Achieved R² ≈ 0.95 on unseen data
- **Interactive Dashboard**:
    - Enter custom asteroid parameters (velocity, magnitude, diameter)
    - Receive real-time risk classification
    - Explore detailed profiles of notable asteroids tracked by NASA

### 📊 Technologies & Tools

- **Python**
- **Pandas** & **NumPy**: for data preprocessing and analysis
- **Scikit-learn**: for machine learning modeling
- **Streamlit**: for planned deployment of a threat assessment dashboard
- **NASA NEO API**: for real-time and historical asteroid data

---

### 🛰️ Credits
Developed as part of an independent project to explore AI for planetary defense.  
Data provided by NASA's Near-Earth Object API.
