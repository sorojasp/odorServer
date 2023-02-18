

from sqlalchemy.orm import backref


def definition_ubication(db):
    class Ubication(db.Model):
        __tablename__ = 'ubication'
        id = db.Column(db.Integer, primary_key=True)
        lat=db.Column(db.String(30))
        lng=db.Column(db.String(30))

        def __init__(self,lat,lng):
            self.lat=lat
            self.lng=lng


