from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='clients/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Review(models.Model):

    RATING = [
        (1, "⭐ Muy malo"),
        (2, "⭐⭐ Malo"),
        (3, "⭐⭐⭐ Bueno"),
        (4, "⭐⭐⭐⭐ Muy bueno"),
        (5, "⭐⭐⭐⭐⭐ Excelente"),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        choices=RATING,
        verbose_name="Calificación"
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)