import matplotlib.pyplot as plt
import os

def plot_feature_importance(model, X, save_path: str = None):
    """
    Plots and optionally saves feature importances from a trained Random Forest model.

    Parameters:
    - model: trained RandomForestRegressor or RandomForestClassifier
    - X: DataFrame of input features (used during model training)
    - save_path: optional path to save the plot (e.g., "reports/figures/feature_importance_rf.png")
    """

