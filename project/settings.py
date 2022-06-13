import pathlib
from pathlib import Path
from typing import Dict

import yaml


def _load_config(path: pathlib.Path) -> Dict:
    with open(path) as f_obj:
        config = yaml.load(f_obj, Loader=yaml.FullLoader)

    return config


BASE_DIR = Path(__file__).resolve().parent
CONFIGS_DIR = BASE_DIR.joinpath('configs')

CONFIG = _load_config(CONFIGS_DIR.joinpath('config.yaml'))
LOGGER_CONFIG = _load_config(CONFIGS_DIR.joinpath('logger_config.yaml'))

DEFAULT_ADDRESS = CONFIG['SERVER']['defaults']['ip']
DEFAULT_PORT = CONFIG['SERVER']['defaults']['port']

PATH_TO_SERVER = BASE_DIR.joinpath('server.py')
PATH_TO_TEMPLATES = BASE_DIR.joinpath('framework/templates')
PATH_TO_DATABASE = BASE_DIR.joinpath('framework/database')
