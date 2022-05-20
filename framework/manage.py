import argparse
import os
import signal
import subprocess
import sys

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

        print(args)
        cmd = METHODS[args.method] + [args.port]
        # sp = subprocess.Popen(
        #     cmd,
        #     stdout=subprocess.PIPE,
        #     shell=True,
        #     preexec_fn=os.setsid,
        # )
        # os.killpg(os.getpgid(sp.pid), signal.SIGTERM)
    except KeyError:
        print('This method is not available.')
        sys.exit(-1)
    except ValueError:
        print(
            'Only a number can be specified as a port.\n'
            'Port number must be in the range of numbers [1024 : 65535].'
        )
        sys.exit(-1)


if __name__ == '__main__':
    parse_commandline()
