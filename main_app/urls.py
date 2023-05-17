from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #view path to home
    path('about/', views.about, name='about'), #views path to about
    path('games/', views.games_index, name='index'), #index path to list
    path('games/<int:game_id>/', views.games_detail, name ='detail'), #detail path to list
    path('games/create/', views.GameCreate.as_view(), name='games_create'), #create path to list
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'), #upate path
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'), #delete path
]
