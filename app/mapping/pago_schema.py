from app.models import Pago
from marshmallow import fields, Schema, post_load

class PagoSchema(Schema):
    id = fields.Integer(dump_only=True)
    producto_id= fields.Integer(required=True)
    precio = fields.Float(required=True)
    medio_pago = fields.String(required=True, validate=fields.Length(min=1, max=60))

    @post_load
    def make_data(self, data, **kwargs):
        return Pago(**data)