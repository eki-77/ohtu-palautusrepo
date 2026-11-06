from rich import print as rprint
from rich.table import Table
from player import PlayerReader, PlayerStats

def tee_taulukko(players):
    taulukko = Table(title="Players")
    taulukko.add_column("name", style="cyan")
    taulukko.add_column("teams")
    taulukko.add_column("goals", style="green")
    taulukko.add_column("assists", style="green")
    taulukko.add_column("points", style="green")
    for player in players:
        taulukko.add_row(player.name, player.team, str(player.goals),
        str(player.assists), str(player.pisteet))
    return taulukko


def main():
    season = input("Season (2024-25): ")
    if season == "":
        season = "2024-25"
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    nationality = input("Nationality (FIN/USA/CAN...): ")
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)
    rprint(tee_taulukko(players))

if __name__ == "__main__":
    main()
