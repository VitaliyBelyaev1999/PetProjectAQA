import logging


# Настройка логгера
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def pytest_runtest_setup(item):
    logger.info(f"PREPARE TO TEST: {item.name}")
