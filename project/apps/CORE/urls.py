from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib.auth.views import LogoutView
from . import views
from .views import home, crear_cliente, busqueda, about, pages
from django.views.generic import TemplateView

app_name = "Home"

urlpatterns = [
    path("", home, name="home"),
    path('login/', views.login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="CORE/logout.html"), name="logout"),
    path("clientes/", views.clientes, name="clientes"),
    path('crear/', crear_cliente, name="crear"),
    path('busqueda/', busqueda, name="busqueda"),
    path('about/', TemplateView.as_view(template_name="CORE/about.html"), name="about"),
    path('pages/', TemplateView.as_view(template_name="CORE/pages.html"), name="pages"),
    path('promo1/', TemplateView.as_view(template_name="CORE/promo1.html"), name="promo1"),
    path('promo2/', TemplateView.as_view(template_name="CORE/promo2.html"), name="promo2"),
    path('promo3/', TemplateView.as_view(template_name="CORE/promo3.html"), name="promo3"),
    #path('register/', views.register, name="register"),
]

urlpatterns += staticfiles_urlpatterns()
### Esto sirve para poder usar los archivos de static
### desde los HTML o templates