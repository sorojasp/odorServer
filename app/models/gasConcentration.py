from app.server.server import Server
from sqlalchemy.orm import backref
from app.models.ubication import Ubication


server=Server()
db=server.getDatabaseObject()


"""
Tutorial sqlalchemy
https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#one-to-many-relationships
"""

class GasConcentration(db.Model):
    __tablename__ = 'gasConcentration'
    id = db.Column(db.Integer, primary_key=True)
    NH3=db.Column(db.Float)
    CO2=db.Column(db.Float)
    CH4=db.Column(db.Float)
    H2S=db.Column(db.Float)
    SO2=db.Column(db.Float)
    temperature=db.Column(db.Float)
    humidity=db.Column(db.Float)
    dateTime=db.Column(db.DateTime)
    ubication_id = db.Column(db.Integer, db.ForeignKey('ubication.id'),
        nullable=False)


    def __init__(self, NH3, CO2, CH4, H2S, SO2, temperature, humidity, dateTime, ubication_id):
        self.NH3=NH3
        self.CO2=CO2
        self.CH4=CH4
        self.H2S=H2S
        self.SO2=SO2
        self.temperature=temperature
        self.humidity=humidity
        self.dateTime=dateTime
        self.ubication_id=ubication_id