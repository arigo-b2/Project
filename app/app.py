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

    # NASA visual
    st.markdown("### 🌌 NASA Asteroid 3D Viewer")
    components.iframe("https://eyes.nasa.gov/apps/asteroids/#/watch/", height=700)

    # Two iframe views
    st.markdown("### 🌌 Asteroid Views")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🌠 Asteroid 2025 BP6 Close Approach**")
        components.iframe("https://eyes.nasa.gov/apps/asteroids/#/2025_bp6?time=2025-01-25T23:27:43.516+00:00&rate=1", height=600)
    with col2:
        st.markdown("**🌎 Planet Earth**")
        components.iframe("https://eyes.nasa.gov/apps/asteroids/#/planets/earth", height=600)
    st.markdown("---")
    

with tab2:
    st.subheader("🪐 Top 10 Asteroid Visualisations and Detailed Profiles")

    asteroid_data = [
        {
            "name": "Apophis",
            "slug": "99942_apophis",
            "desc": """
Apophis is a near-Earth asteroid approximately 370 meters in diameter, classified as an Aten-type asteroid. It became widely known after early orbit predictions suggested a small probability of Earth impact in 2029, which has since been ruled out. However, its close flyby at only 31,000 km—closer than geostationary satellites—makes it a perfect case study in planetary defense.  
Apophis is primarily composed of silicate rock, with a relatively high albedo (reflectivity) and a tumbling spin state. Its orbit is slightly inclined and resonant, meaning gravitational interactions with Earth could subtly alter its future path. Due to its high velocity (around 30 km/s) and moderate size, it carries enough kinetic energy to cause continental-scale destruction if it were to impact.  
<br>
NASA and ESA are both closely tracking this object, and in 2029 it will be visible to the naked eye over parts of Earth, giving scientists a rare opportunity to study asteroid dynamics up close.
"""
        },
        {
            "name": "Bennu",
            "slug": "101955_bennu",
            "desc": """
Bennu is a carbonaceous near-Earth asteroid about 490 meters in diameter and rich in primitive organic material. It orbits the Sun every 1.2 years and has a very Earth-like orbit, placing it in the Apollo group of asteroids.  
Bennu is classified as a potentially hazardous asteroid (PHA) due to its high impact probability (1 in 1750 by 2300) and close Earth flybys, particularly in the late 2100s.  
What makes Bennu remarkable is its role in planetary science—NASA’s OSIRIS-REx mission successfully collected samples from its surface in 2020, returning them to Earth in 2023. These samples are helping scientists understand the early solar system.  
Bennu rotates once every 4.3 hours and has a "rubble pile" structure with loosely bound rocks and low density. A potential impact with Bennu would release energy equivalent to 1,200 megatons of TNT.
"""
        },
        {
            "name": "Florence",
            "slug": "3122_florence",
            "desc": """
Florence is one of the largest known near-Earth asteroids, measuring a massive 4.4 kilometers in diameter. It passed safely by Earth in 2017 at a distance of 7 million km but remains a significant object due to its sheer size and mass.  
Florence is particularly interesting because it has two small moons, making it one of the few triple asteroid systems ever observed in the near-Earth population. Its rotation period is about 2.4 hours, and its surface composition suggests a stony S-type asteroid.  
While Florence currently poses no impact threat, its size gives it the potential to cause global-scale devastation in the extremely unlikely case of an Earth impact. Studies of Florence help refine radar imaging and orbital mechanics models for large NEOs.
"""
        },
        {
            "name": "2023 DW",
            "slug": "2023_dw",
            "desc": """
2023 DW is a recently discovered asteroid approximately 50 meters in diameter, first observed in February 2023. It garnered attention due to an early estimate indicating a 1 in 560 chance of impacting Earth in 2046, although this has been revised downward with additional observations.  
Its orbit is still being refined, but 2023 DW highlights the importance of early detection and impact probability modeling. Its relatively small size may not seem threatening, but similar-sized asteroids like the Chelyabinsk meteor (20m) in 2013 caused widespread damage due to airburst shockwaves.  
2023 DW would likely disintegrate in the atmosphere under most impact scenarios, but could still pose a serious threat to populated regions if it enters at a shallow angle.  
This asteroid is a strong candidate for upcoming observation campaigns and may influence future planetary defense strategies.
"""
        },
        {
            "name": "Didymos",
            "slug": "65803_didymos",
            "desc": """
Didymos is a binary asteroid system consisting of a primary asteroid (~780 meters) and a moonlet called Dimorphos (~160 meters). It orbits the Sun every 2.1 years and is a member of the Apollo group of near-Earth asteroids.  
Didymos gained global attention as the target of NASA’s DART mission (2022)—the first real-world test of asteroid deflection. DART successfully impacted Dimorphos, shortening its orbital period by 33 minutes, proving that kinetic impactors can alter asteroid trajectories.  
The Didymos system is a crucial proof-of-concept for planetary defense technologies. Its binary nature also provides rare insight into tidal forces, mutual orbital evolution, and surface cohesion in small bodies.  
While Didymos itself is not a threat, its configuration and accessibility make it one of the most important objects for long-term planetary risk reduction studies.
"""
        },
        {
            "name": "Toutatis",
            "slug": "4179_toutatis",
            "desc": """
Toutatis is a highly elongated asteroid (~4.5 km long) with a tumbling, chaotic rotation that makes it one of the most unique objects observed. It passed Earth at a safe distance multiple times and was extensively imaged by radar and the Chang’e 2 mission. Its irregular motion provides valuable data on gravitational torques and non-uniform mass distribution in NEOs. While not a current threat, its size and proximity warrant occasional monitoring, especially due to its near-resonant orbital characteristics with Earth.
"""
        },
        {
            "name": "Ryugu",
            "slug": "162173_ryugu",
            "desc": """
Ryugu is a C-type asteroid with a diameter of ~900 meters. Its surface was sampled by the Japanese Hayabusa2 mission, which returned material to Earth in 2020. Ryugu’s structure is porous, with evidence of hydrated minerals suggesting early solar system water content. Though not a threat, Ryugu is critical for understanding asteroid cohesion and formation. It provides benchmarks for how weakly bound rubble piles behave under solar radiation and spin-up forces that might eventually lead to fragmentation.
"""
        },
        {
            "name": "Ganymed",
            "slug": "1036_ganymed",
            "desc": """
Ganymed is the largest known near-Earth asteroid at over 35 km in diameter. Although its orbit keeps it safely distant from Earth, its mass and volume make it a keystone object for planetary science and impact modeling. Ganymed is also of interest due to its spectral similarities with inner belt asteroids, suggesting cross-region migration in the early solar system. Its observations contribute to long-term risk assessments of exceptionally massive NEOs.
"""
        },
        {
            "name": "Phaethon",
            "slug": "3200_phaethon",
            "desc": """
Phaethon is an unusual near-Earth object in that it behaves like a hybrid asteroid-comet. It is the parent body of the Geminid meteor shower, and its extremely close perihelion (~0.14 AU) causes it to shed dust like a comet. At 5.1 km in diameter, Phaethon is unusually large for a meteor-shower progenitor. Its blue color and high thermal stress cycling make it a fascinating subject for surface evolution studies. While not immediately hazardous, its orbital characteristics put it under regular review by planetary defense programs.
"""
        },
        {
            "name": "1998 OR2",
            "slug": "52768_1998_or2",
            "desc": """
1998 OR2 is a stony asteroid approximately 2.1 kilometers in diameter that made a close approach in April 2020 at ~6.3 million km. It is one of the largest potentially hazardous asteroids (PHAs) due to its size and Earth-crossing orbit. Its reflective surface and stable rotation make it ideal for radar observations and shape modeling. While currently not on a collision course, its orbital uncertainty remains under refinement, especially beyond the 2100s. It serves as a training ground for impact mitigation strategies and ground-based telescopic coordination.
"""
        },
    ]

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

        st.markdown("---")
