from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import logging
import yaml
import logging.config
import sys


def configure_logger(name, log_path):
    with open('configs/logger_config.yaml', 'r') as f:
        config_dict = yaml.safe_load(f.read())
        config_dict['handlers']['file']['filename'] = config_dict['handlers']['file']['filename'].format(log_path)
        config_dict['loggers'][name] = config_dict['loggers'].pop('default')
    logging.config.dictConfig(config_dict)
    return logging.getLogger(name)


if __name__ == '__main__':
    alog = configure_logger('default', 'configs/outputs/TPS-RCNN-BiLSTM-Attn/log.txt')
    alog.debug('debug message!')

