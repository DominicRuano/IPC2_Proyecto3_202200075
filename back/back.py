from flask import request, jsonify, Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/', methods = ["POST"]) #por defecto es de tipo GET
def postHome():
    return jsonify({"message": "ipc2 desde un post"})

@app.route("/", methods = ["GET"])
def getHome():
    return jsonify({"message": "ipc2 desde un get ahora mismo"})

@app.route("/adduser", methods = ["POST"])
def addUser():
    if request.method == "POST":
        nombre = request.form["txbnombre"]
        passw = request.form["txbpass"]
        return jsonify({"messaje": "Usuario agregado","nombre":nombre, "password":passw})

@app.route("/adduserbybody", methods = ["POST"])
def addUserByBody():
    miCurso = request.json["curso"]
    miSeccion = request.json["seccion"]
    return jsonify({"Aamessage":"Curso agregado", "Curso": miCurso, "Seccion":miSeccion})

if __name__ == '__main__':
    app.run(debug=True, port=3050)