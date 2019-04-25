from models.distritos import DistritoModel
from flask_restful import Resource

from shapely import wkt
from shapely.geometry import mapping

class ListaDistritos(Resource):
    def get(self):
        list_distritos = []
        for distrit in DistritoModel.query.all():
            distrit = distrit.json()
            distrit["geometry"] = mapping(wkt.loads(distrit["geometry"]))
            list_distritos.append(distrit)
        return {"distritos":list_distritos}

        #return {"distritos": list(map(lambda x: x.json(), DistritoModel.query.all()))}