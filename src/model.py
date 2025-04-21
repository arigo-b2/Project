import os
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score
from scipy.stats import randint
from visualisation import plot_feature_importance

DATA_PATH_PROCESSED = os.getenv("DATA_PATH_PROCESSED")

# Load processed dataset
data_path = f"{DATA_PATH_PROCESSED}/neo_features_for_risk_regression.xlsx"
df = pd.read_excel(data_path)

# Input features (scaled)
feature_cols = [
    'velocity_km_s_scaled',
    'absolute_magnitude_h_scaled',
    'avg_diameter_km_scaled',
    'kinetic_energy_scaled'
]

X = df[feature_cols]
y = df['log_risk_score']  # New target: log(risk_score)

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Hyperparameter search space
param_dist = {
    'n_estimators': randint(100, 300),
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'max_features': ['auto', 'sqrt', 'log2']
}

# Randomized search
search = RandomizedSearchCV(
    estimator=RandomForestRegressor(random_state=42),
    param_distributions=param_dist,
    n_iter=20,
    scoring='neg_mean_absolute_error',
    cv=5,
    n_jobs=-1,
    verbose=1,
    random_state=42
)

print("🔍 Running hyperparameter tuning...")
search.fit(X_train, y_train)
model = search.best_estimator_

print("✅ Best hyperparameters found:")
print(search.best_params_)

# Predict
y_pred_log = model.predict(X_test)

# Reverse log transform
y_test_score = np.expm1(y_test)
y_pred_score = np.expm1(y_pred_log)

# Evaluate
mae = mean_absolute_error(y_test_score, y_pred_score)
rmse = root_mean_squared_error(y_test_score, y_pred_score)
r2 = r2_score(y_test_score, y_pred_score)

# Print results
print("✅ Model Evaluation (risk_score prediction):")
print(f"R² Score:              {r2:.3f}")
print(f"Mean Absolute Error:   {mae:,.2f}")
print(f"Root Mean Squared Error: {rmse:,.2f}")

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/rf_risk_model.pkl")
print("✅ Model saved to models/rf_risk_model.pkl")

plot_feature_importance(model, X, "reports/figures/feature_importance_rf_hp_tuning.png")