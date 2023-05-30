from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('player', views.player, name='player_reg'),
    path('competition', views.competition, name='competition_reg'),
    path('set_winner_ajax', views.set_winner_ajax, name='set_winner_ajax'),
]