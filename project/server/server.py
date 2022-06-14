import sys
from socket import AF_INET
from socket import SOCK_STREAM
from socket import SOL_SOCKET
from socket import SO_REUSEADDR
from socket import socket
from typing import Tuple, List

from project.logger import LOGGER

from project.settings import DEFAULT_ADDRESS
from project.settings import DEFAULT_PORT

from project.server.server import Request

from app import app


class Server:
    logger = LOGGER
    address: str
    port: int

    def __init__(self, addr, prt, app):
        self.address = addr
        self.port = prt
        self.application = app

        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sock.bind((self.address, self.port))
        self.sock.listen()

    def get_data(self):
        # TODO: Распарсить данные и передать на точку входа
        pass

    def _parse_request(self, request_str: str) -> Request:
        request_data = request_str.split('\r\n')
        method, route, version = self._parse_request_line(request_data[0])
        headers = self._parse_headers(request_data[1:])
        return Request(method, route, version, headers)

    def _parse_request_line(self, rl: str) -> Tuple[str, str, str]:
        method, route, version = rl.split(' ')
        return method, route, version

    def _parse_query_string(self, route: str) -> dict:
        pass

    def _parse_headers(self, request_headers: List) -> dict:
        headers = {
            'HTTP_' + el[0].upper(): el[1] for el in map(
                lambda x: x.split(': '),
                request_headers,
            ) if len(el) > 1
        }
        return headers

    def create_response(self, status, headers):
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
                request = self._parse_request(data)
                self.logger.info('[%s] - %s ', request.method, request.route)
                environ = {
                    'REQUEST_METHOD': request.method,
                    'PATH_INFO': request.route,
                }
                environ.update(request.headers)
                self.application(environ, self.create_response)
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
    server = Server(address, port, app)
    server.run()
