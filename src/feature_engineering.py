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