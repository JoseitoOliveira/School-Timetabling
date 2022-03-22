"""
Definições do logger

@authors	joseito.junior@brphotonics.com
@date   	01/02/2022

"""


import logging
import os
import sys
import traceback

from logging.handlers import TimedRotatingFileHandler

if not os.path.exists('logs'):
    os.makedirs('logs')


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s::%(levelname)s::%(message)s',
    datefmt='%H:%M:%S'
)

# Console Handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

# File Handler


fh = TimedRotatingFileHandler('logs/log.log',
                              when="midnight",
                              interval=1,
                              encoding='utf8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
fh.suffix = "%Y%m%d"

# Adicionando o handlers
logger.addHandler(ch)
logger.addHandler(fh)


def logger_print(*values: object, **kwargs: object) -> None:
    for value in values:
        logger.info(value)


def print_exception_locals():
    exc_type, exc_value, tb = sys.exc_info()

    if tb is not None:
        prev = tb
        curr = tb.tb_next

        while curr is not None:
            prev = curr
            curr = curr.tb_next

        logger.info(prev.tb_frame.f_locals)


def print_exception():
    traceback.print_exc()
    print_exception_locals()
