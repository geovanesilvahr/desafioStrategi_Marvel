from flask import request, render_template
from flask_restplus import Resource, fields

from models.herois import HeroiModel
from schemas.heroi import HeroiSchema

from server.instance import server

heroi_ns = server.heroi_ns
heroi_schema = HeroiSchema()
heroi_list_schema = HeroiSchema(many=True)
api = server.api

ITEM_NOT_FOUND = 'Heroi not Found'

item = heroi_ns.model('Heroi', {
    'nome': fields.String(description='Nome do Heroi'),
    'descricao': fields.String(description='Descricao do Heroi'),
    'imagem': fields.String(description='Imagem do Heroi')
})

class Heroi(Resource):

    def get(self, id):
        heroi_data = HeroiModel.find_by_id(id)
        if heroi_data:
            return heroi_schema.dump(heroi_data), 200
        return {'message': ITEM_NOT_FOUND}, 404

    @heroi_ns.expect(item)
    def put(self, id):
        heroi_data = HeroiModel.find_by_id(id)
        heroi_json = request.get_json()

        heroi_data.descricao = heroi_json['descricao']
        heroi_data.imagem = heroi_json['imagem']
        heroi_data.nome = heroi_json['nome']

        heroi_data.save_to_db()
        return heroi_schema.dump(heroi_data), 200

    def delete(self, id):
        heroi_data = HeroiModel.find_by_id(id)
        if heroi_data:
            heroi_data.delete_from_db()
            return '', 204
        return {'message': ITEM_NOT_FOUND}, 404

class HeroiList(Resource):

    def get(self):
        return heroi_list_schema.dump(HeroiModel.find_all()), 200   

    @heroi_ns.expect(item)
    @heroi_ns.doc('Create an Item')
    def post(self):
        heroi_json = request.get_json()
        heroi_data = heroi_schema.load(heroi_json)
        heroi_data.save_to_db()

        return heroi_schema.dump(heroi_data), 201
