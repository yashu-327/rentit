from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_per_day = models.FloatField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    days = models.IntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -> {self.product.name}"