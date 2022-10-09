from flask import Flask,request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.server.server import Server
from flask_cors import CORS, cross_origin


from datetime import datetime
import pytz
from pytz import timezone

#import
import json

app = Flask(__name__)

s1=Server(app)

# Import models
from app.models.ubication import Ubication
from app.models.gasConcentration import GasConcentration


#import schemas
from app.schemas.gasConcentration import GasConcentrationSchema


from app.schemas.ubication import UbicationSchema

# import or operator from sqlalchemy

from sqlalchemy import or_

#get objet of gas concentration schema
gas_schema=GasConcentrationSchema()
gases_schema = GasConcentrationSchema(many=True)

#get objet of gas concentration schema
ubication_schema=UbicationSchema()
ubications_schema = UbicationSchema(many=True)

# Get db object
db=s1.getDatabaseObject()
engine_container = db.get_engine(app)

# Create tables in the database
db.create_all()


#set cors

CORS(s1.getAppObject())





@app.route("/gasConcentrations", methods=["POST"])
def post_gasConcentrations():

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
        lat=request.args.get("H")
        lng=request.args.get("I")


        # find ubication if already exist
        ubication=Ubication.query.filter(Ubication.lat==lat).filter(Ubication.lng==lng).first()

        if ubication==None:
            ubication=Ubication(lat,lng)
            s1.getDatabaseObject().session.add(ubication)
            s1.getDatabaseObject().session.commit()

        NH3=request.args.get("A")
        CO2=request.args.get("B")
        CH4=request.args.get("C")
        H2S=request.args.get("D")
        SO2=request.args.get("E")
        temperature=request.args.get("F")
        humidity=request.args.get("G")
        probe_mode=request.args.get("probe_mode")
        probe_mode_boolean=False

        if probe_mode==0:
            probe_mode_boolean=False
        elif probe_mode==1:
            probe_mode_boolean=True


        dateTime=datetime.now(tz = timezone('America/Bogota'))

        print("new ubication:", ubication)

        new_gas_concentation=GasConcentration(NH3, CO2, CH4, H2S, SO2, temperature, humidity, dateTime, ubication.id,probe_mode_boolean)
        s1.getDatabaseObject().session.add(new_gas_concentation)
        s1.getDatabaseObject().session.commit()

        return gas_schema.jsonify(new_gas_concentation)

    except Exception as error:
        print(error)
        return "Error!"

    finally:
        print("pass for finally =)")
        cleanup(db.session)



@app.route("/gasConcentrations", methods=["GET"])
def get_gasConcentrations():

    try:

        format_data = "%Y-%m-%dT%H:%M:%S"
        # Using strptime with datetime we will format
        # string into datetime


        #get datetime
        datetime_start = datetime.strptime(request.args.get("datetimeStart"), format_data)
        datetime_end =  datetime.strptime(request.args.get("datetimeEnd"), format_data)


        query_filter=GasConcentration.query
        query=None

        #get probe mode

        probe_mode_str=request.args.get("probe_mode")
        probe_mode_bool=False

        if probe_mode_str=='1':
            probe_mode_bool=True
        elif probe_mode_str=='0':
            probe_mode_bool=False
        else:
            probe_mode_bool=False

        # filter with probe mode and dateTime
        query=query_filter.filter(GasConcentration.dateTime>=datetime_start).filter(GasConcentration.dateTime<=datetime_end).filter(GasConcentration.probe_mode==probe_mode_bool)

        # get ubications
        ubications_list:list=[]
        ids_ubications:list=[]
        location_in_database=False



        for ubications in request.args.get("ubications").split(";"):
            print(ubications)
            lat_lng=ubications.split(",")
            ubications_list.append({
                               "lat":lat_lng[0].split(":")[1],
                               "lng":lat_lng[1].split(":")[1]
            })
            query_ubication = Ubication.query.filter(Ubication.lat==lat_lng[0].split(":")[1]).filter(Ubication.lng==lat_lng[1].split(":")[1]).first()

            if query_ubication != None:
                location_in_database=True
                ids_ubications.append(query_ubication.id)

        query=query.filter(GasConcentration.ubication_id.in_(ids_ubications))


        if location_in_database==True:
            concentrations=query.all()
        else:
            concentrations=[]

        print("result f query: ", query.all())

        return gases_schema.jsonify(query.all())


    except Exception as error:

        response={
                "result":False,
                "detail":str(error)
                }
        return json.dumps(response, indent = 4)
    finally:
        print("pass for finally =)")
        cleanup(db.session)




@app.route("/nodeUbications", methods=["GET"])
def get_nodeUbications():

    try:


        all_ubicationNodes = Ubication.query.all()
        return ubications_schema.jsonify(all_ubicationNodes)


    except Exception as error:

        response={
                "result":False,
                "detail":str(error)
                }
        return json.dumps(response, indent = 4)

    finally:
        print("pass for finally =)")
        cleanup(db.session)



def cleanup(session):
    """
    This method cleans up the session object and also closes the connection pool using the dispose method.
    """

    session.close()
    engine_container.dispose()


if __name__ == '__main__':
    app.run()
