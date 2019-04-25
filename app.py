from flask import Flask,request
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_restful import Api
import os

from resources.escolas import ListaEscolas
from resources.distritos import ListaDistritos
from resources.udhs import ListaUDHs

app = Flask(__name__)

#Database
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:ghoti5349@localhost:5433/escolas"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)
CORS(app)
ma = Marshmallow(app)
#init db

api.add_resource(ListaEscolas, "/escolas")
api.add_resource(ListaDistritos, "/distritos")
api.add_resource(ListaUDHs, "/udhs")


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)