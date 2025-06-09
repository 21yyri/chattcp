import customtkinter as ctk
from login import LoginWindow
from chat import Chat, cliente

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

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


App()