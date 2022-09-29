from django import forms

from dashboard.models import Categorias

class ValidacionProducto(forms.ModelForm):
    class Meta:
        model = Categorias
        fields= '__all__'
    """ id = forms.IntegerField()
    producto = forms.CharField(max_length=40, strip=True, min_length=1)
    descripcion = forms.CharField(max_length=200, min_length=1)
    qty = forms.IntegerField(min_value=0)
    precio = forms.DecimalField(min_value=0, decimal_places=2, max_digits=9)
    ventas = forms.IntegerField(min_value=0)
    categoria = forms.ModelChoiceField(queryset=Categorias.objects.all(), to_field_name="categoria", empty_label="Selecciona una Categoria") """