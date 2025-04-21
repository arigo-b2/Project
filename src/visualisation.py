import os
import matplotlib.pyplot as plt

def plot_feature_importance(model, X, save_path: str = None):
    """
    Plots and optionally saves feature importances from a trained Random Forest model.

    Parameters:
    - model: trained RandomForestRegressor or RandomForestClassifier
    - X: DataFrame of input features (used during model training)
    - save_path: optional path to save the plot (e.g., "reports/figures/feature_importance_rf.png")
    """
    importances = model.feature_importances_
    features = X.columns

    plt.figure(figsize=(8, 5))
    plt.barh(features, importances, color="skyblue")
    plt.xlabel("Feature Importance")
    plt.title("Random Forest Feature Importances")
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)
        print(f"📊 Saved feature importance plot to: {save_path}")
    plt.show()