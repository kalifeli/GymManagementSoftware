
from typing import List, Optional
from GestioneClienti.daos.IClienteDao import IClienteDAO
from GestioneClienti.model.Cliente import Cliente
from utils.firebase_client import get_firestore_client

class ClienteDaoFirebase(IClienteDAO):

    def __init__(self):
        self.client = get_firestore_client()
        self.collection = self.client.collection("clienti")

    def aggiungi_cliente(self, cliente: Cliente):
        cliente_dict = cliente.to_dict()
        # Aggiungi il documento e ottieni il riferimento
        doc_ref, _ = self.collection.add(cliente_dict)
        cliente.id = doc_ref.id
        # Aggiorna il campo id sia nel documento Firestore che nel model
        doc_ref.update({"id": cliente.id})


    def elimina_cliente(self, cliente_id: int) -> bool:
        try:
            self.collection.document(cliente_id).delete()
            return True
        except Exception as e:
            print(f"Error deleting cliente: {e}")
            return False

    def get_cliente_by_id(self, cliente_id: int) -> Optional[Cliente]:
        doc = self.collection.document(cliente_id).get()
        if doc.exists:
            return Cliente.from_dict(doc.to_dict())
        return None

    def get_all_clienti(self) -> List[Cliente]:
        docs = self.collection.stream()
        clienti = []
        for doc in docs:
            print("Documento trovato:", doc.id, doc.to_dict())  # DEBUG
            data = doc.to_dict()
            if data:
                data['id'] = doc.id
                clienti.append(Cliente(**data))
        return clienti
