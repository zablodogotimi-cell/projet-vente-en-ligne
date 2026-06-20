from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import get_user_model
from django.db.models import Q  # Permet de chercher par email OU par username
from .models import Utilisateur

# Récupération propre du modèle utilisateur (personnalisé ou natif)
Utilisateur_Model = get_user_model()

def accueil(request):
    """Redirige vers le tableau de bord si l'utilisateur est connecté, sinon affiche l'accueil général."""
    if 'utilisateur_id' in request.session:
        role = request.session.get('utilisateur_role')
        if role == 'Vendeur':
            return redirect('dashboard_vendeur')
        else:
            return redirect('dashboard_acheteur')
            
    return render(request, 'base_accueil.html')

def dashboard_vendeur(request):
    """Affiche l'espace dédié au vendeur."""
    if 'utilisateur_id' not in request.session or request.session.get('utilisateur_role') != 'Vendeur':
        messages.error(request, "Accès refusé. Vous devez être connecté en tant que Vendeur.")
        return redirect('connexion')
    return render(request, 'utilisateurs/dasboard_vendeur.html')

def dashboard_acheteur(request):
    """Affiche l'espace dédié à l'acheteur."""
    if 'utilisateur_id' not in request.session:
        messages.error(request, "Veuillez vous connecter pour accéder à votre espace.")
        return redirect('connexion')
    return render(request, 'utilisateurs/dasboard_acheteur.html')

def inscription(request):
    """Gère l'inscription d'un nouvel utilisateur."""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        role = request.POST.get('role')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Vérification de la correspondance des mots de passe
        if password != password_confirm:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, 'utilisateurs/inscription.html')

        try:
            # Création sécurisée avec le gestionnaire de Django (hachage automatique)
            utilisateur = Utilisateur_Model.objects.create_user(
                username=username,
                email=email,
                role=role,
                password=password 
            )
            
            messages.success(request, "Votre compte a été créé avec succès ! Connectez-vous.")
            return redirect('connexion')

        except Exception as e:
            messages.error(request, f"Erreur lors de l'enregistrement : {e}")
            return render(request, 'utilisateurs/inscription.html')

    return render(request, 'utilisateurs/inscription.html')

def connexion(request):
    """Gère la connexion de l'utilisateur."""
    if request.method == 'POST':
        email_ou_username = request.POST.get('username')
        mot_de_passe = request.POST.get('password')

        try:
            # Cherche l'utilisateur soit par son email, soit par son nom d'utilisateur
            utilisateur = Utilisateur_Model.objects.get(
                Q(email=email_ou_username) | Q(username=email_ou_username)
            )
            
            # Vérification du mot de passe haché via le champ interne .password
            if check_password(mot_de_passe, utilisateur.password):
                request.session['utilisateur_id'] = utilisateur.id
                request.session['utilisateur_role'] = utilisateur.role
                
                messages.success(request, f"Ravi de vous revoir, {utilisateur.username} !")
                
                if utilisateur.role == 'Vendeur':
                    return redirect('dashboard_vendeur')
                else:
                    return redirect('dashboard_acheteur')
            else:
                messages.error(request, "Identifiants ou mot de passe incorrects.")
            
        except Utilisateur_Model.DoesNotExist:
            messages.error(request, "Identifiants ou mot de passe incorrects.")

    return render(request, 'utilisateurs/connexion.html')

def deconnexion(request):
    """Gère la déconnexion et nettoie la session."""
    if 'utilisateur_id' in request.session:
        del request.session['utilisateur_id']
    if 'utilisateur_role' in request.session:
        del request.session['utilisateur_role']
    messages.success(request, "Vous avez été déconnecté.")
    return redirect('accueil')