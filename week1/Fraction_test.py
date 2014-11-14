import unittest
from Fraction import Fraction


class FractionTests(unittest.TestCase):

    def setUp(self):
        self.a = Fraction(2, 3)
        self.b = Fraction(4, 5)

    def test_init(self):
        self.assertEqual(2, self.a._Fraction__nominator)
        self.assertEqual(3, self.a._Fraction__denominator)

    def test_eq_not_true(self):
        self.assertFalse(self.a == self.b)

    def test_eq_true(self):
        self.a._Fraction__nominator = 4
        self.a._Fraction__denominator = 5
        self.assertTrue(self.a == self.b)

    def test_lt_not_true(self):
        self.assertFalse(self.b < self.a)

    def test_lt_true(self):
        self.assertTrue(self.a < self.b)

    def test_gt_not_true(self):
        self.assertFalse(self.a > self.b)

    def test_gt_true(self):
        self.assertTrue(self.b > self.a)

    def test_add(self):
        fraction = self.a + self.b
        self.assertEqual("(22, 15)", fraction.__str__())
        self.assertEqual("(2, 3)", self.a.__str__())
        self.assertEqual("(4, 5)", self.b.__str__())

    def test_sub(self):
        fraction = self.a - self.b
        self.assertEqual("(-2, 15)", fraction.__str__())
        self.assertEqual("(2, 3)", self.a.__str__())
        self.assertEqual("(4, 5)", self.b.__str__())

    def test_lcm(self):
        self.assertEqual(15, self.a._Fraction__lcm(
            self.b._Fraction__denominator))

    def test_str(self):
        self.assertEqual("(2, 3)", self.a.__str__())

if __name__ == '__main__':
    unittest.main()
