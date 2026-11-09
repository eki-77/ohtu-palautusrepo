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
    search_type = input("Search by nationality (n) or team (t): ").strip().lower()
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    if search_type == "t":
        team = input("Team (ANA/BOS/BUF...): ").strip().upper()
        players = stats.top_scorers_by_team(team)
    elif search_type == "n":
        nationality = input("Nationality (FIN/USA/CAN...): ").strip().upper()
        players = stats.top_scorers_by_nationality(nationality)
    else:
        print("Choose n for nationality or t for team.")
        return
    rprint(tee_taulukko(players))

if __name__ == "__main__":
    main()
