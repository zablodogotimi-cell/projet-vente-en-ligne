from django.db import models
from django.conf import settings  # Importe settings
from catalogue.models import Product

class PanierItem(models.Model):
    # Utilise settings.AUTH_USER_MODEL au lieu de User
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantite} x {self.product.nom}"