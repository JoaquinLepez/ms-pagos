from ..repository import PagoRepository
from app.models import Pago

repository = PagoRepository()

class PagoService:

    def all(self) -> list[Pago]: 
        result = repository.all()
        return result

    def add(self, pago: Pago) -> Pago:
        pago = repository.add(pago)
        return pago
    
    def delete(self, id: int) -> bool:
        pago = self.find(id)
        if pago:
            repository.delete(pago)
            return True
        else:
            return False
    
    def find(self, id: int) -> Pago:
        return repository.find(id)