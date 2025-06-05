from GestioneClienti.model.Cliente import Cliente
from GestioneClienti.daos.ClienteDaoFirebase import ClienteDaoFirebase
from GestioneClienti.model.Abbonamento import Abbonamento



class ClienteController:
    def __init__(self, view):
        self.view = view
        self.dao = ClienteDaoFirebase()

        self.load_clienti()

    def load_clienti(self):
        try:
            clienti = self.dao.get_all_clienti()
            print("Clienti caricati:", clienti)  # DEBUG
            self.view.visualizzaClienti(clienti)
        except Exception as e:
            print(f"Errore nel caricamento dei clienti: {str(e)}")

    def aggiungi_cliente(self, cliente):
        """
        Aggiunge un nuovo cliente tramite la DAO e ricarica la lista dei clienti.
        """
        try:
            self.dao.aggiungi_cliente(cliente)
            self.load_clienti()
        except Exception as e:
            print(f"Errore nell'aggiunta del cliente: {str(e)}")

    # Abbonamenti
    def get_abbonamenti_by_cliente_id(self, cliente_id: str):
        """
        Recupera tutti gli abbonamenti associati a un cliente specifico e li restituisce come lista di oggetti Abbonamento.
        """
        try:
            abbonamenti_dict = self.dao.fetch_abbonamenti_by_cliente_id(cliente_id)
            abbonamenti = [Abbonamento.from_dict(a) for a in abbonamenti_dict]
            return abbonamenti
        except Exception as e:
            print(f"Errore nel caricamento degli abbonamenti: {str(e)}")
            return []
        
    def trova_cliente_by_nome(self, nome: str):
        """
        Trova i clienti che corrispondono al nome specificato e li restituisce come lista di oggetti Cliente.
        """
        try:
            clienti_dict = self.dao.trova_cliente_by_nome(nome)
            clienti = [Cliente.from_dict(c['id'], c) for c in clienti_dict]
            return clienti
        except Exception as e:
            print(f"Errore nella ricerca del cliente: {str(e)}")
            return []
