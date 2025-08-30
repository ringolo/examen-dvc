import pandas as pd
from src.utils import PATHS
from src.utils.logs import log_ok, log_fail, log_info
from sklearn.preprocessing import StandardScaler

def main():
    # Load data
    try:
        X_train = pd.read_csv(PATHS.processed_data / "X_train.csv")
        X_test = pd.read_csv(PATHS.processed_data / "X_test.csv")
        log_ok("normalize", "X_train and X_test successfully loaded")
    except Exception as e:
        log_fail("normalize", f"failed to load X_train and X_test: {e}")
        return

    # scale data
    try:
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        log_ok("normalize", "data successfully scaled")
    except Exception as e:
        log_fail("normalize", f"failed to scale data: {e}")
        return

    # Save scaled data
    try:
        pd.DataFrame(X_train_scaled, columns=X_train.columns).to_csv(PATHS.processed_data / "X_train_scaled.csv", index=False)
        pd.DataFrame(X_test_scaled, columns=X_test.columns).to_csv(PATHS.processed_data / "X_test_scaled.csv", index=False)
        log_ok("normalize", "scaled data saved")
    except Exception as e:
        log_fail("normalize", f"failed to save scaled data: {e}")

if __name__ == "__main__":
    main()