from player import Player, PlayerReader, PlayerStats
from rich import print as rprint
from rich.table import Table

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    taulukko = Table(title="Players")
    taulukko.add_column("name", style="cyan")
    taulukko.add_column("teams")
    taulukko.add_column("goals", style="green")
    taulukko.add_column("assists", style="green")
    taulukko.add_column("points", style="green")
    for player in players:
        taulukko.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.pisteet))
    rprint(taulukko)

if __name__ == "__main__":
    main()
