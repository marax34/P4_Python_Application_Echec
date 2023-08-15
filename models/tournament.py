import os
import json
import random


class Tournament:
    def __init__(self, name,
                 place,
                 start,
                 end,
                 players,
                 players_ranking,
                 number_of_rounds=4
                 ):

        self.name = name
        self.place = place
        self.start = start
        self.end = end
        self.current_round = 1
        self.players = players
        self.players_ranking = players_ranking
        self.number_of_rounds = number_of_rounds
        self.rounds = []

    def next_round(self):
        self.current_round += 1

    def shuffle_players(self):
        random.shuffle(self.players_ranking)

    def to_json(self):
        tournament_info = {
            "Nom": self.name,
            "Lieu du tournoi": self.place,
            "Debut du tournoi": self.start,
            "Fin du tournoi": self.end,
            "Round en cours": self.current_round,
            "Nombre de rounds": self.number_of_rounds,
            "Joueurs inscrits": [player.to_json() for player in self.players],
            "Classement des joueurs": [player.to_json()
                                       for player in self.players_ranking],
            "Rounds Infos": [round.to_json() for round in self.rounds]
        }
        return tournament_info

    def save_to_json(self, file_name):
        if not os.path.exists("./tournois"):
            os.makedirs("./tournois")

        with open(file_name, 'w') as json_file:
            json.dump(self.to_json(), json_file, indent=4)

    def __str__(self):
        players_infos = "\n".join([str(player) for player in self.players])
        return (
            f"Nom du tournoi: {self.name}\n"
            f"Lieu du tournoi: {self.place}\n"
            f"Début du tournoi: {self.start}\n"
            f"Fin du tournoi: {self.end}\n"
            f"Round n°: {self.current_round}\n"
            f"Nombre de tours: {self.number_of_rounds}\n"
            f"Liste des joueurs inscrits: {players_infos}\n"
            f"Liste des tours: {self.rounds}"
        )
