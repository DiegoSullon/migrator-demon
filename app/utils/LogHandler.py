import logging
import sys


def getLogger(func_name, level = 'INFO'):
    # Logging config
    logger = logging.getLogger(func_name)
    if (logger.hasHandlers()):
        logger.handlers.clear()
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    if level == 'DEBUG':
        ch.setLevel(logging.DEBUG)
    else:
        ch.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(name)s -  %(funcName)s -  %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger