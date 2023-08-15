import sys
sys.path.append('./')
from models.round import Round
from views.tournament_views import continue_or_quit
import time


def play_tournament(tournament):
    print(tournament.number_of_rounds)
    for round_num in range(tournament.current_round, (tournament.number_of_rounds) + 1):
        tournament.current_round = round_num 
        print(f"Début du round {tournament.current_round}: ")
        round = Round(tournament.players_ranking)
        round.generate_games()
        round.play_games()
        tournament.players_ranking.sort(key= lambda player: (player.score), reverse = True)
        tournament.rounds.append(round)
        if tournament.current_round != tournament.number_of_rounds + 1:
            tournament.next_round()
        tournament.save_to_json(f"./tournois/{tournament.name}")
        continue_or_quit()