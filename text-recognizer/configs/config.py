from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
sys.path.append('../')

import yaml
import argparse
import os
from easydict import EasyDict
from utils.logger import configure_logger
from utils.setup import setup_gpu_and_random


def get_args():
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument(
        '-c', '--config',
        metavar='C',
        default='None',
        help='The Configuration file')
    args = argparser.parse_args()
    return args


def get_config_from_yaml(yaml_file_path):
    """
    Get the config from a yaml file
    :param yaml_file_path:
    :return: config(dictionary)
    """
    # parse the configurations from the config json file provided
    with open(yaml_file_path, 'r') as config_file:
        config_dict = yaml.safe_load(config_file)
    return config_dict


def process_config(yaml_file_path):
    """
    Convert config dict to dot format ( config.abc) and process config such as: create dir,...
    :param yaml_file_path:
    :return: processed config
    """
    config_dict = get_config_from_yaml(yaml_file_path)
    config = EasyDict(config_dict)
    global_config = config.general
    data_config = config.data
    arch_config = config.arch

    # In case : experiment name is None or ''
    if global_config.exp_name == '' or global_config.exp_name is None:
        global_config.exp_name = arch_config.Transformation + '-' + arch_config.FeatureExtraction + '-' + \
                                  arch_config.SequenceModeling + '-' + arch_config.Prediction

    os.makedirs(global_config.output_dir + os.path.sep + global_config.exp_name, exist_ok=True)

    # vocab / character number configuration
    if data_config.sensitive:
        data_config.character += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # create log file
    config.log_file = global_config.output_dir + os.path.sep + global_config.exp_name + os.path.sep + 'log.txt'
    return config


def setup_config():
    args = get_args()
    config = process_config(args.config)
    setup_gpu_and_random(config)
    # logger = configure_logger('Config', config.log_file)
    # logger.info("Config: " + str(dict(config)) + '\n')
    return config


if __name__ == '__main__':
    setup_config()

