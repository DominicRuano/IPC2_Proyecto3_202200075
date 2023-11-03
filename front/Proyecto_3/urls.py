"""
URL configuration for Proyecto_3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto_3.view import *

urlpatterns = [
    path("", inicio),
    path('admin/', admin.site.urls),
    path("getInfo/", getInfo),
    path("reset/", resetearDatos),
    path("buttonReset/", buttonReset, name="boton_reset"),
    path("cargarMensajes/", cargarMensajes),
    path("buttonMensajes/", buttonMensaje, name='boton_mensaje'),
    path("cargarConfiguraciones/", cargarConfiguraciones),
    path("buttonconfig/", buttonconfig, name='boton_config'),
    path("consultarHastag/", consultarHastags),
    path("consultarMenciones/", consultarMenciones),
    path("consultarSentimientos/", consultarSentimiento),
    path("Graficar/", Graficar),
    path("Ayuda/", Ayuda),
    path("buttonAyuda/", info, name="boton_ayuda"),
    path("documentacion/", docu, name="documentacion"),
    path("fechas/", fecha, name="boton_fechas"),
    path("menciones/", mencion, name="boton_menciones"),
    path("sentimientos/", sentimiento, name="boton_sentimiento"),
]
