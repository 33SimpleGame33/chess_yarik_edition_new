from django.test import TestCase
from .models import Player, Competition, Game

class caseTest(TestCase):
    def test_player_create(self):
        
        names = ['Joe', '$123da', '^7afda']

        new_players = []
        for name in names:
            Player.objects.create_player(name = name)

        self.assertEqual(Player.objects.all().count(),len(names))
    
    def test_add_player(self):
        names = ['Joe', 'Bob', 'Steve', 'Abdul']
        competition = Competition.objects.create_competition()
        for name in names:
            Player.objects.create_player(name = name)
        for player in Player.objects.all()[:len(names)]:
            competition.add_player(player)
        self.assertEqual(competition.players.all().count(),len(names))

    def test_competition_generate_competition(self):
        names = ['Joe', 'Bob', 'Steve', 'Abdul']
        competition = Competition.objects.create()
        for name in names:
            Player.objects.create_player(name = name)
        for player in Player.objects.all()[:len(names)]:
            competition.add_player(player)
        competition.generate_competition()
        self.assertIsNotNone(competition.games)