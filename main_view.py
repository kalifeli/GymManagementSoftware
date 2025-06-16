import customtkinter as ctk
from PIL import Image
from GestioneClienti.controller.cliente_controller import ClienteController
from GestioneClienti.view.AggiungiClientePage import AggiungiClientePage
from GestioneClienti.view.ClientiPage import ClientiPage
from HomePage import HomePage
from GestioneContabilita.view.ContabilitaPage import ContabilitaPage
from GestioneContabilita.view.EntratePage import EntratePage
from GestioneContabilita.controller.contabilita_controller import ContabilitaController
from GestioneContabilita.view.AggiungiEntrataPage import AggiungiEntrataPage
from GestioneContabilita.view.AggiungiUscitaPage import AggiungiUscitaPage
from GestioneContabilita.view.GraficoContabilitaPage import GraficoContabilitaPage

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

        self.pagina_corrente = None  # 👈 gestore della pagina corrente

        self.home_page = HomePage(
            self.container,
            show_clienti_callback=self.show_clienti_page,
            show_contabilità_callback=self.show_contabilita_page
        )
        self.home_page.grid(row=0, column=0, sticky="nsew")

        self.show_home_page()

    def show_home_page(self):
        if self.pagina_corrente:
            self.pagina_corrente.destroy()
        self.pagina_corrente = self.home_page
        self.home_page.tkraise()

    def show_clienti_page(self):
        if self.pagina_corrente:
            self.pagina_corrente.destroy()

        self.pagina_corrente = ClientiPage(
            self.container,
            controller=None,
            back_callback=self.show_home_page,
            show_aggiungi_cliente_callback=self.show_aggiungi_cliente_page,
            show_info_cliente_callback=None
        )
        self.pagina_corrente.controller = ClienteController(self.pagina_corrente)
        self.pagina_corrente.grid(row=0, column=0, sticky="nsew")
        self.pagina_corrente.tkraise()

    def show_aggiungi_cliente_page(self):
        if self.pagina_corrente:
            self.pagina_corrente.destroy()

        self.pagina_corrente = AggiungiClientePage(
            self.container,
            controller=None,
            back_callback=self.show_clienti_page
        )
        self.pagina_corrente.controller = ClienteController(self.pagina_corrente)
        self.pagina_corrente.grid(row=0, column=0, sticky="nsew")
        self.pagina_corrente.tkraise()

    def show_contabilita_page(self):
        if self.pagina_corrente:
            self.pagina_corrente.destroy()

        self.pagina_corrente = ContabilitaPage(
            self.container,
            back_callback=self.show_home_page,
            show_aggiungi_entrata_callback=self.show_aggiungi_entrata_page,
            show_aggiungi_uscita_callback=self.show_aggiungi_uscita_page,
            show_grafico_contabilita_callback=self.show_grafico_contabilita_page
        )
        self.pagina_corrente.controller = ContabilitaController(self.pagina_corrente)
        self.pagina_corrente.grid(row=0, column=0, sticky="nsew")
        self.pagina_corrente.tkraise()

    def show_entrate_page(self):
        if self.pagina_corrente:
            self.pagina_corrente.destroy()

        self.pagina_corrente = EntratePage(
            self.container,
            controller=ContabilitaController(),
            back_callback=self.show_home_page
        )
        self.pagina_corrente.grid(row=0, column=0, sticky="nsew")
        self.pagina_corrente.tkraise()

    def show_aggiungi_entrata_page(self):
        if self.pagina_corrente:
            self.pagina_corrente.destroy()

        self.pagina_corrente = AggiungiEntrataPage(
            self.container,
            controller=None,
            back_callback=self.show_contabilita_page
        )
        self.pagina_corrente.controller = ContabilitaController(self.pagina_corrente)
        self.pagina_corrente.grid(row=0, column=0, sticky="nsew")
        self.pagina_corrente.tkraise()

    def show_aggiungi_uscita_page(self):
        if self.pagina_corrente:
            self.pagina_corrente.destroy()

        self.pagina_corrente = AggiungiUscitaPage(
            self.container,
            controller=None,
            back_callback=self.show_contabilita_page
        )
        self.pagina_corrente.controller = ContabilitaController(self.pagina_corrente)
        self.pagina_corrente.grid(row=0, column=0, sticky="nsew")
        self.pagina_corrente.tkraise()

    def torna_a_visualizza_entrate(self):
        if self.pagina_corrente:
            self.pagina_corrente.destroy()
        self.show_contabilita_page()
        self.contabilita_page.visualizza_entrate()

    def torna_a_visualizza_uscite(self):
        if self.pagina_corrente:
            self.pagina_corrente.destroy()
        self.show_contabilita_page()
        self.contabilita_page.visualizza_uscite()

    def show_grafico_contabilita_page(self):
        if self.pagina_corrente:
            self.pagina_corrente.destroy()

        self.pagina_corrente = GraficoContabilitaPage(
            self.container,
            controller=None,
            back_callback=self.show_contabilita_page
        )
        self.pagina_corrente.controller = ContabilitaController(self.pagina_corrente)
        self.pagina_corrente.grid(row=0, column=0, sticky="nsew")
        self.pagina_corrente.tkraise()
