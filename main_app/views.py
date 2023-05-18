from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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

class GameCreate(LoginRequiredMixin, CreateView):
    model = Game
    fields = [ 'name', 'genre', 'players', 'playtime', 'description' ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GameUpdate(LoginRequiredMixin, UpdateView):
    model = Game
    fields = [ 'genre', 'players', 'playtime', 'description' ]

class GameDelete(LoginRequiredMixin, DeleteView):
    model = Game
    success_url = '/games'

# location routes
class LocationList(LoginRequiredMixin, ListView):
    model = Location

class LocationDetail(LoginRequiredMixin, DetailView):
    model = Location

class LocationCreate(LoginRequiredMixin, CreateView):
    model = Location
    fields = [ 'name', 'address']
    success_url = '/locations'

class LocationUpdate(LoginRequiredMixin, UpdateView):
    model = Location
    fields = [ 'address']

class LocationDelete(LoginRequiredMixin, DeleteView):
    model = Location
    success_url = '/locations'


# function based operations
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def games_index(request):
    games = Game.objects.filter(user=request.user) #retrieves only user entries
    return render(request, 'games/index.html', {
        'games': games
    })

@login_required
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
@login_required
def add_record(request, game_id):
    form = RecordForm(request.POST)
    if form.is_valid():
        new_record = form.save(commit=False)
        new_record.game_id = game_id
        new_record.save()
    return redirect('detail', game_id = game_id)

# areas for adding photos functions
# areas for adding photos functions
# areas for adding photos functions
# areas for adding photos functions

#for associated locations
@login_required
def assoc_location(request, game_id, location_id):
  # Note that you can pass a location's id instead of the whole location object
  Game.objects.get(id=game_id).location.add(location_id)
  return redirect('detail', game_id=game_id)

#for associated locations
@login_required
def unassoc_location(request, game_id, location_id):
  # Note that you can pass a location's id instead of the whole location object
  Game.objects.get(id=game_id).location.remove(location_id)
  return redirect('detail', game_id=game_id)

#sign up new users
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)