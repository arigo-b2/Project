import pandas as pd
import numpy as np

def calculate_average_diameter(row):
    """
    Calculate average estimated diameter in km.
    """
    return (row['diameter_min_km'] + row['diameter_max_km']) / 2