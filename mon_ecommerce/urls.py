from django.contrib import admin
from django.urls import path, include
from utilisateurs import views as utilisateurs_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', utilisateurs_views.accueil, name='accueil'),
    path('compte/', include('utilisateurs.urls')),
]