import yaml
import logging.config
import logging


def read_log_config():
    log_conf_file = 'log_conf.yml'

    with open(log_conf_file, 'r') as file:
        log_config = yaml.safe_load(file.read())
        logging.config.dictConfig(log_config)

    logger = logging.getLogger('basicLogger')

    return logger
