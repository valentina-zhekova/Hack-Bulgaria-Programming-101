from hero import Hero
import unittest


class HeroTests(unittest.TestCase):

    def setUp(self):
        self.the_hero = Hero("Bron", 100, "DragonSlayer")

    def test_hero_init(self):
        self.assertEqual("DragonSlayer", self.the_hero.nickname)

    def test_known_as(self):
        self.assertEqual("Bron the DragonSlayer", self.the_hero.known_as())

if __name__ == '__main__':
    unittest.main()
