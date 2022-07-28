from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin

# Register your models here.

class ProspectoAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['razon_social', 'contacto', 'num_tel', 'correo', 'nombre_comercial', 'giro', 'localidad', \
    'fechaReg', 'clasificacion', 'responsable', 'fase', 'observaciones']

#admin.site.register(Clasificacion)
#admin.site.register(Fase)
admin.site.register(Responsable)
admin.site.register(Prospecto, ProspectoAdmin)