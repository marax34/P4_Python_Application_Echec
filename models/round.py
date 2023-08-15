from models.game import Game
from models.player import Player


class Round:
    def __init__(self, players):
        self.players = players
        self.games = []
        self.current_game = 0

    def next_game(self):
        self.current_game += 1

    def generate_games(self):

        num_players = len(self.players)
        if num_players % 2 != 0:
            self.players.append(Player("BOT", "", 0))

        remainining_players = self.players.copy()

        while len(remainining_players) > 1:
            player_1 = remainining_players.pop(0)

            player_2 = None
            for player in remainining_players:
                if player.index not in player_1.played_against:
                    player_2 = player
                    break

            if player_2 is None:
                break

            remainining_players.remove(player_2)
            player_1.played_against.append(player_2.index)
            player_2.played_against.append(player_1.index)
            game = Game(player_1, player_2)
            self.games.append(game)
            # self.games.append((player_1, player_2))

        if num_players % 2 != 0:
            self.players.pop()

    def play_games(self):
        total_games = len(self.games)
        for i in range(self.current_game, (total_games)):
            game = self.games[i]
            player_1, player_2 = game.player_1, game.player_2
            if player_1.lastname != "BOT" and player_2.lastname != "BOT":
                print(f"Match en cours : {player_1.lastname} VS "
                      f"{player_2.lastname}")
            else:
                print(f"{player_1.lastname} n'a pas d'adversaire "
                      "il ne marque ni ne gagne de point")
            self.games[i].play()
            self.next_game()

    def to_json(self):
        # Convert round information to a dictionary
        round_info = {
            "Round": [
                game.to_json()
                for game in self.games
            ],
            # "Match en cours": self.current_game
        }
        return round_info
