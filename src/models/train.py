import pickle
import pandas as pd
from src.utils import PATHS
from src.utils.logs import log_ok, log_fail, log_info
from xgboost import XGBRegressor

def main():
    # Load data
    try:
        X_train_scaled = pd.read_csv(PATHS.processed_data / "X_train_scaled.csv")
        y_train = pd.read_csv(PATHS.processed_data / "y_train.csv")
        log_ok("train", "X_train and y_train successfully loaded")
    except Exception as e:
        log_fail("train", f"failed to load X_train and y_train: {e}")
        return
    try:
        with open(PATHS.models/"best_params.pkl", "rb") as f:
            best_params = pickle.load(f)
        log_ok("train", "best params successfully loaded")
    except Exception as e:
        log_fail("train", f"failed to load best params: {e}")
        return

    # Train
    try:
        xgb = XGBRegressor(objective='reg:squarederror', random_state=42, **best_params)
        log_info("train", "Starting model training")
        xgb.fit(X_train_scaled, y_train)
        log_ok("train", "Model training completed")
    except Exception as e:
        log_fail("train", f"failed to train model: {e}")
        return

    # Save model
    try:
        with open(PATHS.models / "xgb.pkl", 'wb') as f:
            pickle.dump(xgb, f)
        log_ok("train", "Best model saved")
    except Exception as e:
        log_fail("train", f"failed to save best model: {e}")

if __name__ == "__main__":
    main()