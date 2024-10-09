from flask import Blueprint, request
from .services import PagoService, ResponseBuilder
from .mapping import PagoSchema, ResponseSchema

response_schema = ResponseSchema()
pago_service = PagoService()
pago_schema = PagoSchema()

pago = Blueprint('pago', __name__)

@pago.route('/pagos', methods=['GET'])
def index():
    response_builder = ResponseBuilder()
    data = pago_schema.dump(pago_service.all(), many=True)
    response_builder.add_message("Pagos found").add_status_code(200).add_data(data)
    return response_schema.dump(response_builder.build()), 200

@pago.route('/pagos', methods=['POST'])
def add():
    response_builder = ResponseBuilder()
    pago = pago_schema.load(request.json)
    data = pago_schema.dump(pago_service.save(pago))
    response_builder.add_message("Pago added").add_status_code(201).add_data(data)
    return response_schema.dump(response_builder.build()), 201

@pago.route('/pagos/<int:id>', methods=['DELETE'])
def delete(id):
    response_builder = ResponseBuilder()
    data = pago_service.delete(id)
    if data:
        response_builder.add_message("Pago deleted").add_status_code(200).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Pago not found").add_status_code(404).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 404

