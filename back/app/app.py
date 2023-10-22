from TDA.datos import Datos

#crear el objeto
obj = Datos("back\\app\\archivosPrueba\EntradaMensajes.xml","back\\app\\archivosPrueba\EntradaConfiguracion.xml")

#leer un archivo
obj.leerMensajes()

#leer un archivo numero N
obj.path[0] = "back\\app\\archivosPrueba\EntradaMensajes2.xml"
obj.leerMensajes()

#leer configuraciones
obj.leerConfiguraciones()

#leer un archivo nuero N
obj.path[1] = "back\\app\\archivosPrueba\EntradaConfiguracion2.xml"
obj.leerConfiguraciones()


print("")