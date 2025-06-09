import socket

class Cliente:
    def __init__(self) -> None:    
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente.connect(('localhost', 9999))

        self.username = ''
    
    def enviar_bytes(self, msg):
        msg = f'{self.username}: {msg}'
        self.cliente.send(msg.encode())

    def receber_bytes(self):
        return f"{self.cliente.recv(1024).decode()}\n"
        
