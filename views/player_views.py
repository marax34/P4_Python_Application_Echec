import sys
import json
import os
sys.path.append("./")
from models.player import Player
from controllers.json_function import writeJson

def PlayersForCompetition():
    players = []
    print("Merci d'inscrire les joueurs à la compétition annuelle:")
    number_of_players = int(input("Combien de joueurs souhaitez-vous inscrire ? "))
    for i in range(1, number_of_players + 1 ):
        lastname = input("Entrer le nom du joueur: ")
        firstname = input("Entrer le prénom du joueur: ")
        age = input("Entrer l'age du joueur: ")
        player = Player(lastname, firstname, age)
        players.append(player)
        print(f"Joueur {i} inscrit:\n{player}")
        
    players_data = []
    for player in players:
        print(f"{player.lastname} "
              f"{player.firstname} "
              f"{player.age} "
            )
        player_data = {
            "Nom": player.lastname,
            "Prenom": player.firstname,
            "Age": player.age
        }
        players_data.append(player_data)
        
    print(players_data)
    
    writeJson("./competition", "./competition/players.json", players_data)
    
PlayersForCompetition()
    
    
    