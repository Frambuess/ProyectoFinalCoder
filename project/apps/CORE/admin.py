from django.contrib import admin

# Register your models here.
from . import models

# admin.site.site_header = "Tienda online"
# admin.site.site_title = "Home"

admin.site.register(models.Pais)
admin.site.register(models.Mediodepago)
admin.site.register(models.Cliente)
