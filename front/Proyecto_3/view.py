from django.http import HttpResponse
from django.template import loader
from requests import post, get

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
    html = objTemplate.render({"existe": existen,"respuesta": Anwr.json(), 
                            "idNombre_reporte": reporteName, "descripcion": descripcion, "valores": conteo})
    return HttpResponse(html)