import os
import json
from models.player import Player
from models.tournament import Tournament
from models.game import Game
from models.round import Round


def writeJson(directory_path, file_path, data):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    with open(file_path, "w") as file:
        json.dump(data, file)

    print("Les données ont bien été enregistrées")


def loadJson(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def load_tournament(file_path):
    try:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)

            name = data["Nom"]
            place = data["Lieu du tournoi"]
            start = data["Debut du tournoi"]
            end = data["Fin du tournoi"]
            round_in_progress = data["Round en cours"]
            # game_in_progress = data["Match en cours"]
            number_of_rounds = data["Nombre de rounds"]

            players_data = data["Joueurs inscrits"]
            players = []
            for player_data in players_data:
                player = Player(
                                player_data["Nom"],
                                player_data["Prenom"],
                                player_data["Age"]
                                )
                player.score = player_data["Score"]
                players.append(player)

            players_ranking_data = data["Classement des joueurs"]
            players_ranking = []
            for player_data in players_ranking_data:
                player = Player(
                                player_data["Nom"], player_data["Prenom"],
                                player_data["Age"]
                                )
                player.score = player_data["Score"]
                player.index = player_data["Index"]
                # player.played_against = player_data["Joueurs affrontés"]
                players_ranking.append(player)
            round = Round(players_ranking)

            rounds_data = data["Rounds Infos"]
            rounds = []
            for round_data in rounds_data:
                round_info = round_data["Round"]
                for game_data in round_info:
                    player_1_data = game_data["player_1"]
                    player_2_data = game_data["player_2"]
                    player_1 = Player(player_1_data["Nom"],
                                      player_1_data["Prenom"],
                                      player_1_data["Age"])
                    player_1.score = player_1_data["Score"]
                    player_2 = Player(player_2_data["Nom"],
                                      player_2_data["Prenom"],
                                      player_2_data["Age"]
                                      )
                    player_2.score = player_2_data["Score"]
                    # round.games.append((player_1, player_2))
                    game = Game(player_1, player_2)
                    round.games.append(game)
                # round.current_game = game_in_progress
                rounds.append(round)

            tournament = Tournament(name, place, start, end, players,
                                    players_ranking, number_of_rounds)
            tournament.current_round = round_in_progress
            tournament.rounds = rounds
            return tournament

    except FileNotFoundError:
        print(f"Fichier {file_path} introuvable.")
        return None
    except json.JSONDecodeError:
        print(f"Erreur de décodage JSON pour le fichier {file_path}.")
        return None

def load_winner(file_path):
    try:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            
        player_ranking = data["Classement des joueurs"]
        
        winner = player_ranking[0]
        winner_infos = Player(winner["Nom"], winner["Prenom"], winner["Score"])
        print(f"Le vainqueur est {winner_infos.lastname}, {winner_infos.firstname} avec un score de {winner_infos.score}")
        
    except FileNotFoundError:
        print(f"Fichier {file_path} introuvable.")
        return None
    except json.JSONDecodeError:
        print(f"Erreur de décodage JSON pour le fichier {file_path}.")
        return None
        