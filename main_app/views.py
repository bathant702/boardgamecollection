from django.shortcuts import render

#dummy data
games = [
    {'name': 'Magic: The Gathering', 'genre': ' collectible card game', 'players': '2 to many', 'playtime': '20-60 min', 'description': 'family friendly fantasy card game '},
    {'name': 'Monopoly', 'genre': 'board game', 'players': '2 to 4', 'playtime': '180 minutes', 'description': 'family friendly board game about economics'},
    {'name': 'Catan', 'genre': 'board game', 'players': '2 to 6', 'playtime': '120 minutes', 'description': 'family friendly board game about bricks and sheep'},
]

# Create your views here.



# function based operations
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    return render(request, 'games/index.html', {
        'games': games
    })