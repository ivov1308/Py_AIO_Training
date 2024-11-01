import logging.config
import yaml

from logging_settings import logging_config
from module_1 import main

with open('logging_config.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(logging_config)

main()
