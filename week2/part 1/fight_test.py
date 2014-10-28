from fight import Fight
from hero import Hero
from orc import Orc
from weapon import Weapon
import unittest


class FightTests(unittest.TestCase):

    def setUp(self):
        self.hero = Hero("Don Quixote", 9.99, "The Common Sense")
        self.orc = Orc("Oplik", 10, 0.3)
        self.fight = Fight(self.hero, self.orc)
        self.spoon = Weapon("Rounded Spoon", 2, 0.7)
        self.knife = Weapon("Rusty Knife", 6, 0.3)
        self.orc.weapon = self.knife
        self.hero.weapon = self.spoon

    def test_fight_init(self):
        self.assertEqual(self.hero, self.fight.hero)
        self.assertEqual(self.orc, self.fight.orc)

    def test_set_hero_value_error(self):
        with self.assertRaises(ValueError):
            Fight("pancake", self.orc)

    def test_set_orc_value_erroe(self):
        with self.assertRaises(ValueError):
            Fight(self.hero, "pancake")

    def test_get_player_sequence(self):
        h = False
        o = False
        for i in range(0, 1000):
            h = h or (self.fight.get_player_sequence()
                      == (self.hero, self.orc))
            o = o or (self.fight.get_player_sequence()
                      == (self.orc, self.hero))
        self.assertTrue(h)
        self.assertTrue(o)

    def test_simulate_fight(self):
        self.fight.simulate_fight()
        self.assertFalse(self.fight.orc.is_alive()
                         and self.fight.hero.is_alive())

    def test_simulate_fight_no_weapon_orc(self):
        self.fight.orc.weapon = None
        self.fight.simulate_fight()
        self.assertFalse(self.fight.orc.is_alive())

    def test_simulate_fight_no_weapon_hero(self):
        self.fight.hero.weapon = None
        self.fight.simulate_fight()
        self.assertFalse(self.fight.hero.is_alive())

# att, def = def, att
# get_player_sequence --> (h, o)
if __name__ == '__main__':
    unittest.main()
