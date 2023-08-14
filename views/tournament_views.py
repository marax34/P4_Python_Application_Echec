import json
import sys
sys.path.append('./')
from controllers.json_function import loadJson
from models.tournament import Tournament
from models.player import Player
from models.game import Game
from models.round import Round
import time

def select_players():
    """
    Function to find a player in the list of players from competition:
    We load the list of players, choose the number of players we want to register 
    to the tournament en enter lastname and firstname to find the player
    
    """
    players = []
    data = loadJson("./competition/players.json")
    print("Inscription des joueurs au tournoi")
    number_of_players = int(input("Combien de joueurs souhaitez vous inscrire ?: "))
    i = 1
    while i <= number_of_players:
        player_lastname = input("Entrer le nom du joueur: ")
        player_firstname = input("Entrez le prénom du joueur: ")
        player_found = False
        for player in data:
            if player_lastname.lower() == player["Nom"] and player_firstname.lower() == player["Prenom"]:
                player = Player(player["Nom"], player["Prenom"], player["Age"])
                player.set_index(i)
                players.append(player)
                print(f"Joueur {i}  inscrit:\n{player}")
                player_found = True
                i+=1
                break
        if not player_found:
            print("Le joueur saisi n'est pas inscrit à la competition")
    players_ranking = players.copy()
    players.sort(key=lambda player: (player.lastname, player.firstname))    
    for player in players:
        print(player)
    
    return players, players_ranking

def create_tournament():
    """Create a tournament while entering all the informations necessary.
    For the list of players we use the select_players function"""
    print ("Création du tournoi:\nMerci d'entrer les informations suivantes: ")
    name = input("Nom du Tournoi: ")
    place = input("Lieu du Tournoi: ")
    start = input("Date de début du Tournoi: ")
    end = input("Date de fin du Tournoi: ")
    number_of_rounds = int(input("Nombre de rounds: "))
    players, players_ranking = select_players()
    
    tournament = Tournament(name, place, start, end, players, players_ranking, number_of_rounds)
    return(tournament)

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

"""tournament = create_tournament()
for player in tournament.players:
    print(player)
tournament.save_to_json(f"./tournois/{tournament.name}")
tournament.shuffle_players()
print(f" Début du Round {tournament.current_round}: ")
for round in range(tournament.number_of_rounds):
    round = Round(tournament.players_ranking)
    round.generate_games()
    round.play_games()
    tournament.players_ranking.sort(key= lambda player: (player.score), reverse = True)
    tournament.rounds.append(round)
    tournament.save_to_json(f"./tournois/{tournament.name}")
    time.sleep(2)"""

