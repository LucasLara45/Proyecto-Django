from django.db import models

from django.db import models
from clients.models import Client

class Service(models.Model):

    CATEGORY_CHOICES = [
        ('aire', 'Aire acondicionado'),
        ('heladera', 'Heladera'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/')

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
    service_type = models.ForeignKey('Service', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default="pendiente")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.client.name} - {self.service_type}"