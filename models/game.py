class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        
    def play(self):
        result = input("Entrer le nom du vainqueur: ")
        if result == self.player_1.lastname:
            self.player_1.win_game()
            self.player_2.loose_game()    
        elif result == self.player_2.lastname:
            self.player_2.win_game()
            self.player_1.loose_game()
        else:
            self.player_1.draw()
            self.player_2.draw()
        
        
        