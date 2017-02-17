import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S')

from .client import (get_questions_by_tag)
from .statistics import (
    get_top_tags,
    calculate_statistics
)
