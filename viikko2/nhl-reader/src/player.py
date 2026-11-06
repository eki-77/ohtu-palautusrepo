import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.games = dict['games']
        self.id = dict['id']
        self.pisteet = int(dict['goals']) + int(dict['assists'])
    
    def __str__(self):
        return f"{self.name:22}{self.team:20}{self.goals} + {self.assists} = {self.pisteet}"

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = self.get_players()

    def get_players(self):
        response = requests.get(self.url).json()
        players = []
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        return players



class PlayerStats:
    def __init__(self, players):
        self.players = players.players

    def top_scorers_by_nationality(self, nat):
        natplayers = list(filter(lambda pelaaja: pelaaja.nationality == nat, self.players))
        natplayers.sort(key= lambda player: player.pisteet, reverse=True)
        return natplayers
