from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    
    # Routes pour les tableaux de bord (nécessaires pour le bon fonctionnement des redirections)
    path('dashboard/vendeur/', views.dashboard_vendeur, name='dashboard_vendeur'),
    path('dashboard/acheteur/', views.dashboard_acheteur, name='dashboard_acheteur'),
]