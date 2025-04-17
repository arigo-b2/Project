import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def calculate_average_diameter(row):
    return (row['diameter_min_km'] + row['diameter_max_km']) / 2

def calculate_kinetic_energy(row):
    return (row['avg_diameter_km'] ** 3) * (row['velocity_km_s'] ** 2)

def generate_regression_features(df):
    df = df.copy()

    # Derived columns
    df['avg_diameter_km'] = df.apply(calculate_average_diameter, axis=1)
    df = df.dropna(subset=[
        'velocity_km_s',
        'absolute_magnitude_h',
        'avg_diameter_km',
        'miss_distance_km'
    ])
    df['kinetic_energy'] = df.apply(calculate_kinetic_energy, axis=1)

    # Feature columns
    features = [
        'velocity_km_s',
        'absolute_magnitude_h',
        'avg_diameter_km',
        'kinetic_energy'
    ]
    target = 'miss_distance_km'

    # Scaling
    scaler = MinMaxScaler()
    df[[f + '_scaled' for f in features]] = scaler.fit_transform(df[features])

    # Output
    X = df[[f + '_scaled' for f in features]]
    y = df[target]

    return X, y, df

# Test
if __name__ == "__main__":
    input_path = "data/raw/neo_data.xlsx"
    output_path = "data/processed/neo_features_for_regression.xlsx"

    df = pd.read_excel(input_path)
    X, y, df_full = generate_regression_features(df)
    df_full.to_excel(output_path, index=False)
    print(f"✅ Regression features saved to: {output_path}")
