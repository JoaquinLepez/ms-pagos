import os
import unittest
from redis import Redis
from app import create_app, cache, db
from app.models import Pago
from app.services import PagoService

service = PagoService()

class RedisTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        
        self.app_context.push()
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    # test connection to Redis
    def test_redis_connection(self):
        redis = Redis(
            host=self.app.config['CACHE_REDIS_HOST'],
            port=self.app.config['CACHE_REDIS_PORT'],
            db=self.app.config['CACHE_REDIS_DB'],
            password=self.app.config['CACHE_REDIS_PASSWORD']
        )
        self.assertTrue(redis.ping())
    
    def test_cache_after_adding_pago(self):
        pago = Pago(producto_id=1, precio=100, medio_pago='efectivo')
        pago1 = service.add(pago)
        
        cached_pago = cache.get(f'pago_{pago1.id}')
        
        
        self.assertIsNotNone(cached_pago) 
        self.assertEqual(cached_pago.producto_id, pago1.producto_id)
        self.assertEqual(cached_pago.precio, pago1.precio)
        self.assertEqual(cached_pago.medio_pago, pago1.medio_pago)

if __name__ == '__main__':
    unittest.main()