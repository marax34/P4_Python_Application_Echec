from controllers.json_function import loadJson
from models.tournament import Tournament
from models.player import Player
from controllers import regex_validation
import sys


def select_players():
    """
    Function to find a player in the list of players from competition:
    We load the list of players, choose the number of players we want to register 
    to the tournament en enter lastname and firstname to find the player.
    If the player is not in the competition list we send an error same as if we already
    registered the player in the list
    
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
        for resgistered in data:
            if player_lastname.lower() == resgistered["Nom"] and player_firstname.lower() == resgistered["Prenom"]:
                player = Player(resgistered["Nom"], resgistered["Prenom"], resgistered["Age"])
                player.index = resgistered["Index"]
                player_exists = any(
                    player.index == e.index
                    for e in players
                )
                if player_exists:
                    print("Le joueur saisi est déjà inscrit au tournoi")
                else:
                    players.append(player)
                    print(f"Joueur {i}  inscrit:\n{player}")
                    player_found = True
                    i+=1
                    break
        if not player_found and not player_exists:
            print("Le joueur saisi n'est pas inscrit à la competition")
    players_ranking = players.copy()
    players.sort(key=lambda player: (player.lastname, player.firstname))    
    for player in players:
        print(players)
    
    return players, players_ranking

def create_tournament():
    """This fonction is made to Create a tournament while entering all the informations necessary.
    For the list of players we use the select_players function"""
    print ("Création du tournoi:\nMerci d'entrer les informations suivantes: ")
    name = regex_validation.is_name_valid("Nom du Tournoi: ")
    place = regex_validation.is_name_valid("Lieu du Tournoi: ")
    start = regex_validation.is_date_valid("Date de début du tournoi: ")
    end = regex_validation.is_date_valid("Date de fin du Tournoi: ")
    number_of_rounds = int(input("Nombre de rounds: "))
    players, players_ranking = select_players()
    
    tournament = Tournament(name, place, start, end, players, players_ranking, number_of_rounds)
    return(tournament)

def continue_or_quit():
    choice = input("Tapez 1 pour continuer ou une touche pour quitter ?")
    if choice == "1":
        print("Le tournoi continue")
    else:
        print("Aurevoir")
        sys.exit()


"""def play_tournament(tournament):
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
        continue_or_quit()"""