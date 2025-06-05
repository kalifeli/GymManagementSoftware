from abc import ABC, abstractmethod
from typing import List, Optional
from GestioneClienti.model.Cliente import Cliente

class IClienteDAO(ABC):
    @abstractmethod
    def aggiungi_cliente(self, cliente: Cliente):
        pass

    @abstractmethod
    def elimina_cliente(self, cliente_id: int) -> bool:
        pass

    @abstractmethod
    def get_cliente_by_id(self, cliente_id: int) -> Optional[Cliente]:
        pass

    @abstractmethod
    def get_all_clienti(self) -> List[Cliente]:
        pass
