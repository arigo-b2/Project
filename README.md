## ☄️ Deep Impact: Machine Learning–Powered Asteroid Collision Risk Analyser

### 🌍 Overview

This project uses real-world NASA Near-Earth Object (NEO) data to build a machine learning model that estimates the threat level posed by asteroids approaching Earth. Using physics-inspired features such as kinetic energy, brightness, and estimated diameter, the model predicts a log-transformed threat score representing potential impact severity.

### 🧠 Current Features
- Collects and processes real asteroid data using the NASA NeoWs API
- Engineers physics-aware features such as kinetic energy and average size
- Builds a machine learning–ready dataset with scaled inputs and log-transformed risk targets
- Trains a Random Forest Regressor to predict asteroid threat levels
- Evaluates model using MAE, RMSE, and R² (achieving R² ≈ 0.95 on unseen data)


### 📊 Technologies & Tools

- **Python**
- **Pandas** & **NumPy**: for data preprocessing and analysis
- **Scikit-learn**: for machine learning modeling
- **Streamlit**: for planned deployment of a threat assessment dashboard
- **NASA NEO API**: for real-time and historical asteroid data


### 🧠 In Progress
- Interactive dashboard for threat score predictions
- Model interpretability (feature importance)
- Option to simulate hypothetical asteroid input for risk estimation
- Visual charts for predicted vs actual threat behavior

---

### 🛰️ Credits
Developed as part of an independent project to explore AI for planetary defense.  
Data provided by NASA's Near-Earth Object Program.
