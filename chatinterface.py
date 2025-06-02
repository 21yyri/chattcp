import customtkinter as ctk
from models.cliente import Client
from threading import Thread


cliente = Client()
cliente.username = "Yuri"

class Chat(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(f"Chat - {cliente.username}")
        self.geometry("800x600")
        self.resizable(False, False)
        self.running = True

        self.protocol("WM_DELETE_WINDOW", self.fecharChat)

        self.chatDisplay = ctk.CTkTextbox(self, state="disabled", wrap="word")
        self.chatDisplay.pack(fill="both", expand=True, padx=20, pady=20)

        self.msgBox = ctk.CTkEntry(self, width=700, height=30)
        self.msgBox.pack(side="left", fill='x', padx=10, pady=10)
        self.msgBox.bind("<Return>", lambda event : self.sendMsg())

        self.enviar = ctk.CTkButton(self, text="Enviar", command=self.sendMsg)
        self.enviar.pack(side="right", padx=5)

        self.receberThread = Thread(target=self.recvMsg, daemon=True)
        self.receberThread.start()

    def sendMsg(self):
        msg = self.msgBox.get()
        if msg:
            cliente.sendMessage(msg)
            self.msgBox.delete(0, 'end')
            self.atualizaChat(msg)


    def recvMsg(self):
        while self.running:
            try:
                msg = cliente.recvMessage()
                if msg:
                    self.atualizaChat(msg)
            except Exception as E:
                print(E)
                break

    def atualizaChat(self, msg):
        self.chatDisplay.configure(state="normal")
        self.chatDisplay.insert("end", f'{cliente.username}: {msg}' + '\n')
        self.chatDisplay.see("end")
        self.chatDisplay.configure(state="disabled")

    def fecharChat(self):
        self.running = False
        self.destroy()


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

    def fecharLogin(self):
        self.deiconify()
        self.destroy()

    def abrirChat(self):
        self.withdraw()
        chat = Chat()
        chat.protocol("WM_DELETE_WINDOW", self.fecharLogin)
        chat.deiconify()

    def getName(self):
        username = self.entryName.get().strip()
        if username:
            cliente.username = username
            self.abrirChat()


login = LoginWindow()
login.mainloop()