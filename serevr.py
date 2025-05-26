import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind(('localhost', 9999))
except Exception as E:
    print(E)


server.listen(15)

clientes = []

def broadcast(client):
    while True:
        msg = client.recv(1024)

        if not msg:
            clientes.remove(client)
            break

        print(msg.decode())

def handleConn():
    while True:
        client, addr = server.accept()
        clientes.append(client)

        print(f'Conexão estabelecida com {addr}.')

        threadBc = Thread(target=broadcast, args=(client,))
        threadBc.start()


threadConn = Thread(target=handleConn)
threadConn.start()
threadConn.join()