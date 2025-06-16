import firebase_admin
from firebase_admin import firestore
from .IContabilitaDao import IContabilitaDao
from GestioneContabilita.model.Entrata import Entrata
from GestioneContabilita.model.Uscita import Uscita


db = firestore.client()

class ContabilitaDaoFirebase(IContabilitaDao):

    def aggiungi_entrata(self, entrata: Entrata):
        doc_ref = db.collection('entrate').document()
        doc_ref.set(entrata.to_dict())

    def get_entrate(self):
        docs = db.collection('entrate').stream()
        return [Entrata.from_dict(doc.id, doc.to_dict()) for doc in docs]

    def aggiorna_entrata(self, entrata_id, nuovi_dati):
        db.collection('entrate').document(entrata_id).update(nuovi_dati)

    def elimina_entrata(self, entrata_id):
        db.collection('entrate').document(entrata_id).delete()

    def aggiungi_uscita(self, uscita: Uscita):
        doc_ref = db.collection('uscite').document()
        doc_ref.set(uscita.to_dict())

    def get_uscite(self):
        docs = db.collection('uscite').stream()
        return [Uscita.from_dict(doc.id, doc.to_dict()) for doc in docs]

    def aggiorna_uscita(self, uscita_id, nuovi_dati):
        db.collection('uscite').document(uscita_id).update(nuovi_dati)

    def elimina_uscita(self, uscita_id):
        db.collection('uscite').document(uscita_id).delete()
