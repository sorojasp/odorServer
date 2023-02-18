
from sqlalchemy.orm import backref




"""
Tutorial sqlalchemy
https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#one-to-many-relationships
"""


def definition_gasConcentration(db):
    class GasConcentration(db.Model):
        __tablename__ = 'gasConcentration'
        id = db.Column(db.Integer, primary_key=True)
        NH3=db.Column(db.String(20))
        CO2=db.Column(db.String(20))
        CH4=db.Column(db.String(20))
        H2S=db.Column(db.String(20))
        SO2=db.Column(db.String(20))
        temperature=db.Column(db.String(20))
        humidity=db.Column(db.String(20))
        dateTime=db.Column(db.DateTime)
        probe_mode=db.Column(db.Boolean)
        ubication_id = db.Column(db.Integer, db.ForeignKey('ubication.id'),
            nullable=False)


        def __init__(self, NH3, CO2, CH4, H2S, SO2, temperature, humidity, dateTime, ubication_id, probe_mode):
            self.NH3=NH3
            self.CO2=CO2
            self.CH4=CH4
            self.H2S=H2S
            self.SO2=SO2
            self.temperature=temperature
            self.humidity=humidity
            self.dateTime=dateTime
            self.ubication_id=ubication_id
            self.probe_mode=probe_mode
