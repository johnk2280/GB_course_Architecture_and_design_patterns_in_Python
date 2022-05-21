import argparse
import os
import signal
import subprocess
import sys
from typing import List

from logger import LOGGER
from settings import DEFAULT_ADDRESS
from settings import DEFAULT_PORT

METHODS = {
    'runserver': ['python3', 'server.py'],
}


def get_command(method: str) -> List[str]:
    try:
        return METHODS[method]
    except KeyError:
        raise


def parse_command_line() -> None:

    # TODO: реализовать через argparse

    addr = DEFAULT_ADDRESS
    prt = DEFAULT_PORT
    args = sys.argv
    try:
        method = args[1]
        cmd = get_command(method)
    except IndexError:
        LOGGER.info('Необходимо указать метод и (опционально) его аргументы.')
        sys.exit(-1)
    except KeyError:
        LOGGER.info('Указанный метод отсутствует.')
        sys.exit(-1)

    if '-a' in args:
        try:
            addr = args[args.index('-a') + 1]
        except IndexError:
            LOGGER.info(
                'После параметра \'a\'- необходимо указать адрес, '
                'который будет слушать сервер.',
            )
            sys.exit(-1)

    cmd += ['-a', addr]
    if '-p' in args:
        try:
            prt = int(args[args.index('-p') + 1])
            if prt < 1024 or prt > 65535:
                raise ValueError
        except IndexError:
            LOGGER.info(
                'После параметра -\'p\' необходимо указать номер порта.',
            )
            sys.exit(-1)
        except ValueError:
            LOGGER.info(
                'В качестве порта может быть указано только число в диапазоне'
                ' от 1024 до 65535.',
            )
            sys.exit(-1)

    cmd += ['-p', str(prt)]
    try:
        process = subprocess.Popen(cmd)
        process.wait()
    except KeyboardInterrupt:
        sys.exit(-1)

    return


if __name__ == '__main__':
    parse_command_line()
