"""Read from file task file"""

from app.loggers.loggers import get_custom_logger
from app.config import FILES_INPUT_DIR


def read_file_task() -> None:
    """Read from file task file"""
    logger = get_custom_logger("read_file")

    logger.debug("Read file task started")

    file_path = FILES_INPUT_DIR.joinpath(".gitkeep")
    if file_path.exists():
        print("======================File content task==========================")
        with open(file_path, encoding="UTF-8") as file:
            print(file.read())
        file.close()
        print("================================================================")
    else:
        logger.warning(f"File {file_path.name} not found")

    logger.debug("Read file task finished")
