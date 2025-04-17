import pandas as pd
import numpy as np

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
    This is a custom scoring approach for demonstration.
    """
    if row['miss_distance_km'] == 0:
        return 10  # Treat direct hits as max threat
    return row['kinetic_energy'] / row['miss_distance_km']