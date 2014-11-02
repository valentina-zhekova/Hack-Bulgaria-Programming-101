from orc import Orc
from weapon import Weapon
import unittest


class OrcTests(unittest.TestCase):

    def setUp(self):
        self.the_orc = Orc("Oplik", 122, 1.42)

    def test_orc_init(self):
        self.assertEqual(1.42, self.the_orc.berserk_factor)

    def test_set_berserk_factor(self):
        self.the_orc.set_berserk_factor(2.55)
        self.assertEqual(2, self.the_orc.berserk_factor)
        self.the_orc.set_berserk_factor(0.55)
        self.assertEqual(1, self.the_orc.berserk_factor)

    def test_orc_attack_no_weapon(self):
        self.assertEqual(0, self.the_orc.attack())

    # that's a stupid test, fix it later!
    def test_orc_attack(self):
        weapon = Weapon("spoon", 2, 0.7)
        self.the_orc.equip_weapon(weapon)
        critical = False
        normal = False
        critical_num = 4 * self.the_orc.berserk_factor
        normal_num = 2 * self.the_orc.berserk_factor
        for i in range(0, 1000):
            critical = critical or (critical_num == self.the_orc.attack())
            normal = normal or (normal_num == self.the_orc.attack())
        self.assertTrue(critical)
        self.assertTrue(normal)

if __name__ == '__main__':
    unittest.main()
