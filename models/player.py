class Player:
    def __init__(self, lastname, firstname, age, score=0):
        self.lastname = lastname
        self.firstname = firstname
        self.age = int(age)
        self.score = score
        self.index = None
        self.played_against = []
        
    def set_index(self, index):
        self.index = index
        
    def win_game(self):
        self.score += 1
        
    def loose_game(self):
        self.score -= 1
        
    def draw(self):
        self.score += 0.5
        
    def to_json(self):
        player_info = {
            "Nom": self.lastname,
            "Prenom": self.firstname,
            "Age": self.age,
            "Score": self.score          
        }
        return player_info
        
    def __str__(self):
        if self.index is not None:
            return f"{self.index}. {self.firstname} {self.lastname} ({self.age} ans)"
        else:
            return f"{self.firstname} {self.lastname} ({self.age} ans)"
        