from django.urls import path
from . import views

urlpatterns = [
    path('inscription/', views.vue_inscription, name='inscription'),
]