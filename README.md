## 🌍 TrajectoryAI: Forecasting Asteroid-Earth Approaches with Machine Learning

### 🌍 Overview
This project uses NASA's Near Earth Object (NEO) data to build a machine learning model that predicts **how close an asteroid will come to Earth** based on its physical and orbital characteristics. The model estimates the asteroid's **miss distance** (in kilometers) using supervised regression, enabling better understanding of NEO behavior and potential near-Earth threats.


### 🚀 Objective
To predict the **closest approach distance** of asteroids using machine learning. The model is trained on real NASA data using features like size, speed, brightness, and derived kinetic energy to estimate the proximity of asteroids to Earth. The project aims to support proactive risk analysis and threat assessment.


### 📏 Why Miss Distance?
The **miss distance** (`miss_distance_km`) represents how close a NEO comes to Earth during its approach. This distance, when combined with speed and size, helps determine the severity of potential encounters. By learning to estimate miss distance, the model offers insights into:
- Which asteroids might come unusually close
- How early-stage NEO observations relate to final approach behavior

### 📁 Current Features
- Fetches and processes raw asteroid data using the NASA NeoWs API
- Calculates physical proxies like average diameter and kinetic energy
- Builds a machine learning–ready dataset for regression
- Predicts miss distance based on NEO features

### 📊 Technologies & Tools

- **Python**
- **Pandas** & **NumPy**: for data handling
- **Scikit-learn**: for machine learning models (Random Forest Regressor)
- **Streamlit**: for building an interactive dashboard
- **NASA NEO API**: for real-time and historical asteroid data

### 🧠 In Progress
- Feature engineering: velocity, brightness, kinetic energy
- Model evaluation (MAE, RMSE, R²)
- Visualizations: predicted vs actual proximity
- Streamlit app for interactive asteroid input and prediction

### 🛰️ Credits
Developed as part of an independent project to explore AI for planetary defense.  
Data provided by NASA's Near-Earth Object Program.
