from models.player import Player
from controllers.json_function import writeJson
from controllers import regex_validation


def players_for_competition():
    """
    Function to add all the players from club at competition list of players.
    """
    players = []
    print("Merci d'inscrire les joueurs à la compétition annuelle:")
    number_of_players = int(input(
        "Combien de joueurs souhaitez-vous inscrire ? "
        ))
    i = 1
    while i <= number_of_players:
        lastname = regex_validation.is_name_valid(
            "Entrer le nom du joueur: "
            )
        firstname = regex_validation.is_name_valid(
            "Entrer le prénom du joueur: "
            )
        while True:
            age = input("Entrer l'age du joueur: ")
            if not age.isdigit():
                print("L'âge doit être un nombre entier veuillez réessayer: ")
            else:
                break
        player = Player(lastname, firstname, age)

        player_exists = any(
            registered.lastname.lower() == player.lastname.lower()
            and registered.firstname.lower() == player.firstname.lower()
            and registered.age == player.age
            for registered in players
        )
        if player_exists:
            print("Le joueur est déjà inscrit à la compétition")
        else:
            player.set_index(i)
            players.append(player)
            print(f"Joueur {i} inscrit:\n{player}")
            players.sort(key=lambda player:
                         (player.lastname, player.firstname))
            i += 1

    writeJson("./competition", "./competition/players.json",
              [player.to_json() for player in players])
