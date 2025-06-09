import customtkinter as ctk
from threading import Thread
from cliente import Cliente

cliente = Cliente()

class Chat(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(cliente.username)
        self.geometry("800x500")
        self.resizable(False, False)

        self.isRodando: bool = True

        self.protocol("WM_DELETE_WINDOW", self.fechar_chat)

        self.chatDisplay = ctk.CTkTextbox(self, state="disabled", wrap="word")
        self.chatDisplay.pack(fill="both", expand=True, padx=20, pady=10)

        self.msgEntry = ctk.CTkEntry(self, width=680, height=30)
        self.msgEntry.pack(side="left", fill='x', padx=15, pady=5)
        self.msgEntry.bind("<Return>", lambda event : self.send_mensagem())

        self.enviar = ctk.CTkButton(self, text="Enviar", command=self.send_mensagem)
        self.enviar.pack(side="right", padx=5, pady=0)

        self.receberThread = Thread(target=self.receber_mensagem, daemon=True)
        self.receberThread.start()

    def send_mensagem(self):
        mensagem = self.msgEntry.get()
        if mensagem:
            cliente.enviar_bytes(mensagem)
            self.msgEntry.delete(0, 'end')

    def receber_mensagem(self):
        while True:
            try:
                mensagem: str = cliente.receber_bytes()
                self.atualizar_display(mensagem)

            except Exception as Erro:
                break

    def atualizar_display(self, mensagem):
        self.chatDisplay.configure(state="normal")
        self.chatDisplay.insert("end", mensagem)
        self.chatDisplay.see("end")
        self.chatDisplay.configure(state="disabled")

    def fechar_chat(self):
        self.isRodando = False
        self.destroy()