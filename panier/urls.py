from django.urls import path
from . import views

urlpatterns = [
    path('', views.vue_panier, name='voir_panier'),
    path('ajouter/<int:product_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('supprimer/<int:product_id>/', views.supprimer_du_panier, name='supprimer_du_panier'),
    path('valider/', views.valider_panier, name='valider_panier'),
]