# Create your views here.

from typing import Any

from django.contrib.auth.decorators import login_required

#! importaciones para login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models

# PAGINA PRINCIPAL

@login_required
def index(request):
    return render(request, "producto/index.html")


class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria


class ProductoCategoriaCreate(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")


class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria



class ProductoCategoriaUpdate(UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")


class ProductoCategoriaDelete(DeleteView):
    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")


# ***** PRODUCTO

class ProductoList(ListView):
    model = models.Producto

    def get_queryset(self) -> QuerySet[Any]:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Producto.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Producto.objects.all()
        return object_list


class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")


class ProductoDetail(DetailView):
    model = models.Producto


class ProductoUpdate(UpdateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")


class ProductoDelete(DeleteView):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")