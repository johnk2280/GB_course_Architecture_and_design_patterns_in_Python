import argparse
import subprocess

import os
import sys
from time import sleep

METHODS = {
    'runserver': ['python3', 'server.py'],
}


def parse_commandline() -> None:
    parser = argparse.ArgumentParser(
        description='Framework manager',
    )
    parser.add_argument(
        'method',
        type=str,
        help='method',
    )
    parser.add_argument(
        '-p',
        '--port',
        type=str,
        default='8000',
        help='port: default - 8000',
    )

    try:
        args = parser.parse_args()
        if int(args.port) < 1024 or int(args.port) > 65535:
            raise ValueError

        sp = subprocess.Popen(METHODS[args.method] + [args.port])
    except KeyError:
        print('This method is not available.')
        sys.exit(-1)
    except ValueError:
        print(
            'Only a number can be specified as a port.\n'
            'Port number must be in the range of numbers [1024 : 65535].'
        )
        sys.exit(-1)



    return


if __name__ == '__main__':
    parse_commandline()