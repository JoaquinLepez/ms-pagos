import unittest, os
from app import create_app, db
from app.models import Pago
class PagoTestCase(unittest.TestCase):
    
    def setUp(self):
        # User
        self.IDPRODUCTO_PRUEBA = 1
        self.PRECIO_PRUEBA = 5656.3
        self.MEDIO_PAGO_PRUEBA = "Tarjeta"
    
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    def test_pago(self):
        pago = self.__get_pago()

        self.assertEqual(pago.producto_id, self.IDPRODUCTO_PRUEBA)
        self.assertEqual(pago.precio, self.PRECIO_PRUEBA)
        self.assertEqual(pago.medio_pago, self.MEDIO_PAGO_PRUEBA)

    def __get_pago(self):
        pago = Pago()
        pago.producto_id = self.IDPRODUCTO_PRUEBA
        pago.precio = self.PRECIO_PRUEBA
        pago.medio_pago = self.MEDIO_PAGO_PRUEBA

        return pago
    
if __name__ == '__main__':
    unittest.main()