from src.core.config import settings

import logging
import sys

class Logger:
    def __init__(self, name: str):
        self.name = name
        self.level = settings.log_level

        self.logger = logging.getLogger(name)
        self.logger.setLevel(self._get_level(self.level))
        self._setup_handlers()

    def _get_level(self, level_name: str) -> int:
        return getattr(logging, level_name, logging.INFO)

    def _setup_handlers(self):
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(self._get_level(self.level))
        console_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)

    def get_logger(self) -> logging.Logger:
        return self.logger

logger = Logger("polygon-erc20").get_logger()