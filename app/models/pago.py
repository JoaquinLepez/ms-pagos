from app import db

class Pago(db.Model):
    __tablename__ = 'pagos'
    # Atributos propios
    id: int = db.Column(db.Integer, primary_key = True, autoincrement = True)
    producto_id: str = db.Column(db.Integer, nullable = False)
    precio = db.Column(db.Float, nullable = False)
    medio_pago: str = db.Column(db.String(60), nullable = False)

