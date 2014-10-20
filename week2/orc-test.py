from orc import Orc
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

if __name__ == '__main__':
    unittest.main()
