import customtkinter as ctk
from PIL import Image

class LoginPage(ctk.CTkFrame):
    def __init__(self, master, login_callback=None):
        """
        master: riferimento al MainView
        login_callback: funzione da chiamare quando si clicca "Login"
        """
        super().__init__(master)

        # Imposto layout a griglia per questa pagina (1 colonna, 3 righe)
        self.grid_rowconfigure(0, weight=1)  # spazio sopra il titolo
        self.grid_rowconfigure(1, weight=0)  # titolo
        self.grid_rowconfigure(2, weight=1)  # spazio fra titolo e bottoni
        self.grid_rowconfigure(3, weight=0)  # bottoni
        self.grid_rowconfigure(4, weight=1)  # spazio sotto i bottoni
        self.grid_columnconfigure(0, weight=1)

        # Titolo grande e centrato
        title_label = ctk.CTkLabel(
            self,
            text="Login",
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color="#ffffff"
        )
        title_label.grid(row=1, column=0, pady=(20, 10), sticky="n")