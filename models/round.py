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
        
        remainining_players = self.players.copy()
        
        while len(remainining_players) > 1:
            player_1 = remainining_players.pop(0)
            
            player_2 = None
            for player in remainining_players:
                if player not in player_1.played_against:
                    player_2 = player
                    break
                
            if player_2 is None:
                break
            
            remainining_players.remove(player_2)
            player_1.played_against.append(player_2)
            player_2.played_against.append(player_1)
            self.games.append((player_1, player_2))
            
        if num_players % 2 != 0:
            self.players.pop()
            
    def play_games(self):
        for player_1, player_2 in self.games:
            game = Game(player_1, player_2)
            if player_1.lastname != "BOT" and player_2.lastname != "BOT":
                print(f"Match en cours : {player_1.lastname} VS {player_2.lastname}")
            game.play()
            
            
    def to_json(self):
        # Convert round information to a dictionary
        round_info = {
            f"Round": [
                {
                "player_1": game[0].to_json(),
                "player_2": game[1].to_json(),
                }
                for game in self.games
            ]
        }
        return round_info
    