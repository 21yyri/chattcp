import socket
from threading import Thread

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 9999))

username = input('Insira seu nome de usuário: ').strip().lower()

def sendMessage():
    while True:
        msg = input()
        if msg == 'quit':
            cliente.close()
            break

        msg = f'{username}: {msg}'
        cliente.send(msg.encode())

def recvMessage():
    while True:
        server_msg = cliente.recv(1024).decode()
        print(server_msg)

threadRecv = Thread(target=recvMessage)
threadRecv.start()

threadSend = Thread(target=sendMessage)
threadSend.start()
threadSend.join()