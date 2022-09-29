from django.shortcuts import render
from dashboard.models import Productos, Categorias
from django.http import HttpRequest, HttpResponseRedirect

from dashboard.utils import ValidacionProducto

#Inicio
def inicio(request:HttpRequest):
    todos_productos = Productos.objects.all().order_by("-creacion")
    return render(request, 'inicio.html', {'productos': todos_productos})

#Añadir Producto
def add_producto(request:HttpRequest):
    if request.method == "POST":
        form = ValidacionProducto(request.POST)
        if not form.is_valid():
            return HttpResponseRedirect('/?status=error')
        else:
            producto = Productos(**form.cleaned_data)
            producto.save()
            return HttpResponseRedirect('/')
    else:
        return render(request, 'add_producto.html')
            

#Editar Producto
def editar_producto(request:HttpRequest):
    if request.method == "POST":
        form = ValidacionProducto(request.POST)
        if not form.is_valid():
            return HttpResponseRedirect('/?status=error')
        else:
            producto = Productos(**form.cleaned_data)
            producto.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
            

#Eliminar Producto
def eliminar_producto(request:HttpRequest):
    if request.method == 'POST':
        id = request.POST.get("id")
        if id != None:
            producto = Productos.objects.get(id = id)
            if producto != None:
                producto.delete()
                
    HttpResponseRedirect('/')

#Detalles de Producto
def producto(request:HttpRequest, id_producto:int):
    producto = Productos.objects.get(id = id_producto)
    if producto != None:
        return render(request, "producto.html", {'producto': producto})
    else:
        return HttpResponseRedirect('/')

#Ver Categorias
def categorias(request:HttpRequest):
    todas_categorias = Categorias.objects.all()
    return render(request, 'categorias.html', {'categorias': todas_categorias})

#Editar Categorias
def editar_categorias(request:HttpRequest):
    todas_categorias = Categorias.objects.all()
    return render(request, 'categorias.html', {'categorias': todas_categorias})

#Eliminar Categorias
def eliminar_categorias(request:HttpRequest):
    todas_categorias = Categorias.objects.all()
    return render(request, 'categorias.html', {'categorias': todas_categorias})
