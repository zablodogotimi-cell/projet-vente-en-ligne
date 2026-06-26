from django.shortcuts import render, redirect
from catalogue.models import Product

def ajouter_au_panier(request, product_id):
    product = Product.objects.get(id=product_id)
    panier = request.session.get('panier', {})
    
    # Si le produit est déjà dans le panier, on augmente la quantité
    if str(product_id) in panier:
        panier[str(product_id)]['quantite'] += 1
    else:
        panier[str(product_id)] = {
            'nom': product.nom,
            'prix': float(product.prix),
            'quantite': 1
        }
    
    request.session['panier'] = panier
    return redirect('voir_panier')

def vue_panier(request):
    panier = request.session.get('panier', {})
    total = sum(item['prix'] * item['quantite'] for item in panier.values())
    return render(request, 'panier/panier.html', {'panier': panier, 'total': total})

def supprimer_du_panier(request, product_id):
    panier = request.session.get('panier', {})
    if str(product_id) in panier:
        del panier[str(product_id)]
        request.session['panier'] = panier
    return redirect('voir_panier')

def valider_panier(request):
    from commandes.models import Commande
    panier = request.session.get('panier', {})
    
    for product_id, item in panier.items():
        product = Product.objects.get(id=product_id)
        # Création de la commande réelle en base
        Commande.objects.create(
            client_id=request.session['utilisateur_id'],
            product=product,
            quantite=item['quantite'],
            prix_total=item['prix'] * item['quantite']
        )
    
    # Vider le panier après validation
    request.session['panier'] = {}
    return redirect('voir_commandes')