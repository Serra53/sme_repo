from db import db

class EscolaModel(db.Model):

    __tablename__ = "escolas_sp"

    CODINEP = db.Column(db.Integer, primary_key=True, nullable=False)
    NOMESC = db.Column(db.String)
    ENDERECO = db.Column(db.String)
    BAIRRO = db.Column(db.String)
    TIPOESC = db.Column(db.String)

    IDEB_2007_EF1 = db.Column(db.String)
    IDEB_2009_EF1 = db.Column(db.String)
    IDEB_2011_EF1 = db.Column(db.String)
    IDEB_2013_EF1 = db.Column(db.String)
    IDEB_2015_EF1 = db.Column(db.String)
    IDEB_2017_EF1 = db.Column(db.String)

    IDEB_2007_EF2 = db.Column(db.String)
    IDEB_2009_EF2 = db.Column(db.String)
    IDEB_2011_EF2 = db.Column(db.String)
    IDEB_2013_EF2 = db.Column(db.String)
    IDEB_2015_EF2 = db.Column(db.String)
    IDEB_2017_EF2 = db.Column(db.String)

    LATITUDE = db.Column(db.Float(precision=2))
    LONGITUDE = db.Column(db.Float(precision=2))

    PIOR_DESEMP = db.Column(db.Integer)
    Total_EF = db.Column(db.Float(precision=1))

    def __init__(self, CODINEP, NOMESC, ENDERECO, BAIRRO, TIPOESC,
                IDEB_2007_EF1, IDEB_2009_EF1, IDEB_2011_EF1, IDEB_2013_EF1, IDEB_2015_EF1, IDEB_2017_EF1,
                IDEB_2007_EF2, IDEB_2009_EF2, IDEB_2011_EF2, IDEB_2013_EF2, IDEB_2015_EF2, IDEB_2017_EF2,
                LATITUDE, LONGITUDE, PIOR_DESEMP, Total_EF):

        self.CODINEP = CODINEP
        self.NOMESC = NOMESC
        self.ENDERECO = ENDERECO
        self.BAIRRO = BAIRRO
        self.TIPOESC = TIPOESC
        self.IDEB_2007_EF1 = IDEB_2007_EF1
        self.IDEB_2009_EF1 = IDEB_2009_EF1
        self.IDEB_2011_EF1 = IDEB_2011_EF1
        self.IDEB_2013_EF1 = IDEB_2013_EF1
        self.IDEB_2015_EF1 = IDEB_2015_EF1
        self.IDEB_2017_EF1 = IDEB_2017_EF1

        self.IDEB_2007_EF2 = IDEB_2007_EF2
        self.IDEB_2009_EF2 = IDEB_2009_EF2
        self.IDEB_2011_EF2 = IDEB_2011_EF2
        self.IDEB_2013_EF2 = IDEB_2013_EF2
        self.IDEB_2015_EF2 = IDEB_2015_EF2
        self.IDEB_2017_EF2 = IDEB_2017_EF2

        self.LATITUDE = LATITUDE
        self.LONGITUDE = LONGITUDE
        self.PIOR_DESEMP = PIOR_DESEMP
        self.Total_EF = Total_EF     



    def json(self):
        return {"CODINEP":self.CODINEP, "NOMESC":self.NOMESC, 
                "ENDERECO":self.ENDERECO, "BAIRRO": self.BAIRRO,
                "TIPOESC":self.TIPOESC , "IDEB_2007_EF1":self.IDEB_2007_EF1,"IDEB_2009_EF1": self.IDEB_2009_EF1, 
                "IDEB_2013_EF1": self.IDEB_2013_EF1, "IDEB_2015_EF1": self.IDEB_2015_EF1 , "IDEB_2017_EF1": self.IDEB_2017_EF1,
                "IDEB_2007_EF2":self.IDEB_2007_EF2,"IDEB_2009_EF2": self.IDEB_2009_EF2, 
                "IDEB_2013_EF2": self.IDEB_2013_EF2, "IDEB_2015_EF2": self.IDEB_2015_EF2 , "IDEB_2017_EF2": self.IDEB_2017_EF2,
                "LATITUDE":self.LATITUDE, "LONGITUDE":self.LONGITUDE, "PIOR_DESEMP":self.PIOR_DESEMP, "Total_EF": self.Total_EF}