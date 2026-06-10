from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import InscriptionForm

# 1. Page d'accueil générale
def vue_accueil(request):
    return render(request, 'base_accueil.html')

# 2. Page d'inscription
def vue_inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_validate():  #
            user = form.save()
            login(request, user)  
            return redirect('accueil')
    else:
        form = InscriptionForm()
    return render(request, 'utilisateurs/inscription.html', {'form': form})

