from django.db import models
from django.utils import timezone
import requests

# Ubicacion por IP
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
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    valor_propiedad = models.DecimalField(max_digits=10, decimal_places=2)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=100)

    creado_en = models.DateTimeField(default=timezone.now)
    ubicacion = models.CharField(max_length=100, default=get_location)

    def __str__(self):
        return self.nombre
