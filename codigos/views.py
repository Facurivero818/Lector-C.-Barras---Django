from django.shortcuts import render
from codigos.models import Codigos

def index(request):

    return render(request,"index.html")

def consulta(request):
    if request.method == "GET":
        context = {"dato":""}
    elif request.method == "POST":
        valor = (request.POST["valor"])
        try: 
            resultado = Codigos.objects.get(id= valor)

            if resultado.codigo == "RECICLABLE":
                clase_css = "bg-success"
            elif resultado.codigo == "NO RECICLABLE":
                clase_css = "bg-danger"
            else:
                clase_css = ""

            context = {"respuesta":resultado.codigo, "clase_css": clase_css}

        except Codigos.DoesNotExist:
            context = {"respuesta":"CODIGO NO ENCONTRADO"}
    

    else:
        context = {"respuesta":"ERROR AL ENVIAR LA SOLICITUD"}

    return render(request,"consulta.html",context)

def agregar(request):
    if request.method == "GET":
        context = {"respuesta":""}
    elif request.method == "POST":
        valor = request.POST.get("id") 
        try: 
            resultado = Codigos.objects.get(id= valor)
            resultado = False
        
        except Codigos.DoesNotExist:
            resultado = True
        
        if resultado:
            tipo = request.POST.get("tipo") 
            nuevo_codigo = Codigos(valor,tipo)
            nuevo_codigo.save()
            context = {"respuesta":"AGREGADO CORRECTAMENTE"}
        else:
            context = {"respuesta":"CODIGO YA EXISTENTE"}
    else:
        context = {"respuesta":"ERROR AL ENVIAR LA SOLICITUD"}

    return render(request,"agregar.html",context)

def eliminar(request):
    if request.method == "GET":
        context = {"respuesta":""}
    elif request.method == "POST":
        dato = request.POST.get("id") 
        try: 
            eliminar_codigo = Codigos.objects.get(id= dato)
            eliminar_codigo.delete()
            context = {"respuesta":"ELIMINADO CORRECTAMENTE"}

        except Codigos.DoesNotExist:
            context = {"respuesta":"NO EXITE EL CODIGO"}
    else:
        context = {"respuesta":"ERROR AL ENVIAR LA SOLICITUD"}

    return render(request,"eliminar.html",context)
