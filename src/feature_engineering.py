import pandas as pd
import numpy as np

# Torino Scale Threat Level Calculation:
# -------------------------------------------------------------------
# According to NASA and the Torino Scale, an asteroid's threat level
# depends on two main factors:
# 1. Collision Probability  → how likely it is to hit Earth
# 2. Kinetic Energy         → how damaging it would be if it did
#
# In this project, we simulate that using:
# - Miss Distance           → proxy for inverse collision probability
# - Kinetic Energy          → estimated from diameter^3 and velocity^2
#
# These are used to create a "Torino-like" score, which we convert
# to an integer 0–10 level to resemble the official Torino Scale.
#
# ⚠️ Reference: https://carlkop.home.xs4all.nl/torino.html
# -------------------------------------------------------------------

def calculate_average_diameter(row):
    """
    Calculate average estimated diameter in km.
    """
    return (row['diameter_min_km'] + row['diameter_max_km']) / 2

def calculate_kinetic_energy(row):
    """
    Estimate kinetic energy using: KE ~ 0.5 * mass * velocity^2
    Assume mass ∝ diameter^3 (simplified proxy).
    """
    diameter = row['avg_diameter_km']
    velocity = row['velocity_km_s']
    estimated_mass = diameter ** 3
    return 0.5 * estimated_mass * (velocity ** 2)

def calculate_torino_proxy_score(row):
    """
    Estimate a Torino-like score based on kinetic energy and miss distance.
    """
    if row['miss_distance_km'] == 0:
        return 10  # Treat direct hits as max threat
    return row['kinetic_energy'] / row['miss_distance_km']