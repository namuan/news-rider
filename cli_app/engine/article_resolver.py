from urllib.error import HTTPError

import requests
from bs4 import BeautifulSoup

from .log_helper import logger
from .banned_websites import is_banned


def fetch_html_title(url):
    logger.info(f"Fetching HTML title for {url}")
    if is_banned(url):
        return None

    try:
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36"
        headers = {'User-Agent': user_agent}
        page = requests.get(url, headers=headers)
        bs = BeautifulSoup(page.text, "html.parser")
        return bs.title.string
    except HTTPError as err:
        logger.error(f"Unable to fetch URL {url} - HTTP Code: {err.code} - {err.reason}")
    except Exception as err:
        logger.error(f"Unable to fetch URL {url} - {err}")

    return None
