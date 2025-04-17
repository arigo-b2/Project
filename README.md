## 🌍 Deep Impact: Machine Learning–Powered Asteroid Collision Risk Analyser

### 🌍 Overview
This project uses NASA's Near Earth Object (NEO) data to build a machine learning model that predicts the risk level of an asteroid based on its physical and orbital characteristics. It uses classification techniques to determine whether an asteroid poses a potential threat and optionally estimates the threat level using the Torino Impact Hazard Scale.

### 🚀 Objective
To classify and score the risk of asteroids colliding with Earth using supervised learning, with outputs inspired by the [Torino Scale](https://cneos.jpl.nasa.gov/sentry/torino_scale.html). The app can simulate asteroid entries and visualize the predicted threat.


### 📊 About the Torino Scale
The [Torino Impact Hazard Scale](https://cneos.jpl.nasa.gov/sentry/torino_scale.html) is a 0–10 scale used by astronomers to communicate the risk of an asteroid or comet impacting Earth.

| Level | Description            | Meaning                                                                 |
|-------|------------------------|-------------------------------------------------------------------------|
| 0     | No hazard              | Chance of collision is zero or effectively zero.                       |
| 1     | Normal                 | Regular monitoring, but no cause for public concern.                   |
| 2–4   | Merits attention       | Close approaches; needs more observation.                              |
| 5–7   | Threatening            | Significant risk; public and government attention is warranted.        |
| 8–10  | Certain collisions     | Likely or certain impacts with potential for regional to global damage.|

In this project, a proxy Torino score is derived from a combination of estimated kinetic energy and miss distance. The score is categorized into levels resembling the Torino scale, and can be visualized in the Streamlit dashboard.

### 📁 Current Features
- Fetches asteroid data from NASA NeoWs API
- Cleans and flattens nested JSON into tabular format
- Supports Excel export of raw asteroid data
- Designed to estimate risk level using features like diameter, velocity, and distance

### 📊 Technologies & Tools

- **Python**
- **Pandas** & **NumPy**: for data handling
- **Scikit-learn**: for machine learning models (Logistic Regression, Random Forest)
- **Streamlit**: for building an interactive dashboard
- **NASA NEO API**: for real-time and historical asteroid data

### 🧠 In Progress
- Feature engineering: velocity, kinetic energy, scaled distances
- Model training and evaluation (classification or risk scoring)
- Streamlit dashboard with Torino scale visual and live predictions

### 🛰️ Credits

Developed as part of an independent project to explore AI for planetary defense.  
Data provided by NASA's Near-Earth Object Program.
