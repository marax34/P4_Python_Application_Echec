from models.game import Game
from models.player import Player

class Round:
    def __init__(self, players):
        self.players = players
        self.games = []
        
    def generate_games(self):
         
        num_players = len(self.players)
        if num_players % 2 != 0:
            self.players.append(Player("BOT", "", 0))
            
        num_games = len(self.players) // 2 
        for i in range(num_games):
            game = (self.players[i*2], self.players[i*2 + 1])
            self.games.append(game)
            
        if num_players % 2 != 0:
            self.players.pop()
            
    def play_games(self):
        for player_1, player_2 in self.games:
            game = Game(player_1, player_2)
            if player_1.lastname != "BOT" and player_2.lastname != "BOT":
                print(f"Match en cours : {player_1.lastname} VS {player_2.firstname}")
            game.play()
            
    def to_json(self):
        # Convert round information to a dictionary
        round_info = {
            f"Round"
            "matchs": [
                {
                    "player_1": game[0].to_json(),
                    "player_2": game[1].to_json(),
                }
                for game in self.games
            ]
        }
        return round_info
    