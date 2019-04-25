from models.escolas import EscolaModel
from flask_restful import Resource


class ListaEscolas(Resource):
    def get(self):
        return {"escolas": list(map(lambda x: x.json(), EscolaModel.query.all()))}
    
