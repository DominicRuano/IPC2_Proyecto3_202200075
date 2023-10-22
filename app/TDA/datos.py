import xml.etree.ElementTree as ET
from TDA.palabras import Palabras
from TDA.mensaje import Mensaje
import re

fechaRE = r'\b\d{2}/\d{2}/\d{4}\b'


class Datos():
    def __init__(self, path) -> None:
        self.root = ET.parse(path).getroot()
        self.mensajes = []
        self.palabras = Palabras()
    
    def leerMensajes(self):
        for a in self.root.findall("MENSAJES"):
            for mensaje in a.findall("MENSAJE"):
                fecha = mensaje.find("FECHA")
                fecha = re.findall(fechaRE, fecha.text)
                contenido = mensaje.find("TEXTO").text
                self.mensajes.append(Mensaje(fecha, contenido.replace("  ", "").replace("\n", "")))