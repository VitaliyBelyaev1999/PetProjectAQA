import logging


def pytest_runtest_setup(item):
    logging.info(f"Start test {item.name}")

