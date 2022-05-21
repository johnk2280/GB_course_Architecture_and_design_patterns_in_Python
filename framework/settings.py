import pathlib
from pathlib import Path
from typing import Dict

import yaml


BASE_DIR = Path(__file__).resolve().parent
CONFIGS_DIR = BASE_DIR.joinpath('configs')


def _load_config(path: pathlib.Path) -> Dict:
    with open(path) as f_obj:
        config = yaml.load(f_obj, Loader=yaml.FullLoader)

    return config


CONFIG = _load_config(CONFIGS_DIR.joinpath('config.yaml'))
LOGGER_CONFIG = _load_config(CONFIGS_DIR.joinpath('logger_config.yaml'))
