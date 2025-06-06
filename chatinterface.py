import customtkinter as ctk
from models.cliente import Client
from threading import Thread

cliente = Client()

class App:
    def __init__(self):
        self.show_login()
    
    def show_login(self):
        self.loginWindow = LoginWindow(self)
        self.loginWindow.mainloop()

    def show_chat(self, username):
        self.loginWindow.destroy()
        cliente.username = username
        self.chatWindow = Chat()
        self.chatWindow.mainloop()

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

        self.enviar = ctk.CTkButton(self, text="Send", command=self.sendMsg)
        self.enviar.pack(side="right", padx=5)

        self.receberThread = Thread(target=self.recvMsg, daemon=True)
        self.receberThread.start()

    def sendMsg(self):
        msg = self.msgBox.get()
        if msg:
            cliente.sendMessage(msg)
            self.msgBox.delete(0, 'end')

    def recvMsg(self):
        while True:
            try:
                msg: str = cliente.recvMessage()

                self.chatDisplay.configure(state="normal")
                self.chatDisplay.insert("end", msg)
                self.chatDisplay.see("end")
                self.chatDisplay.configure(state="disabled")
            except Exception as E:
                print(E)
                break

    def fecharChat(self):
        self.running = False
        self.destroy()


class LoginWindow(ctk.CTk):
    def __init__(self, app):
        super().__init__()
        self.appChat = app
        self.title("Login")
        self.geometry("400x150")

        self.nomeLabel = ctk.CTkLabel(self, text="Insira o nome a ser usado no chat.")
        self.nomeLabel.pack(pady=5)

        self.entryName = ctk.CTkEntry(self)
        self.entryName.pack(pady=5)

        self.botaoLogin = ctk.CTkButton(self, text="Definir", command=self.getName)
        self.botaoLogin.pack()

    def fecharLogin(self):
        self.destroy()

    def getName(self):
        user_name = self.entryName.get().strip()
        if user_name:
            self.appChat.show_chat(username=user_name)


App()