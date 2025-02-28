import logging
import configparser
from logging.handlers import RotatingFileHandler


test_config = configparser.ConfigParser()
test_config.read('pytest.ini')

name_file = str(test_config['pytest']['log_file'])
logging.basicConfig(filename=name_file)
handler = RotatingFileHandler(name_file, maxBytes=10240, backupCount=1)


log_format = "%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"


def get_file_handler():
    file_handler = logging.FileHandler(name_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(log_format))
    return file_handler


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(log_format))
    return stream_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger
