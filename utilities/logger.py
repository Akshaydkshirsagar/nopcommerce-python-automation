import logging
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parents[1] / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "automation.log"


def get_logger(name):
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger