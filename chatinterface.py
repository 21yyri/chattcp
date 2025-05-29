from typing import Tuple
import customtkinter as ctk
from cliente import Client

'''
threadRecv = Thread(target=recvMessage)
threadRecv.start()

threadSend = Thread(target=sendMessage)
threadSend.start()
threadSend.join()
'''
cliente = Client()

class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("400x150")
        self.entryName = ctk.CTkEntry(self, )
        self.entryName.pack(pady=10)

        self.botaoLogin = ctk.CTkButton(self, text="Enviar", command=self.getName)
        self.botaoLogin.pack()
    def getName(self):
        username = self.entryName.get()
        cliente.username = username

        self.nomeLabel = ctk.CTkLabel(self, text=f"{cliente.username}")
        self.nomeLabel.pack()


login = LoginWindow()
login.mainloop()