from django.shortcuts import render, redirect
from .models import Commande  # On importe le bon nom

def vue_commandes(request):
    # 1. Vérification de la connexion
    if 'utilisateur_id' not in request.session:
        return redirect('/compte/connexion/')
    
    user_id = request.session.get('utilisateur_id')
    role = request.session.get('role')

    # 2. Logique selon le rôle
    # On utilise 'Commande' partout, car c'est le nom du modèle importé
    if role == 'vendeur':
        # Assure-toi que ton modèle Commande a bien un champ 'product'
        commandes = Commande.objects.filter(product__vendeur_id=user_id).order_by('-date_creation')
    else:
        # Assure-toi que ton modèle Commande a bien un champ 'client_id'
        commandes = Commande.objects.filter(client_id=user_id).order_by('-date_creation')

    # 3. Rendu de la page
    return render(request, 'commandes/mes_commandes.html', {
        'commandes': commandes
    })