import sqlite3
import logging
import os
from ConfigParser import SafeConfigParser as ConfigParser

ROOT_PATH = os.path.abspath(__file__)
CONFIG_PATH = os.path.abspath(os.path.join(ROOT_PATH, os.pardir))
CONFIG_FILE = os.path.abspath(os.path.join(CONFIG_PATH, "config.ini"))

logger = logging.getLogger(__name__)

_config = ConfigParser()
_config.read(CONFIG_FILE)

conn = sqlite3.connect('subsciber.db', check_same_thread=False)
cursor = conn.cursor()


def setup_logging():
    """Sets up logging"""
    logging.basicConfig(level=logging.DEBUG,
                        format=('%(asctime)s: %(levelname)s: [%(name)s.%(funcName)s] - %(message)s'))
    handler = logging.StreamHandler()
    logger.addHandler(handler)


def get_configs(name='DEFAULT'):
    return dict(_config.items(name))


def get_api_key():
    return get_configs['api_key']