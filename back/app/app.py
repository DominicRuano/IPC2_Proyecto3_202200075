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