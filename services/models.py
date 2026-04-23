from django.db import models

from django.db import models
from clients.models import Client

class ServiceOrder(models.Model):
    SERVICE_TYPES = [
        ("instalacion", "Instalación"),
        ("mantenimiento", "Mantenimiento"),
        ("reparacion", "Reparación"),
    ]

    STATUS = [
        ("pendiente", "Pendiente"),
        ("en_progreso", "En progreso"),
        ("finalizado", "Finalizado"),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="services")
    date = models.DateTimeField(auto_now_add=True)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    status = models.CharField(max_length=20, choices=STATUS, default="pendiente")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='services/', blank=True, null=True)

    def __str__(self):
        return f"{self.client.name} - {self.service_type}"