import logging
import os
from datetime import datetime

_LOG_FILE = None

def _get_run_log_file():
    global _LOG_FILE
    if _LOG_FILE is None:
        os.makedirs("logs", exist_ok=True)
        _LOG_FILE = os.path.join(
            "logs",
            f"test_run_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
        )
    return _LOG_FILE


def get_logger(logger_name: str) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # Add handlers only once per logger
    if not logger.handlers:
        log_file = _get_run_log_file()

        file_handler = logging.FileHandler(log_file)
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        # Prevent double logging via root logger
        logger.propagate = False

    return logger
