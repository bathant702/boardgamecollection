from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #view path to home
    path('about/', views.about, name='about'), #views path to about
    path('games/', views.games_index, name='index'), #index path to list
]