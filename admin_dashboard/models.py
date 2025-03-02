from django.db import models
from django.utils import timezone
import requests

def get_location():
    """
    Obtiene la ubicación del usuario basada en la IP pública.
    Retorna una cadena con el formato "País, Estado".
    """
    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        country = data.get("country", "Desconocido")
        region = data.get("regionName", "Desconocido")
        return f"{country}, {region}"
    except Exception:
        return "Ubicación no disponible"

# Create your models here.

class Lead(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    value_property = models.CharField(max_length=100)
    mortgage = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    
    location = models.CharField(max_length=100, default=get_location)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.fullname
