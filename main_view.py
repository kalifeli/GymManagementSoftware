import customtkinter as ctk
from PIL import Image
from GestioneClienti.controller.cliente_controller import ClienteController
from GestioneClienti.view.AggiungiAbbonamentoPage import AggiungiAbbonamentoPage
from GestioneClienti.view.AggiungiClientePage import AggiungiClientePage
from GestioneClienti.view.ClientiPage import ClientiPage
from GestioneClienti.view.InfoCliente import InfoClientePage
from GestioneClienti.view.ModificaClientePage import ModificaClientePage
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
            show_info_cliente_callback=self.show_info_cliente_page
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

    def show_info_cliente_page(self, cliente):
        controller = ClienteController(self)
        self.info_cliente_page = InfoClientePage(
            self.container,
            cliente=cliente,
            controller=controller, 
            back_callback=self.show_clienti_page,
            aggiungi_abbonamento_callback=lambda: self.show_aggiungi_abbonamento_page(cliente),
            modifica_cliente_callback=lambda: self.show_modifica_cliente_page(cliente)
        )
        self.info_cliente_page.controller = ClienteController(self.info_cliente_page)
        self.info_cliente_page.grid(row=0, column=0, sticky="nsew")
        self.info_cliente_page.tkraise()

    def show_aggiungi_abbonamento_page(self, cliente):
        self.aggiungi_abbonamento_page = AggiungiAbbonamentoPage(
            self.container,
            cliente=cliente,
            controller=ClienteController(self),  
            back_callback=lambda: self.show_info_cliente_page(cliente),
        )
        self.aggiungi_abbonamento_page.controller = ClienteController(self.aggiungi_abbonamento_page)
        self.aggiungi_abbonamento_page.grid(row=0, column=0, sticky="nsew")
        self.aggiungi_abbonamento_page.tkraise()
    
    def show_modifica_cliente_page(self, cliente):
        self.modifica_cliente_page = ModificaClientePage(
            self.container,
            controller=ClienteController(self),
            cliente=cliente,
            back_callback=lambda: self.show_info_cliente_page(cliente)
        )
        self.modifica_cliente_page.controller = ClienteController(self.modifica_cliente_page)
        self.modifica_cliente_page.grid(row=0, column=0, sticky="nsew")
        self.modifica_cliente_page.tkraise()
    

