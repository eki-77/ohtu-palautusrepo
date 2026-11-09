import requests

class Player:
    def __init__(self, dict_p):
        self.name = dict_p['name']
        self.nationality = dict_p['nationality']
        self.assists = dict_p['assists']
        self.goals = dict_p['goals']
        self.team = dict_p['team']
        #self.games = dict_p['games']
        #self.id = dict_p['id']
        self.pisteet = int(dict_p['goals']) + int(dict_p['assists'])

    def __str__(self):
        return f"{self.name:22}{self.team:20}{self.goals} + {self.assists} = {self.pisteet}"
        #return [self.name, self.team, self.goals, self.assists, self.pisteet]

    def ala_tee_mitaan(self):
        return

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = self.get_players()

    def get_players(self):
        response = requests.get(self.url, timeout=10).json()
        players = []
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        return players

#    def ala_tee_mitaan(self):
#        return



class PlayerStats:
    def __init__(self, players):
        self.players = players.players

    def top_scorers_by_nationality(self, nat):
        natplayers = list(filter(lambda pelaaja: pelaaja.nationality == nat, self.players))
        natplayers.sort(key= lambda player: player.pisteet, reverse=True)
        return natplayers

    def ala_tee_mitaan(self):
        return

    def top_goal_scorers(self, how_many):
        '''palauttaa how_many määrän pelaajia, jotka ovat tehneet eniten maaleja'''
        sorted_players = sorted(self.players, key=lambda player: player.goals, reverse=True)
        return sorted_players[:how_many]
