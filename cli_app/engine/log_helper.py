import colorlog
import logging

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter('%(asctime)s %(log_color)s%(levelname)s : %(message)s'))

logger = colorlog.getLogger('news_rider')
logger.addHandler(handler)
logger.setLevel(logging.INFO)
