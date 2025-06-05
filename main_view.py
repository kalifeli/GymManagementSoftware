import customtkinter as ctk
from PIL import Image
from GestioneClienti.controller.cliente_controller import ClienteController
from GestioneClienti.view.AggiungiClientePage import AggiungiClientePage
from GestioneClienti.view.ClientiPage import ClientiPage
from HomePage import HomePage

class MainView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gym Management Software")
        self.geometry("1024x768")

        self.container = ctk.CTkFrame(self)
        self.container.grid(row=0, column=0, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Istanzia direttamente la HomePage
        self.home_page = HomePage(self.container, show_clienti_callback=self.show_clienti_page)
        self.home_page.grid(row=0, column=0, sticky="nsew")

        self.show_home_page()

    def show_home_page(self):
        self.home_page.tkraise()

   


    def show_clienti_page(self):
        self.clienti_page = ClientiPage(
            self.container,
            controller=None,  # Il controller sarà impostato dopo
            back_callback=self.show_home_page,
            show_aggiungi_cliente_callback= self.show_aggiungi_cliente_page,
            show_info_cliente_callback=None
        )
        self.clienti_page.controller = ClienteController(self.clienti_page)
        self.clienti_page.grid(row=0, column=0, sticky="nsew")
        self.clienti_page.tkraise()

    def show_aggiungi_cliente_page(self):
        self.aggiungi_cliente_page = AggiungiClientePage(
            self.container,
            controller= None,
            back_callback=self.show_clienti_page
        )
        self.aggiungi_cliente_page.controller = ClienteController(self.aggiungi_cliente_page)
        self.aggiungi_cliente_page.grid(row=0, column=0, sticky="nsew")
        self.aggiungi_cliente_page.tkraise()

    

