from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from requests import post, get
import requests

seInicializo = False
seCargoMensajes = False
seInformacion = False

def getInfo(request):
    return HttpResponse("Frontend: Estudiantes de ipc2")

def getReporte(request):
    url = "http://127.0.0.1:3050"
    Anwr = get(url)

    reporteName = "sentimiento de mensajes"
    descripcion = "Reporte de sentimiento de mensaje"
    conteo = [10, 20, 50, 54]
    existen = True

    objTemplate = loader.get_template("reporte.html")
    html = objTemplate.render({"existe": existen,"respuesta": Anwr.json(), "idNombre_reporte": reporteName, "descripcion": descripcion, "valores": conteo})
    return HttpResponse(html)

def inicio(request):
    objHTML = loader.get_template("Main.html")
    html = objHTML.render()
    return HttpResponse(html)

def resetearDatos(request):
    global seInicializo
    vacio = False
    try:
        api_url = 'http://127.0.0.1:3050/estaVacio'
        response = requests.post(api_url)

        if response.json()["message"] == "Vacio":
            # La solicitud se realizó con éxito
            vacio = True
        else:
            # La solicitud falló
            vacio = False
    except:
        pass

    objHTML = loader.get_template("resetearDatos.html")
    html = objHTML.render({"valor": seInicializo, "estaVacio": vacio})
    seInicializo = False
    return HttpResponse(html)

def buttonReset(request):
    try:
        global seInicializo
        api_url = 'http://127.0.0.1:3050/limpiarDatos'
        response = requests.post(api_url)

        if response.status_code == 200:
            # La solicitud se realizó con éxito
            seInicializo = True
            return redirect("http://127.0.0.1:8000/reset/")
        else:
            # La solicitud falló
            seInicializo = False
            return redirect("http://127.0.0.1:8000/reset/")
    except:
        return redirect("http://127.0.0.1:8000/reset/")

def cargarMensajes(request):
    global seCargoMensajes
    objHTML = loader.get_template("cargarMensajes.html")
    vacio = seCargoMensajes
    seCargoMensajes = False
    html = objHTML.render({"estaVacio": vacio})
    return HttpResponse(html)

@csrf_exempt
def buttonMensaje(request):
    global seCargoMensajes
    try:
            api_url = 'http://127.0.0.1:3050/grabarMensajes'

            # Verifica si se ha seleccionado un archivo
            if 'archivo' in request.FILES:
                archivo = request.FILES['archivo']

                # Configura la solicitud POST con el archivo adjunto
                files = {'archivo': archivo}

                # Realiza la solicitud POST a la API
                response = requests.post(api_url, files=files)
                if response.status_code == 200:
                    # La solicitud se realizó con éxito
                    seCargoMensajes = True
                    return redirect("http://127.0.0.1:8000/cargarMensajes/")
                else:
                    # La solicitud falló
                    return redirect("http://127.0.0.1:8000/cargarMensajes/")

            # Si no se seleccionó un archivo o hubo un error
            return redirect("http://127.0.0.1:8000/cargarMensajes/")

    except Exception as e:
        return HttpResponse(f'Error al enviar el archivo a la API: {str(e)}')

def cargarConfiguraciones(request):
    global seCargoMensajes
    objHTML = loader.get_template("cargarConfiguracion.html")
    html = objHTML.render({"estaVacio": seCargoMensajes })
    seCargoMensajes = False
    return HttpResponse(html)

@csrf_exempt
def buttonconfig(request):
    global seCargoMensajes
    try:
            api_url = 'http://127.0.0.1:3050/grabarPalabras'

            # Verifica si se ha seleccionado un archivo
            if 'archivo' in request.FILES:
                archivo = request.FILES['archivo']

                # Configura la solicitud POST con el archivo adjunto
                files = {'archivo': archivo}

                # Realiza la solicitud POST a la API
                response = requests.post(api_url, files=files)
                if response.status_code == 200:
                    # La solicitud se realizó con éxito
                    seCargoMensajes = True
                    return redirect("http://127.0.0.1:8000/cargarConfiguraciones/")
                else:
                    # La solicitud falló
                    return redirect("http://127.0.0.1:8000/cargarConfiguraciones/")

            # Si no se seleccionó un archivo o hubo un error
            return redirect("http://127.0.0.1:8000/cargarConfiguraciones/")

    except Exception as e:
        return HttpResponse(f'Error al enviar el archivo a la API: {str(e)}')

def consultarHastags(request):
    objHTML = loader.get_template("consultarHastags.html")
    html = objHTML.render()
    return HttpResponse(html)

def consultarMenciones(request):
    objHTML = loader.get_template("consultarMenciones.html")
    html = objHTML.render()
    return HttpResponse(html)

def consultarSentimiento(request):
    objHTML = loader.get_template("consultarSentimiento.html")
    html = objHTML.render()
    return HttpResponse(html)

def Graficar(request):
    objHTML = loader.get_template("graficar.html")
    html = objHTML.render()
    return HttpResponse(html)

def Ayuda(request):
    global seInformacion
    objHTML = loader.get_template("ayuda.html")
    html = objHTML.render({"valor": seInformacion})
    seInformacion = False
    return HttpResponse(html)

def info(request):
    global seInformacion
    seInformacion = True
    return redirect("http://127.0.0.1:8000/Ayuda")

def docu(request):
    api_url = 'http://127.0.0.1:3050/documentacion'
    requests.get(api_url)
    return redirect("http://127.0.0.1:8000/Ayuda")