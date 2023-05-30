from django.shortcuts import render
from .models import Game, Player, Competition
from django.http import JsonResponse
from .forms import PlayerForm, CompetitionForm
import math

def index(request):
    players = Player.objects.all()
    competitions = Competition.objects.all()
    return render(request, 'main/index.html', {'competitions' : competitions, 'players' : players})

def player(request):
    if request.POST:
        player = Player.objects.create_player(request.POST.get('name'))
    form = PlayerForm()
    return render(request, 'main/register.html', {'form': form})

def competition(request):
    if request.method == 'POST':
        players_list = [Player.objects.get(pk=i) for i in request.POST.getlist('players')]
        print(f'---> {players_list}')
        if len(players_list) > 1 and not(math.log2(len(players_list)) % 1):
            competition = Competition.objects.create_competition(players=players_list)
            competition.generate_competition()
            print(f'---> {competition}')
    form = CompetitionForm()
    return render(request, 'main/competition.html', {'form': form})

def set_winner_ajax(request):
    game = Game.objects.get(pk=request.GET['game'])
    game.set_winner(Player.objects.get(pk=request.GET['winner']))
    next_game = game.get_next_game()
    return JsonResponse({'next_game':next_game.id})