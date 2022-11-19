import sys
from loguru import logger


class Logger:
    def __init__(self, logger: logger) -> None:
        self.logger = logger
        self._setup_default_format()

    def _setup_default_format(self) -> None:
        """Define the initial format for loguru"""
        fmt = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> - <level>{message}</level>"
        self.logger.remove()
        self.logger.add(sys.stderr, format=fmt)

    def set_verbose(self, active: bool) -> None:
        """If true print all the statements inside the code"""
        if not active:
            self.logger.remove()
            self.logger.add(sys.stderr, level="INFO")

    def error(self, message) -> None:
        self.logger.error(message)

    def debug(self, message) -> None:
        self.logger.debug(message)

    def info(self, message) -> None:
        self.logger.info(message)

    def warn(self, message) -> None:
        self.logger.warn(message)
