from flask import request, jsonify, Flask
from flask_cors import CORS
from app.app import *


app = Flask(__name__)
CORS(app)

@app.route("/")
def getHome():
    return jsonify({"message": "ipc2 desde un get ahora mismo"})

@app.route('/grabarMensajes', methods=['POST'])
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

@app.route('/grabarPalabras', methods=['POST'])
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

@app.route('/limpiarDatos', methods=['POST'])
def borrarDatos():
    try:
        limpiarDatos()
        return jsonify({"message": "Se inicializo con exito"})
    except:
        return jsonify({"message": "Se produjo un error, es posible que la DB ya este vacia"})

@app.route('/estaVacio', methods=['POST'])
def siEstaVacio():
    try:
        if estaVacion():
            return jsonify({"message": "Vacio"})
        else:
            return jsonify({"message": "No esta Vacio"})
    except:
        return jsonify({"message": "Error"})
if __name__ == '__main__':
    app.run(debug=True, port=3050)