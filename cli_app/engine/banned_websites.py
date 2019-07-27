banned_websites_list = [
    'twitter.com',
    'imgur.com',
    'youtu.be',
    'youtube.com'
]


def is_banned(url):
    return any(l in url for l in banned_websites_list)
