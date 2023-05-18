from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Game, Location
from .forms import RecordForm

#dummy data
# games = [
#     {'name': 'Magic: The Gathering', 'genre': ' collectible card game', 'players': '2 to many', 'playtime': '20-60 min', 'description': 'family friendly fantasy card game '},
#     {'name': 'Monopoly', 'genre': 'board game', 'players': '2 to 4', 'playtime': '180 minutes', 'description': 'family friendly board game about economics'},
#     {'name': 'Catan', 'genre': 'board game', 'players': '2 to 6', 'playtime': '120 minutes', 'description': 'family friendly board game about bricks and sheep'},
# ]

# Create your views here.
# class based operations
# game routes
class GameCreate(CreateView):
    model = Game
    fields = [ 'name', 'genre', 'players', 'playtime', 'description' ]

class GameUpdate(UpdateView):
    model = Game
    fields = [ 'genre', 'players', 'playtime', 'description' ]

class GameDelete(DeleteView):
    model = Game
    success_url = '/games'

# location routes
class LocationList(ListView):
    model = Location

class LocationDetail(DetailView):
    model = Location

class LocationCreate(CreateView):
    model = Location
    fields = [ 'name', 'address']
    success_url = '/locations'

class LocationUpdate(UpdateView):
    model = Location
    fields = [ 'address']

class LocationDelete(DeleteView):
    model = Location
    success_url = '/locations'


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

#add game to collection
def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    id_list = game.location.all().values_list('id')
    locations_game_doesnt_have = Location.objects.exclude(id__in=id_list)
    record_form = RecordForm()
    return render(request, 'games/detail.html', {
        'game': game,
        'record_form': record_form,
        'locations': locations_game_doesnt_have
    })

#add record
def add_record(request, game_id):
    form = RecordForm(request.POST)
    if form.is_valid():
        new_record = form.save(commit=False)
        new_record.game_id = game_id
        new_record.save()
    return redirect('detail', game_id = game_id)

#for associated locations
def assoc_location(request, game_id, location_id):
  # Note that you can pass a location's id instead of the whole location object
  Game.objects.get(id=game_id).location.add(location_id)
  return redirect('detail', game_id=game_id)

#for associated locations
def unassoc_location(request, game_id, location_id):
  # Note that you can pass a location's id instead of the whole location object
  Game.objects.get(id=game_id).location.remove(location_id)
  return redirect('detail', game_id=game_id)