import socket

class Client:
    def __init__(self) -> None:    
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente.connect(('localhost', 9999))

        self.username = ''
    
    def sendMessage(self, msg):
        msg = f'{self.username}: {msg}'
        self.cliente.send(msg.encode())

    def recvMessage(self):
        while True:
            mensagem = f"{self.cliente.recv(1024).decode()}\n"
            return mensagem

