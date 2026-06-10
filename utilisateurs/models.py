from django.db import models
from django import list_forms # Erreur fréquente, c'est bien : from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur

class InscriptionForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Utilisateur
        fields = UserCreationForm.Meta.fields + ('username','nom','prenom','email', 'role', 'telephone','mots de passe')