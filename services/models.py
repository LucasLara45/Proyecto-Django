from django.db import models
from clients.models import Client
from django.contrib.auth.models import User

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
    STATUS = [
        ("pendiente", "Pendiente"),
        ("en_progreso", "En progreso"),
        ("finalizado", "Finalizado"),
    ]

    PAYMENT_METHOD = [
        ("efectivo", "Efectivo"),
        ("transferencia", "Transferencia"),
        ("tarjeta", "Tarjeta"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, verbose_name="Nombre Completo")
    phone = models.CharField(max_length=30, verbose_name="Teléfono")
    address = models.CharField(max_length=255, verbose_name="Dirección")
    email = models.EmailField(verbose_name="Correo electrónico")
    payment_method = models.CharField(max_length=30, choices=PAYMENT_METHOD, verbose_name="Método de pago")
    notes = models.TextField(verbose_name="Nota")
    status = models.CharField(max_length=20, choices=STATUS, default="pendiente")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.service.title}"