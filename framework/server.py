import sys
from socket import AF_INET
from socket import SOCK_STREAM
from socket import SOL_SOCKET
from socket import SO_REUSEADDR
from socket import socket
from typing import Tuple

from logger import LOGGER

from settings import DEFAULT_ADDRESS
from settings import DEFAULT_PORT


class Server:
    logger = LOGGER
    address: str
    port: int

    def __init__(self, addr, prt):
        self.address = addr
        self.port = prt

        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sock.bind((self.address, self.port))
        self.sock.listen()

    def get_data(self):
        pass

    def create_response(self):
        pass

    def run(self) -> None:
        self.logger.info(
            '\nJohnkTestServer version 0.1'
            '\nСервер разработки запущен на адресе http://%s:%s\n'
            'Для завершения работы сервера нажмите "Ctl+C".',
            self.address,
            self.port,
        )
        try:
            while True:
                client, addr = self.sock.accept()
                data = client.recv(2048).decode()
                self.logger.info('Получены данные:\n%s', data)
                response = b'Hello from server'
                client.sendall(response)
                client.close()
        except KeyboardInterrupt:
            self.logger.info('\nСервер остановлен.')
            sys.exit(-1)


def parse_command_line() -> Tuple[str, int]:

    # TODO: реализовать через argparse

    addr = DEFAULT_ADDRESS
    prt = DEFAULT_PORT
    args = sys.argv
    if '-a' in args:
        try:
            addr = args[args.index('-a') + 1]
        except IndexError:
            LOGGER.info(
                'После параметра \'a\'- необходимо указать адрес, '
                'который будет слушать сервер.',
            )
            sys.exit(-1)

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
                'В качестве порта может быть указано только число в диапазоне '
                'от 1024 до 65535.',
            )
            sys.exit(-1)

    return addr, prt


if __name__ == '__main__':
    address, port = parse_command_line()
    server = Server(address, port)
    server.run()
