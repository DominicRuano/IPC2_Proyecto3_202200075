import xml.etree.ElementTree as ET
from app.TDA.palabras import Palabras
from app.TDA.mensaje import Mensaje
import re

fechaRE = r'\b\d{2}/\d{2}/\d{4}\b'
hashtagRE = r'#(.*?)#'
mencionesRE = r'@(\w+)'

class Datos():
    def __init__(self, *args) -> None:
        self.path = [*args]
        self.mensajes = []
        self.palabras = Palabras()
        self.leerDB()

    def vacio(self):
        if self.path == ['',''] and self.mensajes == [] and self.palabras.positivas == [] and self.palabras.positivasRechazadas == [] and self.palabras.negativas == [] and self.palabras.negativasRechazadas == []:
            return False
        else:
            return True

    def inicilizar(self):
        self.path = ['','']
        self.mensajes = []
        self.palabras.positivas = []
        self.palabras.positivasRechazadas = []
        self.palabras.negativas = []
        self.palabras.negativasRechazadas = []

    def leerDB(self):
        try:
            root = ET.parse("back\\app\\informacion\MensajesDB.xml").getroot()
            for a in root.findall("MENSAJES"):
                for mensaje in a.findall("MENSAJE"):
                    fecha = mensaje.find("FECHA")
                    fecha = re.findall(fechaRE, fecha.text)
                    contenido = mensaje.find("TEXTO").text.replace("\t", "").replace("\n", "")
                    self.mensajes.append(Mensaje(fecha[0], contenido))
        except:
            print("No se detecto una DB de mensajes")
            self.mensajes = []

        try:
            root = ET.parse("back\\app\\informacion\PalabrasDB.xml").getroot()
            for a in root.findall("diccionario"):
                for mensaje in a.findall("positivas"):
                    for palabra in mensaje.findall("palabra"):
                        self.palabras.positivas.append(palabra.text)
                for mensaje in a.findall("negativas"):
                    for palabra in mensaje.findall("palabra"):
                        self.palabras.negativas.append(palabra.text)
                for mensaje in a.findall("positivasrechazadas"):
                    for palabra in mensaje.findall("palabra"):
                        self.palabras.positivasRechazadas.append(palabra.text)
                for mensaje in a.findall("negativasrechazadas"):
                    for palabra in mensaje.findall("palabra"):
                        self.palabras.negativasRechazadas.append(palabra.text)
            
        except:
            print("No se detecto una DB de palabras")
            self.palabras.positivas = []
            self.palabras.positivasRechazadas = []
            self.palabras.negativas = []
            self.palabras.negativasRechazadas = []

    def leerMensajes(self):
        root = ET.parse(self.path[0]).getroot()
        for a in root.findall("MENSAJES"):
            for mensaje in a.findall("MENSAJE"):
                fecha = mensaje.find("FECHA")
                fecha = re.findall(fechaRE, fecha.text)
                contenido = mensaje.find("TEXTO").text.replace("  ", "").replace("\n", "")
                if self.BuscarMensaje(fecha, contenido):
                    self.mensajes.append(Mensaje(fecha[0], contenido))
                #else:
                    #print(f"Mensaje rechazado: \nFecha: {fecha[0]} \nContenido: {contenido}")
        self.guardarMensajes()

    def BuscarMensaje(self, fecha, contenido):
        try:
            for msj in self.mensajes:
                if msj.fecha.lower() == fecha[0].lower() and msj.texto.lower() == contenido.lower():
                    return False
            return True
        except:
            print("Se detecto un error inesperado, uno de los mensajes no se agregara.")

    def guardarMensajes(self):
        with open("back\\app\\informacion\MensajesDB.xml", "w") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write("<config>\n")
            f.write("\t<MENSAJES>\n")
            for mensaje in self.mensajes:
                f.write("\t\t<MENSAJE>\n")
                f.write(f"\t\t\t<FECHA>{mensaje.fecha}</FECHA>\n")
                f.write(f"\t\t\t<TEXTO>\n\t\t\t\t{mensaje.texto}\n\t\t\t</TEXTO>\n")
                f.write("\t\t</MENSAJE>\n")
            f.write("\t</MENSAJES>\n")
            f.write("</config>")

    def leerConfiguraciones(self):
        root = ET.parse(self.path[1]).getroot()
        for palabra in root.find("sentimientos_positivos"):
            if self.buscarConfiguracion(palabra.text, "positivas"):
                if self.buscarConfiguracion(palabra.text, "negativas"):
                    self.palabras.positivas.append(palabra.text)
                elif self.buscarConfiguracion(palabra.text, "positivasRechazadas"):
                    self.palabras.positivasRechazadas.append(palabra.text)

        for palabra in root.find("sentimientos_negativos"):
            if self.buscarConfiguracion(palabra.text, "negativas"):
                if self.buscarConfiguracion(palabra.text, "positivas"):
                    self.palabras.negativas.append(palabra.text)
                elif self.buscarConfiguracion(palabra.text, "negativasRechazadas"):
                        self.palabras.negativasRechazadas.append(palabra.text)
        self.guardarConfiguraciones()

    def buscarConfiguracion(self, valor, clave):
        if clave == "positivas":
            for palabra in self.palabras.positivas:
                if palabra.lower() == valor.lower():
                    return False
            return True
        elif clave == "negativas":
            for palabra in self.palabras.negativas:
                if palabra.lower() == valor.lower():
                    return False
            return True
        elif clave == "negativasRechazadas":
            for palabra in self.palabras.negativasRechazadas:
                if palabra.lower() == valor.lower():
                    return False
            return True
        elif clave == "positivasRechazadas":
            for palabra in self.palabras.positivasRechazadas:
                if palabra.lower() == valor.lower():
                    return False
            return True

    def guardarConfiguraciones(self):
        with open("back\\app\\informacion\PalabrasDB.xml", "w") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write("<config>\n")
            f.write("\t<diccionario>\n")
            f.write("\t\t<positivas>\n")
            for palabra in self.palabras.positivas:
                f.write(f"\t\t\t<palabra>{palabra}</palabra>\n")
            f.write("\t\t</positivas>\n")
            f.write("\t\t<negativas>\n")
            for palabra in self.palabras.negativas:
                f.write(f"\t\t\t<palabra>{palabra}</palabra>\n")
            f.write("\t\t</negativas>\n")
            f.write("\t\t<positivasrechazadas>\n")
            for palabra in self.palabras.positivasRechazadas:
                f.write(f"\t\t\t<palabra>{palabra}</palabra>\n")
            f.write("\t\t</positivasrechazadas>\n")
            f.write("\t\t<negativasrechazadas>\n")
            for palabra in self.palabras.negativasRechazadas:
                f.write(f"\t\t\t<palabra>{palabra}</palabra>\n")
            f.write("\t\t</negativasrechazadas>\n")
            f.write("\t</diccionario>\n")
            f.write("</config>")

    def has(self, fechas):
        valores = fechas.split(',')
        agregar = []
        regrear = []
        valor = ""
        for fecha in valores:
            for mensaje in self.mensajes:
                if fecha.replace("-", "/") == mensaje.fecha:
                    hastags = re.findall(hashtagRE, mensaje.texto)
                    for a in hastags:
                        indice = -1
                        # Recorre la lista y busca la palabra
                        for i, diccionario in enumerate(agregar):
                            if a in diccionario:
                                indice = i
                                break
                        if indice != -1:
                            agregar[indice][a] += 1
                        else:
                            agregar.append({f"{a}": 1})
            for i, diccionario in enumerate(agregar):
                valor += f"<ul>{diccionario}</ul>"
            regrear.append(f"<li>{fecha}</li>\n {valor}")
            agregar = []
            valor = ""
        return regrear

    def men(self, fechas):
        valores = fechas.split(',')
        agregar = []
        regrear = []
        valor = ""
        for fecha in valores:
            for mensaje in self.mensajes:
                if fecha.replace("-", "/") == mensaje.fecha:
                    hastags = re.findall(mencionesRE, mensaje.texto)
                    for a in hastags:
                        indice = -1
                        # Recorre la lista y busca la palabra
                        for i, diccionario in enumerate(agregar):
                            if a in diccionario:
                                indice = i
                                break
                        if indice != -1:
                            agregar[indice][a] += 1
                        else:
                            agregar.append({f"{a}": 1})
            for i, diccionario in enumerate(agregar):
                valor += f"<ul>{diccionario}</ul>"
            regrear.append(f"<li>{fecha}</li>\n {valor}")
            agregar = []
            valor = ""
        return regrear

    def sent(self, fechas):
        valores = fechas.split(',')
        contadorP = 0
        contadorP2 = 0
        contadorN = 0
        contadorN2 = 0
        ContadorNN2 = 0
        regrear = []
        valor = ""
        for fecha in valores:
            for mensaje in self.mensajes:
                if fecha.replace("-", "/") == mensaje.fecha:
                    for palabra in self.palabras.positivas:
                        if fecha.replace("-", "/") == mensaje.fecha:
                            hastags = re.findall(palabra, mensaje.texto)
                            for a in hastags:
                                contadorP += 1
                    for palabra in self.palabras.negativas:
                        if fecha.replace("-", "/") == mensaje.fecha:
                            hastags = re.findall(palabra, mensaje.texto)
                            for a in hastags:
                                contadorN += 1
                    if contadorP > contadorN:
                        contadorP2 += 1
                    elif contadorN > contadorP:
                        contadorN2 +=1
                    else:
                        ContadorNN2 +=1
                    contadorN = 0
                    contadorP = 0
            valor += "<ul> {'" + f"Positivos' : {contadorP2}" + "'}</ul>"
            valor += "<ul> {'" + f"Negativos' : {contadorN2}" + "'}</ul>"
            valor += "<ul> {'" + f"Neutros' : {ContadorNN2}" + "'}</ul>"
            regrear.append(f"<li>{fecha}</li>\n {valor}")
            valor = ""
            contadorP2 = 0
            contadorN2 = 0
            ContadorNN2 = 0
        return regrear

