from django.contrib import admin
from .models import Lead

# Register your models here.
class LeadAdmin(admin.ModelAdmin):
    exclude = ('location', 'created_at')
    list_display = ('fullname', 'email', 'phone', 'value_property', 'mortgage', 'state', 'location', 'created_at')


admin.site.register(Lead, LeadAdmin)
