from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('export-articles/', views.exporter_articles_csv, name='exporter_articles'),
    path('ajouter-produit/', views.ajouter_produit, name='ajouter_produit'),
    path('mon-catalogue/', views.v_dashboard_catalogue, name='dashboard_catalogue'),
    path('categorie/ajouter/', views.ajouter_categorie, name='ajouter_categorie'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)