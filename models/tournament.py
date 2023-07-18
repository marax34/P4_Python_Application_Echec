class Tournament:
    def __init__(self, name, 
                place, 
                start, 
                end, 
                round_number, 
                number_of_round=4
                ):
        
        self.name = name
        self.place = place
        self.start = start
        self.end = end
        self.round_number = round_number
        self.number_of_round = number_of_round
        self.players = []
        self.rounds = []
        
        
    
    def __str__(self):
        players_infos = "\n".join([str(player) for player in self.players])
        return (
            f"Nom du tournoi: {self.name}"
            f"Lieu du tournoi: {self.place}"
            f"Début du tournoi: {self.start}"
            f"Fin du tournoi: {self.end}"
            f"Round n°: {self.round_number}"
            f"Nombre de tours: {self.number_of_round}"
            f"Liste des joueurs inscrits: {players_infos}"
            f"Liste des tours: {self.rounds}"
        )