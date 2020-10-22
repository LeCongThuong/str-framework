import random
import numpy as np
import torch
import torch.backends.cudnn as cudnn


def setup_gpu_and_random(config):
    """
    Set up random seed and reconfig batch_size and workers
    :param config:
    :return:
    """
    random.seed(config.general.manualSeed)
    np.random.seed(config.general.manualSeed)
    torch.manual_seed(config.general.manualSeed)
    torch.cuda.manual_seed(config.general.manualSeed)

    cudnn.benchmark = True
    cudnn.deterministic = True
    config.num_gpu = torch.cuda.device_count()

    if config.num_gpu > 1:
        print('------ Use multi-GPU setting ------')
        print('if you stuck too long time with multi-GPU setting, try to set --workers 0')
        # check multi-GPU issue https://github.com/clovaai/deep-text-recognition-benchmark/issues/1
        config.workers = config.workers * config.num_gpu
        config.batch_size = config.batch_size * config.num_gpu

        """ previous version
        print('To equlize batch stats to 1-GPU setting, the batch_size is multiplied with num_gpu and multiplied batch_size is ', opt.batch_size)
        opt.batch_size = opt.batch_size * opt.num_gpu
        print('To equalize the number of epochs to 1-GPU setting, num_iter is divided with num_gpu by default.')
        If you dont care about it, just commnet out these line.)
        opt.num_iter = int(opt.num_iter / opt.num_gpu)
        """