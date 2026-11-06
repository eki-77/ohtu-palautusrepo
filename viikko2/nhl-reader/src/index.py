import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Suomalaiset pelaajat: ")
    print("")
    
    finplayers = list(filter(lambda pelaaja: pelaaja.nationality == 'FIN', players))
    finplayers.sort(key= lambda player: player.pisteet, reverse=True)

    for player in finplayers:
        print(player)

if __name__ == "__main__":
    main()
