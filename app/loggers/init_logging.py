"""Initializes the loggers"""

import logging
import sys
import os

# from app.config import LOGS_DIR


def init_logging() -> None:
    """
    Initializes the loggers

    Returns
    -------
    None
    """
    logging.basicConfig(
        level=os.getenv("LOGGER_LEVEL", "INFO"),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        stream=sys.stdout,
        # filename=LOGS_DIR.joinpath("app.log"),
        # filemode="w",
    )
    logging.getLogger("core").debug("Logging was initiated.")
