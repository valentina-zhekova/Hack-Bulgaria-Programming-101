from weapon import Weapon
import unittest


class WeaponTests(unittest.TestCase):

    def setUp(self):
        self.the_weapon = Weapon("Mighty Axe", 25, 0.2)

    def test_weapon_init(self):
        self.assertEqual("Mighty Axe", self.the_weapon.type)
        self.assertEqual(25, self.the_weapon.damage)
        self.assertEqual(0.2, self.the_weapon.critical_strike_percent)

    def test_value_error(self):
            with self.assertRaises(ValueError):
                Weapon("", 25, 20)

    def test_critical_hit(self):
        true = False
        false = True
        for i in range(0, 1000):
            true = true or self.the_weapon.critical_hit()
            false = false and self.the_weapon.critical_hit()
        self.assertFalse(false)
        self.assertTrue(true)

if __name__ == '__main__':
    unittest.main()
