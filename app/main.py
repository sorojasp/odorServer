from flask import Flask,request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.server.server import Server



from datetime import datetime

app = Flask(__name__)

s1=Server(app)

# Import models
from app.models.ubication import Ubication
from app.models.gasConcentration import GasConcentration

#import schemas
from app.schemas.gasConcentration import GasConcentrationSchema

#get objet of gas concentration schema
gas_schema=GasConcentrationSchema()
gases_schema = GasConcentrationSchema(many=True)

# Get db object
db=s1.getDatabaseObject()

# Create tables in the database
db.create_all()




@app.route("/gasConcentrations", methods=["POST"])
def post():

    """
        data to probe  NH3=200.38&CO2=10000.38&CH4=100000.99&H2S=100.25&SO2=236.88&T=200.38&H=200.388

        ?NH3=200.38&CO2=10000.38&CH4=100000.99
        &H2S=100.25&SO2=236.88&T=200.38&H=200.388

        &A=200.38&B=10000.38&C=100000.99&H=4.697540
        &D=100.25E=236.88&F=20.38&G=20.388&I=-74.114441
    """

    try:

        #print(request.json['lastname']) get data from body

        #Ubication
        lat=float(request.args.get("H"))
        lng=float(request.args.get("I"))

        new_ubication=Ubication(lat,lng)



        NH3=float(request.args.get("A"))
        CO2=float(request.args.get("B"))
        CH4=float(request.args.get("C"))
        H2S=float(request.args.get("D"))
        SO2=float(request.args.get("E"))
        temperature=float(request.args.get("F"))
        humidity=float(request.args.get("G"))
        probe_mode=float(request.args.get("probe_mode"))
        probe_mode_boolean=False

        if probe_mode==0:
            probe_mode_boolean=False
        elif probe_mode==1:
            probe_mode_boolean=True


        dateTime=datetime.now()

        s1.getDatabaseObject().session.add(new_ubication)
        s1.getDatabaseObject().session.commit()

        print("new ubication:", new_ubication)




        new_gas_concentation=GasConcentration(NH3, CO2, CH4, H2S, SO2, temperature, humidity, dateTime, new_ubication.id,probe_mode_boolean)
        s1.getDatabaseObject().session.add(new_gas_concentation)
        s1.getDatabaseObject().session.commit()


        return gas_schema.jsonify(new_gas_concentation)

    except Exception as error:
        print(error)
        return "Error!"


@app.route("/gasConcentrations", methods=["GET"])
def get():

    try:

        concentrations=GasConcentration.query.filter_by(humidity=33).all()
        print(concentrations)
        return gases_schema.jsonify(concentrations)

    except Exception as error:
        return str(error)
