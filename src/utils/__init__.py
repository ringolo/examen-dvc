from types import SimpleNamespace
from pathlib import Path

project_folder = Path(__file__).parents[2]
PATHS = SimpleNamespace(
    raw_data=project_folder / "data" / "raw_data",
    raw_data_file=project_folder / "data" / "raw_data" / "data.csv",
    processed_data=project_folder / "data" / "processed_data",
    models=project_folder / "models",
    metrics=project_folder / "metrics",
    log_file=project_folder / "logs" / "logs.txt",

)