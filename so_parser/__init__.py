import logging

from .client import (get_questions_by_tag)
from .statistics import (calculate_statistics, get_top_tags)


def setup_logging():
    logger = logging.getLogger('so_client')
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

setup_logging()
