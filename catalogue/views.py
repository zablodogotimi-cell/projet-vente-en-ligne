import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Prefetch
from .models import Product, Category

# 1. Vue pour exporter les articles en CSV
def exporter_articles_csv(request):
    if 'utilisateur_id' not in request.session:
        return redirect('/compte/connexion/')
        
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="export_articles_categories.csv"'
    response.write(u'\ufeff'.encode('utf-8')) # Évite les bugs d'accents sur Excel
    
    writer = csv.writer(response, delimiter=';')
    writer.writerow(['Catégorie', 'Nom de l\'article', 'Prix', 'Stock'])
    
    vendeur_id = request.session.get('utilisateur_id')
    articles = Product.objects.filter(vendeur_id=vendeur_id).select_related('category').order_by('category__name', 'name')
    
    for article in articles:
        cat_name = article.category.name if article.category else "Sans catégorie"
        writer.writerow([cat_name, article.name, article.price, article.stock])
        
    return response

# 2. Vue pour ajouter/importer un produit manuellement
def ajouter_produit(request):
    if 'utilisateur_id' not in request.session:
        return redirect('/compte/connexion/')
        
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        category_id = request.POST.get('category')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        
        vendeur_id = request.session.get('utilisateur_id')
        
        Product.objects.create(
            vendeur_id=vendeur_id,
            category_id=category_id if category_id else None,
            name=name,
            price=price,
            stock=stock,
            description=description,
            image=image
        )
        return redirect('dashboard_vendeur')
    return redirect('dashboard_catalogue')
        
def v_dashboard_catalogue(request):
    if 'utilisateur_id' not in request.session:
        return redirect('/compte/connexion/')
        
    role_utilisateur = request.session.get('role', '')
    provenance = request.META.get('HTTP_REFERER', '')
    
    if role_utilisateur:
        role_clean = role_utilisateur.strip().lower()
    else:
        role_clean = ''
        
    if role_clean == 'vendeur' or 'vendeur' in provenance or 'vendeur' in request.path:
        request.session['role'] = 'vendeur'
        vendeur_id = request.session.get('utilisateur_id')
        
        # 1. Pour l'affichage des produits : On garde le filtre propre
        prods_vendeur = Product.objects.filter(vendeur_id=vendeur_id)
        categories_affichees = Category.objects.filter(products__in=prods_vendeur).prefetch_related(
            Prefetch('products', queryset=prods_vendeur, to_attr='produits')
        ).distinct()
        
        # 2. NOUVEAU : Pour le formulaire d'ajout : On prend absolument TOUTES les catégories
        toutes_les_categories = Category.objects.all()
        
        return render(request, 'catalogue/dasboard_vendeur_catalogue.html', {
            'categories': categories_affichees,       # Pour boucler sur les produits
            'toutes_les_categories': toutes_les_categories  # Pour ton formulaire d'ajout
        })
        
    else:
        # (Le reste du code pour l'acheteur ne change pas...)
        prods_acheteur = Product.objects.filter(stock__gt=0)
        categories = Category.objects.filter(products__in=prods_acheteur).prefetch_related(
            Prefetch('products', queryset=prods_acheteur, to_attr='produits')
        ).distinct()
        
        return render(request, 'catalogue/dasboard_acheteur_catalogue.html', {
            'categories': categories
        })
    
def ajouter_categorie(request):
    if 'utilisateur_id' not in request.session:
        return redirect('/compte/connexion/')
        
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            from django.utils.text import slugify
            Category.objects.create(
                name=name,
                slug=slugify(name)
            )
            
    return redirect('dashboard_catalogue')