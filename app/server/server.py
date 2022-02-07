from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app.shared.singletonMeta.singletonMeta import SingletonMeta
from flask import Flask


class Server(metaclass=SingletonMeta):

    port:str="3306"
    host:str="199.79.62.144"
    user:str="ingnova1_stiven"
    password:str="#Stiven1911"
    database:str="ingnova1_sr7nose"
    app=None
    db=None
    ma=None

    def __init__(self,app=None):
        self.app = app
        self.__setDatabase()
        self.__setDatabaseObject()
        self.__setMarshmallowObject()


    def __setDatabase(self):
        self.app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    def __setDatabaseObject(self):
        self.db = SQLAlchemy(self.app)

    def __setMarshmallowObject(self):
        self.ma = Marshmallow(self.app)

    def getDatabaseObject(self):
        return self.db

    def getMarshmallowObject(self):
        return self.ma

    def getAppObject(self):
        return self.app
