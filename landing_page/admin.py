from django.contrib import admin
from landing_page.models import Lead


class AdminLead(admin.ModelAdmin):
    exclude = ('creado_en', 'ubicacion')
    list_display = ('nombre', 'email', 'telefono', 'valor_propiedad', 'monto', 'estado', 'creado_en', 'ubicacion')

# Register your models here.
admin.site.register(Lead, AdminLead)
