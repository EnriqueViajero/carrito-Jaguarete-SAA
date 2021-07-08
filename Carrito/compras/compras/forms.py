from django import forms
from .models import productos

class FormProductoCustom(forms.ModelForm):
    #campos del modelo
    class Meta:
        model = productos
        fields = ('id_producto', 'nombre', 'precio','cantidd_existente','fecha_ingreso',)