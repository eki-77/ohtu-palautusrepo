import unittest
from types import SimpleNamespace

from player import PlayerStats


class StubPlayerReader:
    def __init__(self):
        self.players = [
            SimpleNamespace(name="Alex", nationality="CAN", team="BOS", goals=30, pisteet=60),
            SimpleNamespace(name="Blake", nationality="USA", team="BOS", goals=20, pisteet=70),
            SimpleNamespace(name="Casey", nationality="CAN", team="NYR", goals=50, pisteet=90),
            SimpleNamespace(name="Drew", nationality="CAN", team="BOS", goals=40, pisteet=50),
        ]


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.stats = PlayerStats(StubPlayerReader())

    def test_top_scorers_by_nationality_filters_and_sorts_by_points(self):
        result = self.stats.top_scorers_by_nationality("CAN")

        self.assertEqual([player.name for player in result], ["Casey", "Alex", "Drew"])

    def test_top_scorers_by_team_filters_and_sorts_by_points(self):
        result = self.stats.top_scorers_by_team("BOS")

        self.assertEqual([player.name for player in result], ["Blake", "Alex", "Drew"])

    def test_top_goal_scorers_returns_requested_number_in_descending_order(self):
        result = self.stats.top_goal_scorers(2)

        self.assertEqual([player.name for player in result], ["Casey", "Drew"])


if __name__ == "__main__":
    unittest.main()