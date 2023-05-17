from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game

#dummy data
# games = [
#     {'name': 'Magic: The Gathering', 'genre': ' collectible card game', 'players': '2 to many', 'playtime': '20-60 min', 'description': 'family friendly fantasy card game '},
#     {'name': 'Monopoly', 'genre': 'board game', 'players': '2 to 4', 'playtime': '180 minutes', 'description': 'family friendly board game about economics'},
#     {'name': 'Catan', 'genre': 'board game', 'players': '2 to 6', 'playtime': '120 minutes', 'description': 'family friendly board game about bricks and sheep'},
# ]

# Create your views here.
# class based operations
class GameCreate(CreateView):
    model = Game
    fields = [ 'name', 'genre', 'players', 'playtime', 'description' ]
    success_url = '/games/{game_id}'

class GameUpdate(UpdateView):
    model = Game
    fields = [ 'genre', 'players', 'playtime', 'description' ]

class GameDelete(DeleteView):
    model = Game
    success_url = '/games'


# function based operations
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games = Game.objects.all() #retrieving Game model
    return render(request, 'games/index.html', {
        'games': games
    })

def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'games/detail.html', {
        'game': game
    })
