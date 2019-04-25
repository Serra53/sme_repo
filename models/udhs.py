from db import db

class UDHModel(db.Model):

    __tablename__ = "udhs"

    UDH_ATLAS = db.Column(db.Integer, primary_key=True, nullable=False)
    geometry = db.Column(db.String)
    T_ANALF18M = db.Column(db.Float(precision=2))
    T_FBBAS = db.Column(db.Float(precision=2))
    T_FBFUND = db.Column(db.Float(precision=2))
    T_FBMED = db.Column(db.Float(precision=2))
    IDHM_E = db.Column(db.Float(precision=2))



    def __init__(self, UDH_ATLAS, geometry,T_ANALF18M, T_FBBAS,T_FBFUND,T_FBMED,IDHM_E):
        self.UDH_ATLAS = UDH_ATLAS
        self.T_ANALF18M = T_ANALF18M
        self.T_FBBAS = T_FBBAS
        self.T_FBFUND = T_FBFUND
        self.T_FBMED = T_FBMED
        self.IDHM_E = IDHM_E
        self.geometry = geometry



    def json(self):
        return {"udh_atlas":self.UDH_ATLAS,"t_analf18m": self.T_ANALF18M , "t_fbbas":self.T_FBBAS, 
                "t_fbfund":self.T_FBFUND, "t_fbmed":self.T_FBMED, "idhme":self.IDHM_E, 
                "geometry":self.geometry}