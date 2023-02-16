from django.db import models

# Create your models here.
class BitcoinPrice(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)