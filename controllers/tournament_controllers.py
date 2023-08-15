from models.round import Round
from views.tournament_views import continue_or_quit
from controllers.json_function import load_winner
import sys
import time


def play_tournament(tournament):
    print(tournament.number_of_rounds)
    for round_num in range(tournament.current_round,
                           (tournament.number_of_rounds) + 1):
        tournament.current_round = round_num
        print(f"Début du round {tournament.current_round}: ")
        round = Round(tournament.players_ranking)
        round.generate_games()
        round.play_games()
        tournament.players_ranking.sort(key=lambda player: (player.score),
                                        reverse=True)
        tournament.rounds.append(round)
        if tournament.current_round != tournament.number_of_rounds + 1:
            tournament.next_round()
        tournament.save_to_json(f"./tournois/{tournament.name}")
        if tournament.current_round == tournament.number_of_rounds + 1:
            load_winner(f"./tournois/{tournament.name}")
            print("Tournoi terminé")
            time.sleep(2)
            sys.exit()
        else:
            continue_or_quit()
