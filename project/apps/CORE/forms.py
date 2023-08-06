from django import forms
from .models import Cliente

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

# Tener una app de registro donde se puedan registrar usuario. Un usuario está compuesto por:
# email - contraseña - nombre de usuario.


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["pais_origen_id", "apellido", "nombre", "nacimiento", "medio_id", "nrotarjeta"]


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"] # quiero agregar email
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # Quita los mensajes de ayuda
        # help_texts = {k: "" for k in fields}
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }
 


