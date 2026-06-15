from django.urls import path
from .views import vue_accueil, vue_inscription, vue_connexion

urlpatterns = [
    path('', vue_accueil, name='accueil'),
   path('inscription/', vue_inscription, name='inscription'),
    path('connexion/', vue_connexion, name='connexion'),
    
]