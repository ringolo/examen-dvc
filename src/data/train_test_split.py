import pandas as pd
from src.utils import PATHS
from src.utils.logs import log_ok, log_fail, log_info
from sklearn.model_selection import train_test_split

def main():
    # Load data
    try:
        # using date as index will remove it from feature, which is a desired effect, as no relation is expected between date and target.
        df = pd.read_csv(PATHS.raw_data_file, parse_dates=["date"], index_col="date")
        log_ok("preprocess", "raw data loaded")
    except Exception as e:
        log_fail("preprocess", f"failed to load raw data: {e}")
        return
    
    # check for nas
    if df.isna().sum().sum():
        initial_lines = len(df)
        df.dropna(inplace=True)
        removed_lines = len(df) - initial_lines
        log_info("preprocess", f"pulled data had na values. {removed_lines}/{initial_lines} were removed")
    
    # check for duplicates
    if df.duplicated().sum():
        initial_lines = len(df)
        df.drop_duplicates(inplace=True)
        removed_lines = len(df) - initial_lines
        log_info("preprocess", f"pulled data had duplicates. {removed_lines}/{initial_lines} were removed")
    
    # split into train and test sets
    try:
        features = df.drop(columns="silica_concentrate")
        target = df["silica_concentrate"]
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
        X_train.to_csv(PATHS.processed_data / "X_train.csv", index=False)
        X_test.to_csv(PATHS.processed_data / "X_test.csv", index=False)
        y_train.to_csv(PATHS.processed_data / "y_train.csv", index=False)
        y_test.to_csv(PATHS.processed_data / "y_test.csv", index=False)
        log_ok("preprocess", "data preprocessed and saved")
    except Exception as e:
        log_fail("preprocess", f"failed to preprocess data: {e}")

if __name__ == "__main__":
    main()