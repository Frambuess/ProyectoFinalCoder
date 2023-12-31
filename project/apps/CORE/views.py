from datetime import date

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
#from django.urls import is_valid_path
from .forms import ClienteForm
from django.contrib.auth.models import User

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render

from . import forms


# Create your views here.
from .models import Cliente, Mediodepago, Pais

def home(request):
    return render(request, "CORE/index.html")

def clientes(request):
    clientes_registros = Cliente.objects.all()
    contexto = {"clientes": clientes_registros}
    return render(request, "CORE/clientes.html", contexto)


def crear_cliente(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Home:clientes")
    else:  # request.method == "GET"
        form = ClienteForm()
    return render(request, "CORE/crear.html", {"form": form})


def busqueda(request: HttpRequest) -> HttpResponse:
    # Búsqueda por nombre que contenga "M"
    cliente_nombre = Cliente.objects.filter(nombre__contains="M")

    # Nacimientos  mayores a 2005
    cliente_nacimiento = Cliente.objects.filter( nacimiento__lt=date(2005, 1, 1))

    #age = date.today().year - nacimiento.year - ((date.today().month, date.today().day) < (nacimiento.month, nacimiento.day))

    #cliente_nacimiento = Cliente.objects.filter((date.today().year - nacimiento.year - ((date.today().month, date.today().day) < (nacimiento.month, nacimiento.day)))__gte=18)

    # País de origen vacío
    cliente_pais = Cliente.objects.filter(pais_origen_id=1)

    contexto = {
        "clientes_nombre": cliente_nombre,
        "clientes_nacimiento": cliente_nacimiento,
        "clientes_pais": cliente_pais
    }
    return render(request, "CORE/busqueda.html", contexto)


def about(request):
    return render(request, "CORE/about.html")

def pages(request):
    return render(request, "CORE/pages.html")

#! LOGIN


def login_request(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, "CORE/index.html", {"mensaje": "Inició sesión correctamente"})
    else:
        form = forms.CustomAuthenticationForm()
    return render(request, "CORE/login.html", {"form": form})


#! REGISTRO


@staff_member_required
def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "CORE/index.html", {"mensaje": "Vendedor creado 😊"})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "CORE/register.html", {"form": form})