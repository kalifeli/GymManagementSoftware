
from typing import List, Optional
from GestioneClienti.daos.IClienteDao import IClienteDAO
from GestioneClienti.model.Abbonamento import Abbonamento
from GestioneClienti.model.Cliente import Cliente
from GestioneClienti.model.Corso import Corso
from utils.firebase_client import get_firestore_client

class ClienteDaoFirebase(IClienteDAO):

    def __init__(self):
        self.client = get_firestore_client()
        self.collection_clienti = self.client.collection("clienti")
        self.collection_abbonamenti = self.client.collection("abbonamenti")
        self.collection_corsi = self.client.collection("corsi")


    def aggiungi_cliente(self, cliente: Cliente):
        try:

            # Controllo se esiste già un cliente con la stessa email
            query = self.collection_clienti.where("email", "==", cliente.email).stream()
            for doc in query:
                print(f"Cliente già presente con email: {cliente.email}")
                return False  # Cliente già esistente, non lo aggiunge
            
            doc_ref = self.collection_clienti.document()
            cliente.id = doc_ref.id
            dati = cliente.to_dict()
            dati['id'] = cliente.id  # Associa l'ID del cliente al dizionario
            doc_ref.set(dati)  # Aggiungi il documento con i dati del cliente
            print(f"Cliente aggiunto: {cliente.id}")
            return True
        except Exception as e:
            print(f"Errore aggiungendo cliente: {e}")
            return False


    def elimina_cliente(self, cliente_id: int) -> bool:
        try:
            self.collection_clienti.document(cliente_id).delete()
            return True
        except Exception as e:
            print(f"Errore eliminando cliente: {e}")
            return False

    def get_cliente_by_id(self, cliente_id: int) -> Optional[Cliente]:
        doc = self.collection_clienti.document(cliente_id).get()
        if doc.exists:
            return Cliente.from_dict(doc.to_dict())
        return None

    def get_all_clienti(self) -> List[Cliente]:
        docs = self.collection_clienti.stream()
        clienti = []
        for doc in docs:
            #print("Documento trovato:", doc.id, doc.to_dict())
            data = doc.to_dict()
            if data:
                data['id'] = doc.id
                clienti.append(Cliente(**data))
        return clienti
    
    def get_abbonamenti_by_cliente_id(self, cliente_id) -> Optional[List[Abbonamento]]:
        print(f"Query abbonamenti per id_cliente={cliente_id}")  # DEBUG
        docs = self.collection_abbonamenti.where("id_cliente", "==", cliente_id).stream()
        abbonamenti = []
        for doc in docs:
            print("Abbonamento trovato:", doc.id, doc.to_dict())  # DEBUG
            data = doc.to_dict()
            if data:
                data['id'] = doc.id
                # Conversione delle date in stringa
                if 'data_inizio' in data and hasattr(data['data_inizio'], 'isoformat'):
                    data['data_inizio'] = data['data_inizio'].isoformat()
                if 'data_fine' in data and hasattr(data['data_fine'], 'isoformat'):
                    data['data_fine'] = data['data_fine'].isoformat()
                abbonamenti.append(Abbonamento.from_dict(data))
        return abbonamenti if abbonamenti else None
    
    def add_abbonamento_to_cliente(self, cliente_id: str, abbonamento: Abbonamento):
        """
        Aggiunge un nuovo documento nella collezione "abbonamenti". Dopo il 'add',
        assegniamo all'oggetto 'abbonamento.id' e l'id del cliente.
        """
        try:
            doc_ref = self.collection_abbonamenti.document()
            abbonamento.id = doc_ref.id  # Imposta l'ID dell'abbonamento
            dati = abbonamento.to_dict()
            dati['id'] = abbonamento.id
            dati['id_cliente'] = cliente_id  # Associa l'abbonamento al cliente
            doc_ref.set(dati)  # Aggiungi il documento con i dati dell'abbonamento
            print(f"Abbonamento aggiunto: {abbonamento.id} per cliente {cliente_id}")

            return True
        except Exception as e:
            print(f"Error adding abbonamento: {e}")
            return False 

    def elimina_abbonamento(self, abbonamento_id: str) -> bool:
        try:
            self.collection_abbonamenti.document(abbonamento_id).delete()
            return True
        except Exception as e:
            print(f"Error deleting abbonamento: {e}")
            return False
    
    def get_all_corsi(self) -> List[Corso]:
        """
        Recupera tutti i corsi disponibili.
        """
        docs = self.collection_corsi.stream()
        corsi = []
        for doc in docs:
            data = doc.to_dict()
            corsi.append(Corso.from_dict(data))
        return corsi

    
            