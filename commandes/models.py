from django.db import models

from catalogue.models import Product  # On importe le produit pour l'associer
from django.contrib.auth.models import User # Si tu utilises les utilisateurs Django

class Commande(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    client_id = models.IntegerField() # Ou ForeignKey(User) si tu gères les comptes différemment
    quantite = models.IntegerField(default=1)
    date_creation = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=50, default='En attente')

    def __str__(self):
        return f"Commande de {self.product.name} par {self.client_id}"