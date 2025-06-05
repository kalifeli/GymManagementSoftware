
from dataclasses import dataclass
from datetime import date
from enum import Enum


class StatoAbbonamento(Enum):
    ATTIVO = "Attivo"
    SCADUTO = "Scaduto"
    SOSPESO = "Sospeso"


@dataclass
class Abbonamento:
    id: str = None
    cliente_id: str = None
    corso: str = ""
    pacchetto: str = ""
    data_inizio: str = date.today().strftime("dd-mm-yyyy")
    data_fine: str = date.today().strftime("dd-mm-yyyy")
    prezzo: float = 0.0
    saldato: bool = False
    stato: str = StatoAbbonamento.ATTIVO.value

    def to_dict(self):
        return {
            "id": self.id,
            "cliente_id": self.cliente_id,
            "corso": self.corso,
            "pacchetto": self.pacchetto,
            "data_inizio": self.data_inizio,
            "data_fine": self.data_fine,
            "prezzo": self.prezzo,
            "saldato": self.saldato,
            "stato": self.stato
        }

    @classmethod
    def from_dict(data):
        return Abbonamento(
            id=data.get("id"),
            cliente_id=data.get("cliente_id"),
            corso=data.get("corso"),
            pacchetto=data.get("pacchetto"),
            data_inizio=data.get("data_inizio"),
            data_fine=data.get("data_fine"),
            prezzo=data.get("prezzo"),
            saldato=data.get("saldato"),
            stato=data.get("stato")
        )
    
