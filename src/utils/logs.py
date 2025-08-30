from src.utils import PATHS
from datetime import datetime
from functools import partial

def log(result, operation, message, print_to_stdout=True):
    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    log_message = f"{timestamp}: [{result.upper()}] {operation.upper()}: {message}\n"
    with open(PATHS.log_file, 'a') as log_file:
        log_file.write(log_message)
    if print_to_stdout:
        print(log_message, end='')

log_ok = partial(log, "OK")
log_fail = partial(log, "FAIL")
log_info = partial(log, "INFO")
if not PATHS.log_file.parent.exists():
    PATHS.log_file.parent.mkdir(parents=True)
    log_info("LOGS", f"Created log directory at {PATHS.log_file.parent}")
