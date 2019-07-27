from random import randint
import time
from .log_helper import logger


def sleepr():
    n = randint(10, 20)
    logger.info(f"Sleeping for {n} seconds")
    time.sleep(n)
