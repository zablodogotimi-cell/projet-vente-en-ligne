from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import InscriptionForm  # Importation corrigée depuis .forms
from .forms import InscriptionForm
from django.contrib.auth.forms import AuthenticationForm
# 1. Page d'accueil générale

def vue_accueil(request):
    return render(request, 'base_accueil.html')

# 2. Page d'inscription
def vue_inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connecte automatiquement l'utilisateur après inscription
            return redirect('accueil')  # Redirige vers l'accueil
    else:
        form = InscriptionForm()
    return render(request, 'utilisateurs/inscription.html', {'form': form})
def vue_connexion(request):
    if request.method == 'POST':
        # CORRECTION ICI : On passe la requête via l'argument nommé 'request'
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accueil')
    else:
        form = AuthenticationForm()
    return render(request, 'utilisateurs/connexion.html', {'form': form})