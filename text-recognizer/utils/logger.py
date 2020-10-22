from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging


def initial_logger(log_file_path):
    FORMAT = '%(asctime)s-%(levelname)s: %(message)s'
    logging.basicConfig(filename=log_file_path, level=logging.INFO, format=FORMAT)
    logger = logging.getLogger(__name__)
    return logger


