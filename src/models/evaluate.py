import json
import pickle
import pandas as pd
from src.utils import PATHS
from src.utils.logs import log_ok, log_fail, log_info
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def main():
    # Load data
    try:
        X_test_scaled = pd.read_csv(PATHS.processed_data / "X_test_scaled.csv")
        y_test = pd.read_csv(PATHS.processed_data / "y_test.csv")
        log_ok("evaluate", "X_test_scaled and y_test successfully loaded")
    except Exception as e:
        log_fail("evaluate", f"failed to load X_test_scaled and y_test: {e}")
        return
    try:
        with open(PATHS.models/"xgb.pkl", "rb") as f:
            xgb = pickle.load(f)
        log_ok("evaluate", "XGBoost model successfully loaded")
    except Exception as e:
        log_fail("evaluate", f"failed to compute predictions XGBoost model: {e}")
        return

    # Compute predictions
    try:
        y_pred = xgb.predict(X_test_scaled)
        log_ok("evaluate", "model prediction completed")
    except Exception as e:
        log_fail("evaluate", f"failed to compute predictions: {e}")
        return
    
    # Save predictions
    try:
        pd.DataFrame(y_pred, columns=["silica_concentrate_pred"]).to_csv(PATHS.processed_data / "y_pred.csv", index=False)
        log_ok("evaluate", "y_pred saved")
    except Exception as e:
        log_fail("evaluate", f"failed to save y_pred: {e}")
        return

    # Compute metrics
    try:
        scores = {
            "mse": mean_squared_error(y_test, y_pred),
            "mae": mean_absolute_error(y_test, y_pred),
            "r2": r2_score(y_test, y_pred)
        }
        log_ok("evaluate", "model evaluation completed")
    except Exception as e:
        log_fail("evaluate", f"failed to compute metrics: {e}")
        return

    # Save metrics
    try:
        with open(PATHS.metrics / "scores.json", 'w') as f:
            json.dump(scores, f)
        log_ok("evaluate", "metrics saved")
    except Exception as e:
        log_fail("evaluate", f"failed to save metrics: {e}")

if __name__ == "__main__":
    main()