import socket
from socket import AF_INET
from socket import SOCK_STREAM

server_sock = socket.socket(AF_INET, SOCK_STREAM)
server_address = ('127.0.0.1', 8002)
server_sock.bind(server_address)
server_sock.listen(5)


while True:
    print('Сервер готов к работе на адресе http://127.0.0.1:8002')
    client, address = server_sock.accept()
    print(f'Подключился {address}')
    data = client.recv(1024).decode()
    print(f'Получены данные {data}')
    client.sendall(b'Hello from my server\n')
    client.close()
