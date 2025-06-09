import socket
from threading import Thread, Lock

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind(('localhost', 9999))
except Exception as E:
    print(E)


server.listen(15)

clientes = []
lock = Lock()

def broadcast(mensagem: bytearray):
    print(mensagem)
    with lock:
        for cliente in clientes:
            try:
                cliente.send(mensagem)
            except:
                clientes.remove(cliente)

def handleCli(cliente: socket.socket):
    while True:
        try:
            msg = cliente.recv(1024)
            if not msg:
                break
            broadcast(msg)
        except:
            with lock:
                clientes.remove(cliente)
                cliente.close()

def handleConn():
    while True:
        client, addr = server.accept()
        with lock:
            clientes.append(client)
        print(f'Conexão estabelecida com {addr}')

        threadBc = Thread(target=handleCli, args=(client,))
        threadBc.start()


print('Iniciando servidor.')
handleConn()
