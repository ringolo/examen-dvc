import pickle
import pandas as pd
from src.utils import PATHS
from src.utils.logs import log_ok, log_fail, log_info
from sklearn.model_selection import GridSearchCV
from xgboost import XGBRegressor

def main():
    # Load data
    try:
        X_train_scaled = pd.read_csv(PATHS.processed_data / "X_train_scaled.csv")
        y_train = pd.read_csv(PATHS.processed_data / "y_train.csv")
        log_ok("grid search", "X_train and y_train successfully loaded")
    except Exception as e:
        log_fail("grid search", f"failed to load X_train and y_train: {e}")
        return

    # Perform grid search
    try:
        param_grid = {
            'n_estimators': [100, 200, 300],
            'max_depth': [3, 5, 7],
            'learning_rate': [0.01, 0.1, 0.2],
        }
        estimator = XGBRegressor(objective='reg:squarederror', random_state=42)
        gscv = GridSearchCV(
            estimator=estimator,
            param_grid=param_grid,
            scoring='neg_mean_squared_error',
            cv=5
        )
        log_info("grid search", "Starting Grid Search")
        gscv.fit(X_train_scaled, y_train)
        log_ok("grid search", f"Grid Search completed")
        log_info("grid search", f"Best model: {gscv.best_params_} with score {gscv.best_score_}")
    except Exception as e:
        log_fail("grid search", f"failed to perform grid search: {e}")
        return

    # Save best parameters
    try:
        best_params = gscv.best_params_
        with open(PATHS.models / "best_params.pkl", 'wb') as f:
            pickle.dump(best_params, f)
        log_ok("grid search", "Best parameters saved")
    except Exception as e:
        log_fail("grid search", f"failed to save best parameters: {e}")

if __name__ == "__main__":
    main()