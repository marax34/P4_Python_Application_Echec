import json
import sys
sys.path.append('./')
from controllers.json_function import loadJson
from models.tournament import Tournament
from models.player import Player
from models.game import Game
from views.tournament_views import select_players

select_players()

game = Game(tournament.players[0], tournament.players[1])
game.play()
