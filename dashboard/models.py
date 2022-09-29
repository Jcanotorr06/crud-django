from django.db import models

class Categorias(models.Model):
    categoria = models.CharField(max_length=40, null=False, blank=False, default=None)
    
    def __str__(self):
        return self.categoria

class Productos(models.Model):
    producto = models.CharField(max_length=40, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    qty = models.PositiveIntegerField(default=0, null=False, blank=False)
    precio = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=9)
    ventas = models.IntegerField(default=0, null=False, blank=False)
    creacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(
        "Categorias", 
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.producto