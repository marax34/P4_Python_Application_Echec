import json
import sys
sys.path.append('./')
from controllers.json_function import loadJson
from models.tournament import Tournament
from models.player import Player

tournament = Tournament("Echec Master", "Lyon", "13/08/2023", "20/08/2023", "2", "12")

def select_players():
    """
    Function to find a player in the list of players from competition:
    We load the list of players, choose the number of players we want to register 
    to the tournament en enter lastname and firstname to find the player
    
    """
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
                tournament.players.append(player)
                print(f"Joueur {i}  inscrit:\n{player}")
                player_found = True
                i+=1
                break
        if not player_found:
            print("Le joueur saisi n'est pas inscrit à la competition")
    tournament.players.sort(key=lambda player: (player.lastname, player.firstname))    
    for player in tournament.players:
        print(player)       

select_players()

