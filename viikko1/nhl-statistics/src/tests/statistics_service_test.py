import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_palauttaa_oikean_pelaajan(self):
        pelaaja = self.stats.search("Kurri")
        self.assertEqual(pelaaja.name, "Kurri")
        self.assertEqual(pelaaja.team, "EDM")
        self.assertEqual(pelaaja.goals, 37)
        self.assertEqual(pelaaja.assists, 53)

    def test_search_pelaajaa_ei_ole(self):
        pelaaja = self.stats.search("Selänne")
        self.assertEqual(pelaaja, None)
    
    def test_hakee_oikean_tiimin(self):
        pelaajalista = self.stats.team("PIT")
        self.assertEqual(len(pelaajalista), 1)
        self.assertEqual(str(pelaajalista[0]), "Lemieux PIT 45 + 54 = 99")
    
    def test_hakee_oikean_top_listan(self):
        pelaajalist = self.stats.top(3)
        #top antaa yhden liikaa
        self.assertEqual(len(pelaajalist), 4)
        self.assertEqual(str(pelaajalist[0]), "Gretzky EDM 35 + 89 = 124")
        self.assertEqual(str(pelaajalist[1]), "Lemieux PIT 45 + 54 = 99")
        self.assertEqual(str(pelaajalist[2]), "Yzerman DET 42 + 56 = 98")
        self.assertEqual(str(pelaajalist[3]), "Kurri EDM 37 + 53 = 90")
    
    def test_top_pisteiden_perusteella(self):
        pelaajalista = self.stats.top(1, SortBy.POINTS)
        self.assertEqual(str(pelaajalista[0]), "Gretzky EDM 35 + 89 = 124")
    
    def test_top_maalien_perusteella(self):
        pelaajalista = self.stats.top(1, SortBy.GOALS)
        self.assertEqual(str(pelaajalista[0]), "Lemieux PIT 45 + 54 = 99")
    
    def test_top_syottojen_perusteella(self):
        pelaajalista = self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual(str(pelaajalista[0]), "Gretzky EDM 35 + 89 = 124")

    