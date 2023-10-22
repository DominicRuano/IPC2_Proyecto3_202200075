from TDA.datos import Datos

#crear el objeto
obj = Datos("app\\archivosPrueba\EntradaMensajes.xml","app\\archivosPrueba\EntradaConfiguracion.xml")

#leer un archivo
obj.leerMensajes()

#leer un archivo numero N
obj.path[0] = "app\\archivosPrueba\EntradaMensajes2.xml"
obj.leerMensajes()

#leer configuraciones
obj.leerConfiguraciones()

print("")