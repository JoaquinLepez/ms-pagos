from ..repository import PagoRepository
from app.models import Pago
from app import cache

repository = PagoRepository()

class PagoService:

    def all(self) -> list[Pago]:
        result = cache.get('pagos')
        if result is None:
            result = repository.all()
            cache.set('pagos', result, timeout=15)
        return result

    def add(self, pago: Pago) -> Pago:
        pago = repository.add(pago)
        cache.set(f'pago_{pago.id}', pago, timeout=15)
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