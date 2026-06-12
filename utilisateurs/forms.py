from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur

class InscriptionForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Utilisateur
        # On liste les champs sans espaces, et sans le mot de passe (géré tout seul)
        fields = UserCreationForm.Meta.fields + ('nom', 'prenom', 'email', 'role', 'telephone')