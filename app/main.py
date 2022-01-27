from flask import Flask,request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.server.server import Server

app = Flask(__name__)

s1=Server(app)

# Import models
from app.models.gasConcentration import GasConcentration

# Get db object
db=s1.getDatabaseObject()

# Create tables in the database
db.create_all()



@app.route("/", methods=["POST"])
def hello():

    print(request.json['lastname'])

    name=request.args.get("name")
    print(name)

    return "Hello, World!"
