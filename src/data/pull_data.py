import os
import requests
from src.utils import PATHS
from src.utils.logs import log_ok, log_fail

data_url = "https://datascientest-mlops.s3.eu-west-1.amazonaws.com/mlops_dvc_fr/raw.csv"
os.makedirs(PATHS.raw_data, exist_ok=True)

def main():
    response = requests.get(data_url)
    if response.status_code == 200:
        with open(PATHS.raw_data_file, 'wb') as f:
            f.write(response.content)
        log_ok("PULL", "Successfully uploaded data")
    else:
        log_fail("PULL", f"Failed to download data: http code={response.status_code}")

if __name__ == '__main__':
    main()