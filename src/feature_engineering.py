import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def calculate_average_diameter(row):
    return (row['diameter_min_km'] + row['diameter_max_km']) / 2

def calculate_kinetic_energy(row):
    return (row['avg_diameter_km'] ** 3) * (row['velocity_km_s'] ** 2)

def generate_risk_features(df):
    df = df.copy()

    # Required derived columns
    df['avg_diameter_km'] = df.apply(calculate_average_diameter, axis=1)
    df['kinetic_energy'] = df.apply(calculate_kinetic_energy, axis=1)

    # Drop rows with missing values
    df = df.dropna(subset=[
        'velocity_km_s',
        'absolute_magnitude_h',
        'avg_diameter_km',
        'kinetic_energy',
        'miss_distance_km'
    ])

    # Compute new risk score
    df['raw_risk_score'] = df['kinetic_energy'] / df['miss_distance_km']
    df['log_risk_score'] = np.log1p(df['raw_risk_score'])  # TARGET

    # Extra features
    df['diameter_range'] = df['diameter_max_km'] - df['diameter_min_km']
    df['diameter_ratio'] = df['diameter_max_km'] / df['diameter_min_km']
    df['log_velocity'] = np.log1p(df['velocity_km_s'])

    # Final features to use
    features = [
        'velocity_km_s',
        'absolute_magnitude_h',
        'avg_diameter_km',
        'kinetic_energy'
    ]
    target = 'log_risk_score'

    # Scale input features
    scaler = MinMaxScaler()
    df[[f + '_scaled' for f in features]] = scaler.fit_transform(df[features])

    # Final X, y
    X = df[[f + '_scaled' for f in features]]
    y = df[target]

    return X, y, df

# Test
if __name__ == "__main__":
    input_path = "data/raw/neo_data.xlsx"
    output_path = "data/processed/neo_features_for_risk_regression.xlsx"

    df = pd.read_excel(input_path)
    X, y, df_full = generate_risk_features(df)
    df_full.to_excel(output_path, index=False)
    print(f"✅ Processed risk features saved to: {output_path}")