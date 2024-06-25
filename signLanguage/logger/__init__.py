import logging
import os
from datetime import datetime
from from_root import from_root

DATE_TIME_FORMAT = '%Y_%m_%d_%H_%M_%S'
DATE_TIME = datetime.now().strftime(DATE_TIME_FORMAT)
LOG_FILE = f"{DATE_TIME}.log"
# print(f"LOG_FILE = {LOG_FILE}")

log_folder = 'log'
log_path = os.path.join(from_root(), log_folder, DATE_TIME)
# print(f"log_path = {log_path}")

os.makedirs(log_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)
print(f"Logs are stored in file: {LOG_FILE_PATH}")

FORMAT = "[ %(asctime)s ] - %(name)s - %(levelname)s - %(message)s"

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format=FORMAT,
    level=logging.INFO
)
