from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler

# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Logs folder
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "pipeline.log"

logger = logging.getLogger("ETL_PIPELINE")
logger.setLevel(logging.INFO)

# Prevent duplicate logs
if not logger.handlers:

    # File handler
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,   # 5 MB
        backupCount=3
    )

    # Console handler
    console_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)