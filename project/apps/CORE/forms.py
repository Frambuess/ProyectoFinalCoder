from django import forms
from .models import Cliente

 
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["pais_origen_id", "apellido", "nombre", "nacimiento", "medio_id", "nrotarjeta"]


