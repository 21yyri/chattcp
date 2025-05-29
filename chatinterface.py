import customtkinter as ctk
from models.cliente import Client
from threading import Thread


cliente = Client()

class Chat(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(f"Chat - {cliente.username}")
        self.geometry("800x600")
        self.resizable(False, False)

        self.chatDisplay = ctk.CTkTextbox(self, state="disabled", wrap="word")
        self.chatDisplay.pack(fill="both", expand=True, padx=20, pady=20)

        self.msgBox = ctk.CTkEntry(self, width=700, height=30)
        self.msgBox.pack(side="left", fill='x', padx=10, pady=10)

        self.enviar = ctk.CTkButton(self, text="enviar", command=self.sendMsg)
        self.enviar.pack(side="right", padx=5)

        Thread(target=self.recvMsg).start()
    def sendMsg(self):
        msg = self.msgBox.get()
        cliente.sendMessage(msg)            

    def recvMsg(self):
        while True:
            msg = cliente.recvMessage()

            self.chatDisplay.configure(state="normal")
            self.chatDisplay.insert("end", msg)
            self.chatDisplay.see("end")
            self.chatDisplay.configure(state="disabled")

class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("400x150")

        self.nomeLabel = ctk.CTkLabel(self, text="Insira o nome a ser usado no chat.")
        self.nomeLabel.pack(pady=5)

        self.entryName = ctk.CTkEntry(self)
        self.entryName.pack(pady=5)

        self.botaoLogin = ctk.CTkButton(self, text="Enviar", command=self.getName)
        self.botaoLogin.pack()

    def getName(self):
        username = self.entryName.get().strip()
        if username:
            cliente.username = username
            Chat()
            self.after_cancel("all")
            self.destroy()

            
            


chat = LoginWindow()
chat.mainloop()