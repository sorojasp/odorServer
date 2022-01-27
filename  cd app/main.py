from flask import Flask,request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

@app.route("/", methods=["POST"])
def hello():
    engine = create_engine('mysql+pymysql://ingnova1_stiven:#Stiven1911@199.79.62.144:3306/ingnova1_recyapp')
    print("engine:", engine)
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()

    print("session:", session)

    name=request.args.get("name")
    print(name)

    return "Hello, World!"
