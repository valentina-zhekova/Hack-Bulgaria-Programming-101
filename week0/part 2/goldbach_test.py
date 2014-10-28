import unittest
from goldbach import *


class GoldbachTests(unittest.TestCase):

    def test_goldbach_is_odd(self):
        self.assertEqual([], goldbach(7))

    def test_goldbach_accurate_for_even_numbers(self):
        self.assertEqual([(2, 2)], goldbach(4))
        self.assertEqual([(3, 3)], goldbach(6))
        self.assertEqual([(3, 5)], goldbach(8))
        self.assertEqual([(3, 7), (5, 5)], goldbach(10))
        self.assertEqual([(3, 97), (11, 89), (17, 83), (29, 71),
                        (41, 59), (47, 53)], goldbach(100))

    def test_is_prime_for_negative_number(self):
        self.assertTrue(is_prime(-7))
        self.assertFalse(is_prime(-8))

    def test_is_prime_for_not_prime_number(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(6))

    def test_is_prime_for_prime_numbers(self):
        self.assertTrue(is_prime(5))

if __name__ == '__main__':
    unittest.main()
