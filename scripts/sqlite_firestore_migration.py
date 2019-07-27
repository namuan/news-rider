import datetime
import os
import sys

from google.cloud import firestore
from peewee import *

sys.path.append(os.getcwd())

home_dir = os.getenv('HOME')

db_file_path = os.getcwd() + '/../../data/news_rider.db'
print("Reading database from {}".format(db_file_path))
old_db = SqliteDatabase(db_file_path)


class NewsItem(Model):
    NewsUrl = CharField(primary_key=True)
    NewsTitle = CharField()
    TimeStamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = old_db


db = firestore.Client()
posts_ref = db.collection('posts')


def save_data(url, title, timestamp):
    print(f"Adding {url} for database")
    posts_ref.add({
        'news_url': url,
        'news_title': title,
        'timestamp': timestamp
    })


def exists_in_database(url):
    print(f"Checking if {url} exists in database")
    news_found_ref = posts_ref.where('news_url', '==', url).limit(1)
    return next(news_found_ref.get(), None) is not None


if __name__ == '__main__':
    for news_item in NewsItem.select():
        if not exists_in_database(news_item.NewsUrl):
            save_data(news_item.NewsUrl, news_item.NewsTitle, news_item.TimeStamp)
