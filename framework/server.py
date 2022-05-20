import socket
from socket import AF_INET
from socket import SOCK_STREAM
from typing import Tuple

import argparse


def parse_commandline() -> Tuple[str, int]:
    addr = '127.0.0.1'
    port = 8000
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            'port',
            type=str,
        )
        args = parser.parse_args()
        print(args)
        addr = args.address
        port = int(args.port)
    except AttributeError:
        pass

    return addr, port


server_sock = socket.socket(AF_INET, SOCK_STREAM)
server_address = parse_commandline()
server_sock.bind(server_address)
server_sock.listen(5)

while True:
    print(f'Сервер готов к работе на адресе {server_address}')
    client, address = server_sock.accept()
    print(f'Подключился {address}')
    data = client.recv(1024).decode()
    print(f'Получены данные {data}')
    client.sendall(b'Hello from my server\n')
    client.close()
