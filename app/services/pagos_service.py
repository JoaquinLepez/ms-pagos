from ..repository import PagoRepository
from app.models import Pago

repository = PagoRepository()

class PagoService:

    def all(self) -> list[Pago]:
        return repository.all()

    def save(self, pago: Pago) -> Pago:
        return repository.save(pago)
    
    def delete(self, id: int) -> bool:
        pago = self.find(id)
        if pago:
            repository.delete(pago)
            return True
        else:
            return False
    
    def find(self, id: int) -> Pago:
        return repository.find(id)