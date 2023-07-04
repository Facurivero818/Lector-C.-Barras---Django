from django.shortcuts import render
from codigos.models import Codigos

def index(request):

    return render(request,"index.html")

def consulta(request):
    if request.method == "GET":
        context = {"dato":""}
    elif request.method == "POST":
        dato = (request.POST["valor"])
        resultado = Codigos.objects.get(id= dato)
        context = {"dato":resultado.codigo}
    else:
        context = {"dato":"ERROR AL ENVIAR LA SOLICITUD"}

    return render(request,"consulta.html",context)

def agregar(request):
    if request.method == "GET":
        context = {"dato":""}
    elif request.method == "POST":
        id = request.POST.get("id") 
        tipo = request.POST.get("tipo") 
        nuevo_codigo = Codigos(id,tipo)
        nuevo_codigo.save()
        context = {"dato":"Agregado correctamente"}
    else:
        context = {"dato":"ERROR AL ENVIAR LA SOLICITUD"}

    return render(request,"agregar.html",context)

def eliminar(request):
    if request.method == "GET":
        context = {"dato":""}
    elif request.method == "POST":
        #LEER BASE DE DATOS
        context = {"dato":"Elimiando correctamente"}
    else:
        context = {"dato":"ERROR AL ENVIAR LA SOLICITUD"}

    return render(request,"eliminar.html",context)
