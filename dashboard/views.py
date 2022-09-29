from django.shortcuts import get_object_or_404, render
from dashboard.models import Productos, Categorias
from django.http import HttpRequest, HttpResponseRedirect

from dashboard.utils import ValidacionProducto

#Inicio
def inicio(request:HttpRequest):
    todos_productos = Productos.objects.all().order_by("-creacion")
    categorias = Categorias.objects.all()
    return render(request, 'inicio.html', {'productos': todos_productos, 'categorias': categorias})

#Añadir Producto
def add_producto(request:HttpRequest):
    if request.method == "POST":
        form = ValidacionProducto(request.POST)
        if form.is_valid():
            producto = Productos(**form.cleaned_data)
            producto.save()
    
    return HttpResponseRedirect('/')
            

#Editar Producto
def editar_producto(request:HttpRequest):
    if request.method == "POST":
        id = request.POST.get("id")
        producto = get_object_or_404(Productos, id=id)
        form = ValidacionProducto(request.POST, instance=producto)
        if form.is_valid():
            producto.save()
    
    return HttpResponseRedirect('/')
            

#Eliminar Producto
def eliminar_producto(request:HttpRequest):
    if request.method == 'POST':
        id = request.POST.get("id")
        if id != None:
            producto = Productos.objects.get(id = id)
            if producto != None:
                producto.delete()
                
    return HttpResponseRedirect('/')

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

def add_categorias(request:HttpRequest):
    if request.method == 'POST':
        if request.POST.get("categoria"):
            categoria = Categorias()
            categoria.categoria = request.POST.get("categoria")
            categoria.save()
    
    return HttpResponseRedirect("/categorias")

#Editar Categorias
def editar_categorias(request:HttpRequest):
    if(request.method == 'POST'):
        categoria = Categorias.objects.get(id = request.POST.get("id"))
        if categoria != None:
            categoria.categoria = request.POST.get("categoria")
            categoria.save()
    return HttpResponseRedirect("/categorias")

#Eliminar Categorias
def eliminar_categorias(request:HttpRequest):
    if(request.method == 'POST'):
        categoria = Categorias.objects.get(id = request.POST.get("id"))
        if categoria != None:
            categoria.delete()
    return HttpResponseRedirect("/categorias")
