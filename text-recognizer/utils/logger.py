from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import logging
import yaml
import logging.config


def configure_logger(name, log_path):
    with open('configs/logger_config.yaml', 'r') as f:
        config_dict = yaml.safe_load(f.read())
        config_dict['handlers']['file']['filename'] = config_dict['handlers']['file']['filename'].format(log_path)
    logging.config.dictConfig(config_dict)
    return logging.getLogger(name)


if __name__ == '__main__':
    alog = configure_logger('default', 'configs/output/TPS-RCNN-BiLSTM-Attn/log.txt')
    alog.debug('debug message!')

