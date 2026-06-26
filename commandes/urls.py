from django.urls import path
from . import views

urlpatterns = [
    # C'est ici que tu définis le nom 'voir_commandes' (ou le nom que tu préfères)
    path('', views.vue_commandes, name='voir_commandes'),
]