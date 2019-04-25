from db import db

class DistritoModel(db.Model):

    __tablename__ = "distritos"

    ds_codigo = db.Column(db.Integer, primary_key=True, nullable=False)
    ds_nome = db.Column(db.String)
    geometry = db.Column(db.String)

    def __init__(self, ds_codigo, ds_nome, geometry):
        self.ds_codigo = ds_codigo
        self.ds_nome = ds_nome
        self.geometry = geometry

    def json(self):
        return {"ds_codigo":self.ds_codigo, "ds_nome":self.ds_nome, 
                "geometry":self.geometry}