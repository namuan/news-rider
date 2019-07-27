from random import shuffle

from .article_resolver import fetch_html_title
from .command_reader import read_commands
from .command_reader import run_command
from .firestore_records_handler import exists_in_database
from .firestore_records_handler import save_data
from .log_helper import logger
from .markdown_exporter import export_markdown
from .randomiser import sleepr
from .twitter_poster import send_tweet


def _random_sleeper():
    sleepr()


def _add_url_to_database(url, title):
    save_data(url, title)


def _send_tweet(title, url):
    tweet = f"📣 {title} - {url}"
    send_tweet(tweet)


def _export_markdown(title, url):
    export_markdown(title, url)


def _fetch_html_title(url):
    return fetch_html_title(url)


def _exists_in_database(url):
    return exists_in_database(url)


def _randomise_list_inplace(combined_urls):
    shuffle(combined_urls)


def _run_command(command):
    return run_command(command)


def _read_commands(commands_file):
    return read_commands(commands_file)


def orchestrate(commands_file, dry_run):
    # 1. Read all commands from the given file
    commands = _read_commands(commands_file)
    combined_urls = []
    # 2. For each command
    for command in commands:
        # 3. Run the command and capture output as list
        _random_sleeper()

        url_list = _run_command(command)
        # 4. Combine list from each command
        combined_urls += url_list

    # 4.3 randomise the list
    _randomise_list_inplace(combined_urls)

    # 5. For each url in list
    for url in combined_urls:

        if not url:
            continue

        # 6. Check if the url is in database. Goto 5 if it exist
        already_tweeted = _exists_in_database(url)
        if already_tweeted:
            logger.warning(f"{url} found in database")
            continue

        # 7. Using BeautifulSoap, get the title of the html page
        title = _fetch_html_title(url)
        if title is None:
            continue

        # 8. Compose tweet with title and url

        # 9. Send tweet after reading credentials from .env file
        if dry_run:
            logger.warning(f"DRYRUN: Not sending {title}")
        else:
            _export_markdown(title, url)
            # _send_tweet(title, url) Enabling this will send a tweet to your account

        # 10. Add url in database
        _add_url_to_database(url, title)

        # 11. Sleep for random # of secs
        _random_sleeper()
