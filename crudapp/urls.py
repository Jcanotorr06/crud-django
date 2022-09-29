from django import views
from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Inicio
    path('', views.inicio, name="inicio"),
    #Añadir Producto
    path('add_producto', views.add_producto, name="add_producto"),
    #Editar Producto
    path('editar_producto', views.editar_producto, name="editar_producto"),
    #Eliminar Producto
    path('eliminar_producto', views.eliminar_producto, name="eliminar_producto"),
    #Detalles de Producto
    path('producto/<int:id_producto>', views.producto, name="producto"),
    #Ver Categorias
    path('categorias', views.categorias, name="categorias"),
    #Añadir Categoria
    path('add_categorias', views.add_categorias, name="add_categorias"),
    #Editar Categorias
    path('editar_categorias', views.editar_categorias, name="editar_categorias"),
    #Eliminar Categorias
    path('eliminar_categorias', views.eliminar_categorias, name="eliminar_categorias"),
]
