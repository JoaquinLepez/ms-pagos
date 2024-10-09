from typing import List
from app import db
from app.models import Pago

class PagoRepository:
    def all(self) -> List[Pago]:
        return db.session.query(Pago).all()
    
    def save(self, pago: Pago) -> Pago:
        db.session.add(pago)
        db.session.commit()
        return pago
    
    def find(self, id: int) -> Pago:
        return db.session.query(Pago).filter(Pago.id == id).one_or_none()

    def delete(self, pago: Pago) -> None:
        db.session.delete(pago)
        db.session.commit()
        return None