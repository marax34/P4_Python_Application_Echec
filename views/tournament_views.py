import json
import sys
sys.path.append('./')
from controllers.json_function import loadJson
from models.tournament import Tournament
from models.player import Player
from models.game import Game

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
            if player_lastname == player["Nom"] and player_firstname == player["Prenom"]:
                player = Player(player["Nom"], player["Prenom"], player["Age"])
                players.append(player)
                print(f"Joueur {i}  inscrit:\n{player}")
                player_found = True
                i+=1
                break
        if not player_found:
            print("Le joueur saisi n'est pas inscrit à la competition")
    players.sort(key=lambda player: (player.lastname, player.firstname))    
    for player in players:
        print(player)
    
    return players

def create_tournament():
    print ("Création du tournoi:\nMerci d'entrer les informations suivantes: ")
    name = input("Nom du Tournoi: ")
    place = input("Lieu du Tournoi: ")
    start = input("Date de début du Tournoi: ")
    end = input("Date de fin du Tournoi: ")
    round_number = input("N° du round en cours: ")
    number_of_rounds = input("Nombre de rounds: ")
    players = select_players()
    
    tournament = Tournament(name, place, start, end, round_number, players, number_of_rounds)
    print(tournament)

create_tournament()