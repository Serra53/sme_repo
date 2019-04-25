from models.udhs import UDHModel
from flask_restful import Resource

from shapely import wkt
from shapely.geometry import mapping

class ListaUDHs(Resource):
    def get(self):
        list_UDHs = []
        for udh in UDHModel.query.all():
            udh = udh.json()
            udh["geometry"] = mapping(wkt.loads(udh["geometry"]))
            list_UDHs.append(udh)
        return {"udhs":list_UDHs}
