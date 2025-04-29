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
st.title("🌎 Deep Impact: Asteroid Risk Intelligence Dashboard")
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
    <strong>Welcome to Deep Impact</strong> — a machine learning powered dashboard for analyzing the potential threat posed by asteroids.
    This tool estimates a kinetic-energy–based risk score using user-provided inputs such as velocity, absolute magnitude, and diameter — simulating the projected impact effects of an asteroid assuming a direct Earth-bound trajectory. The model leverages real-world asteroid data, applies physics-based impact estimations, and uses a trained Random Forest regressor to classify the object into intuitive threat levels ranging from negligible to highly hazardous.
    Use the form below to experiment with hypothetical asteroid scenarios and explore how their impact profiles compare to those of real NEOs monitored by NASA. ☄️🛰️

    """,
    unsafe_allow_html=True
)

st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3 = st.tabs(["🛰️ Live Risk Prediction", "📡 Top 5 Asteroid Visuals and Profiles", "🌌 About the Project"])

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

    # Custom risk-specific interpretation line
    risk_physics_interpretation = {
        "🟢 Very Low": "Given its relatively low velocity and small diameter, this asteroid would likely be unable to penetrate the Earth's atmosphere. It would lose most of its energy to atmospheric drag and disintegrate at high altitudes, posing minimal risk to ground-level infrastructure or life.",
        "🟡 Low": "With modest size and velocity, this asteroid may partially survive atmospheric entry, but would likely fragment at high altitudes due to thermal stress and pressure differences. While it could produce a small airburst or sonic boom, the likelihood of ground impact or substantial damage remains very low.",
        "🟠 Elevated": "Due to its larger size and kinetic energy, this asteroid could survive atmospheric entry, especially if composed of dense materials like metal or rock. Upon entry, it might decelerate but remain intact enough to reach the ground, causing localized impact effects such as shockwaves, crater formation, or structural damage in populated zones. Its threat potential increases significantly if its entry angle is shallow or its trajectory intersects urban regions.",
        "🔴 High": "This asteroid possesses substantial mass and velocity, making it capable of withstanding intense aerodynamic heating during atmospheric entry. Its kinetic energy would be largely retained upon descent, allowing it to impact the Earth's surface with catastrophic force. Depending on the location and composition, it could lead to regional-scale destruction, including shockwaves, thermal radiation, fires, and long-lasting environmental effects."
    }

    # Combine everything into the final interpretation
    risk_summary_line = risk_conclusions[risk_category]
    risk_interpretation = risk_physics_interpretation[risk_category]

    # Physics-based explanation
    interpretation = f"""
    Based on the input parameters — a **velocity of {velocity_mps:,.2f} m/s**, an **absolute magnitude of {magnitude:.2f}**, and an **average diameter of {diameter_m:,.2f} meters**, the asteroid’s **kinetic energy** has been estimated using its average size and speed. This results in a predicted **risk score of {predicted_risk:.8f}**, which reflects the potential severity of impact if such an object were heading toward Earth. {risk_interpretation} The object is classified as a **{risk_category}** risk under the assumption of an Earth-impacting orbit. {risk_summary_line}\n\n
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
    st.markdown("### 🌌 NASA Interactive 3D Viewer: Visualising the Next Five Closest Asteroid Flybys")
    components.iframe("https://eyes.nasa.gov/apps/asteroids/#/watch/", height=650)


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

        if i!=len(asteroid_data)-1:
            st.markdown("---")

with tab3:
    st.markdown("### 🌌 About the Project")
    st.markdown(
        """
        <div style='
            text-align: justify;
            padding-right: 30px;
            font-size: 16px;
            line-height: 1.7;
            color: #dddddd;
        '>
        <strong>Deep Impact</strong> is an interactive machine learning dashboard that models, simulates, and classifies the potential threat posed by Near-Earth Objects (NEOs), including asteroids and comets whose orbits bring them into close proximity with Earth. The project integrates astrophysical modeling, data science techniques, and supervised machine learning methods to create a scientifically grounded, interpretable risk estimation platform. It uses real-world observational data sourced from NASA’s Near-Earth Object database, focusing on key features such as encounter velocity, estimated diameter from optical reflectivity measurements, and absolute magnitude as an indicator of intrinsic brightness. These parameters are selected for their direct physical relevance to impact outcomes, where kinetic energy serves as a critical determinant of destructive potential. Feature engineering refines the raw measurements by averaging minimum and maximum diameter estimates, standardizing all inputs to promote stable model learning, and emphasizing velocity given its quadratic influence on energy release. Deep Impact applies a Random Forest Regressor to predict a kinetic energy–based risk score for each simulated object, translating continuous outputs into discrete hazard levels calibrated against historical asteroid impact events including the Tunguska (1908) and Chelyabinsk (2013) incidents. The platform bridges physics-based reasoning with machine learning predictions to offer accessible yet rigorous risk assessments.
        <br><br>
        Model development emphasizes scientific accuracy, physical interpretability, and predictive robustness. The Random Forest model is selected for its ensemble-based approach, which captures complex, non-linear relationships between asteroid characteristics while resisting overfitting through variance reduction across decision trees. A logarithmic transformation of kinetic energy is employed as the target variable to accommodate the broad dynamic range of impact energies, from minor airbursts to globally significant collisions. Hyperparameter tuning is conducted via grid search and k-fold cross-validation, optimizing model parameters such as maximum tree depth, minimum samples per split, and the number of estimators to achieve a balance between model complexity and generalization ability. Evaluation using metrics such as the coefficient of determination (R²), mean absolute error (MAE), and root mean squared error (RMSE) confirms the model’s high predictive accuracy and stable behavior across validation sets. Feature importance analysis aligns with theoretical kinetic energy relationships, highlighting velocity as the dominant predictor, followed by diameter, both of which critically affect mass and energy calculations. Absolute magnitude provides secondary predictive value by constraining uncertainty in size estimation, especially for objects with incomplete observational profiles.
        <br><br>
        The dashboard, developed using the Streamlit framework, enables users to explore a wide range of hypothetical asteroid impact scenarios by adjusting physical input parameters and observing real-time updates to predicted kinetic energy outputs and hazard classifications. Through dynamic user interaction, the system illustrates fundamental astrophysical principles such as the sensitivity of impact severity to small changes in velocity and mass, reinforcing concepts like the quadratic velocity dependence of kinetic energy. Deep Impact demonstrates how machine learning models, when informed by domain-specific physics, can serve as effective, scalable tools for preliminary planetary defense analyses. The platform provides an accessible interface that bridges detailed scientific modeling with public understanding, offering users insight into the mechanisms driving asteroid impact threats. Future extensions of the project aim to incorporate additional orbital parameters such as eccentricity and inclination, material composition proxies, and probabilistic uncertainty modeling to refine risk predictions further and contribute to the ongoing development of space hazard assessment technologies. 🚀🌍
        """,
        unsafe_allow_html=True
    )

# Footer
st.markdown(
    """
    <hr style="border: 1px solid #3E4145; margin-top: 50px; margin-bottom: 10px;">
    <div style='text-align: center; font-size: 15px; color: #888888;'>
        Made with ❤️ by <strong>Arbina Gotame</strong> | Deep Impact Project
    </div>
    """,
    unsafe_allow_html=True
)
