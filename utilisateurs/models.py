from django.db import models
from django.contrib.auth.models import AbstractUser

# Si tu as personnalisé l'utilisateur, ton modèle doit ressembler à ça :
class Utilisateur(AbstractUser):
    nom = models.CharField(max_length=50, blank=True)
    prenom = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length=20, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    
    # Django gère déjà username, email et password via AbstractUser