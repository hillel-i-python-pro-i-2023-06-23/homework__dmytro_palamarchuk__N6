"""Module homework #5"""

from dotenv import load_dotenv

from app.loggers.loggers import get_core_logger
from app.loggers.init_logging import init_logging
from app.services.read_file_task import read_file_task
from app.services.generate_users_task import generate_users_task
from app.services.astronauts_task import astronauts_task
from app.services.average_value_task import average_value_task


def main() -> None:
    """Main entry point"""
    # Upload dotenv configuration
    load_dotenv()
    # Initialize logging
    init_logging()

    logger = get_core_logger()
    # Start app
    logger.info("Application Starting")

    # Task #1: read-print file content
    read_file_task()

    # Task #2: Generate users
    generate_users_task(50)

    # Task #3: astronauts
    astronauts_task()

    # Task #4: average value
    average_value_task()

    # Finish app
    logger.info("Application Finished")
