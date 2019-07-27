import datetime
import os
import sys

from peewee import *

from .log_helper import logger

sys.path.append(os.getcwd())

home_dir = os.getenv('HOME')

db = SqliteDatabase(home_dir + '/news_rider.db')


class NewsItem(Model):
    NewsUrl = CharField(primary_key=True)
    NewsTitle = CharField()
    TimeStamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


db.create_tables([NewsItem], safe=True)


def save_data(url, title):
    logger.info(f"Adding {url} for database")
    NewsItem.insert(
        {
            'NewsUrl': url,
            'NewsTitle': title
        }
    ).on_conflict_ignore().execute()


def exists_in_database(url):
    logger.info(f"Checking if {url} exists in database")
    existing_news_item = NewsItem.select().where(NewsItem.NewsUrl == url)
    return existing_news_item
