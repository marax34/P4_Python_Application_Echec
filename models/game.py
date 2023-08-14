class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        
    def to_json(self):
        return {
            "player_1": self.player_1.to_json(),
            "player_2": self.player_2.to_json(),
        }
        
    def play(self):
        if self.player_1.lastname == "BOT" or self.player_2.lastname == "BOT":
            return
        while True:
            result = input("Entrer le nom du vainqueur ou entrer 'draw' si égalité: ")
            if result == self.player_1.lastname:
                self.player_1.win_game()
                self.player_2.loose_game()
                break
            elif result == self.player_2.lastname:
                self.player_2.win_game()
                self.player_1.loose_game()
                break
            elif result.lower() == "draw":
                self.player_1.draw()
                self.player_2.draw()
                break
            else:
                print("Merci de choisir un joueur présent dans le match ou écrire draw si égalité")
            
            
        
        