import customtkinter as ctk

class LoginWindow(ctk.CTk):
    def __init__(self, app):
        super().__init__()
        self.appChat = app
        self.title("Login")
        self.geometry("300x130")

        self.nomeLabel = ctk.CTkLabel(self, text="Insira o nome a ser usado no chat.")
        self.nomeLabel.pack(pady=5)

        self.entryName = ctk.CTkEntry(self)
        self.entryName.pack(pady=2)

        self.botaoLogin = ctk.CTkButton(self, text="Definir", command=self.get_name)
        self.botaoLogin.pack(pady=0)
        
        self.entryName.bind("<Return>", lambda event : self.getName())
        self.botaoLogin.bind("<Return>", lambda event : self.getName())

        self.botaoLogin.focus_set()
    def fechar_login(self):
        self.destroy()

    def get_name(self):
        user_name = self.entryName.get().strip()
        if user_name:
            self.appChat.show_chat(username=user_name)
