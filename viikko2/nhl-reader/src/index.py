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


def hae_pelaajat(stats):
    search_type = input("Search by nationality (n) or team (t): ").strip().lower()
    if search_type == "t":
        team = input("Team (ANA/BOS/BUF...): ").strip().upper()
        return stats.top_scorers_by_team(team)
    if search_type == "n":
        nationality = input("Nationality (FIN/USA/CAN...): ").strip().upper()
        return stats.top_scorers_by_nationality(nationality)
    print("Choose n for nationality or t for team.")
    return None


def main():
    season = input("Season (2024-25): ")
    if season == "":
        season = "2024-25"
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = hae_pelaajat(stats)
    if players is None:
        return
    rprint(tee_taulukko(players))

if __name__ == "__main__":
    main()
