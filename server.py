from ast import While
from email.errors import NoBoundaryInMultipartDefect
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname_ex, 1111))

server.listen()

clients = []
nicknames = []
banlist = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[client.index(client)]} says {message}")
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Подключился с адресом{str(address)}")

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024)
        nicknames.append(nickname)

        clients.append(client)

        print(f"Имя пользователя: {nickname}")
        broadcast(f"{nickname} connected to the server!\n".encode('utf-8'))
        client.send("Подключился к серверу".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
print("Сервер запущен...")
receive()
