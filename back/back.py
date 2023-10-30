from flask import request, jsonify, Flask
from flask_cors import CORS
from app.app import *


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

@app.route('/subir-mensajes', methods=['POST'])
def subir_mensajes():
    if 'archivo' not in request.files:
        return jsonify({"message": "No se envio ningun archivo"})

    archivo = request.files['archivo']

    if archivo.filename == '':
        return 'No se seleccionó ningún archivo'
    
    archivo.filename = "back\\app\\enviadoApi\\" + archivo.filename
    archivo.save(archivo.filename)
    leerMensajes(archivo.filename)
    
    return jsonify({"message": "El archivo se subio exitosamente"})

@app.route('/subir-palabras', methods=['POST'])
def subir_Palabras():
    if 'archivo' not in request.files:
        return jsonify({"message": "No se envio ningun archivo"})

    archivo = request.files['archivo']

    if archivo.filename == '':
        return 'No se seleccionó ningún archivo'
    
    archivo.filename = "back\\app\\enviadoApi\\" + archivo.filename
    archivo.save(archivo.filename)
    leerConfig(archivo.filename)
    
    return jsonify({"message": "El archivo se subio exitosamente"})

if __name__ == '__main__':
    app.run(debug=True, port=3050)