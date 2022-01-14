from flask import Flask,request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def hello():
    name=request.args.get("name")
    print(name)

    return "Hello, World!"
