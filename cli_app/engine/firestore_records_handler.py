import datetime
import os
import sys

from google.cloud import firestore
from google.api_core.exceptions import ServiceUnavailable
from .log_helper import logger
from .retry_decorator import retry

sys.path.append(os.getcwd())

cred_json = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
logger.info("Reading from " + cred_json)

db = firestore.Client()
posts_ref = db.collection('posts')


def save_data(url, title):
    logger.info(f"Adding {url} for database")
    posts_ref.add({
        'news_url': url,
        'news_title': title,
        'timestamp': datetime.datetime.now()
    })


@retry(ServiceUnavailable, logger=logger)
def exists_in_database(url):
    logger.info(f"Checking if {url} exists in database")
    news_found_ref = posts_ref.where('news_url', '==', url).limit(1)
    return next(news_found_ref.get(), None) is not None
