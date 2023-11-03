import os
from app.TDA.datos import Datos

#crear el objeto
obj = Datos("","")

def leerMensajes(path):
    global obj
    obj.path[0] = path
    obj.leerMensajes()

def leerConfig(path):
    global obj
    obj.path[1] = path
    obj.leerConfiguraciones()

def limpiarDatos():
    global obj
    obj.inicilizar()
    os.remove("back\\app\\informacion\\MensajesDB.xml")
    os.remove("back\\app\\informacion\\PalabrasDB.xml")

def estaVacion():
    global obj
    return obj.vacio()

def documentacion():
    filepath = "Documentacion_Proyecto3_IPC2_202200075.pdf"
    os.system(f"start {filepath}")

def devovlerHas(fechas):
    global obj
    return obj.has(fechas)

def devovlerMen(fechas):
    global obj
    return obj.men(fechas)

def devovlerSent(fechas):
    global obj
    return obj.sent(fechas)