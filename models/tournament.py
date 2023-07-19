class Tournament:
    def __init__(self, name, 
                place, 
                start, 
                end, 
                round_number,
                players,
                number_of_rounds=4
                ):
        
        self.name = name
        self.place = place
        self.start = start
        self.end = end
        self.round_number = round_number
        self.players = players
        self.number_of_rounds = number_of_rounds
        self.rounds = []
        
        
    
    def __str__(self):
        players_infos = "\n".join([str(player) for player in self.players])
        return (
            f"Nom du tournoi: {self.name}\n"
            f"Lieu du tournoi: {self.place}\n"
            f"Début du tournoi: {self.start}\n"
            f"Fin du tournoi: {self.end}\n"
            f"Round n°: {self.round_number}\n"
            f"Nombre de tours: {self.number_of_rounds}\n"
            f"Liste des joueurs inscrits: {players_infos}\n"
            f"Liste des tours: {self.rounds}"
        )