import unittest
from isAnBn import *


class IsAnBnTests(unittest.TestCase):

    def test_is_an_bn_empty(self):
        self.assertTrue(is_an_bn(""))

    def test_is_an_bn_don_t_have_a_at_all(self):
        self.assertFalse(is_an_bn("turtles"))

    def test_is_an_bn_accurate_otherwise(self):
        self.assertFalse(is_an_bn("rado"))
        self.assertFalse(is_an_bn("aaabb"))
        self.assertTrue(is_an_bn("aaabbb"))
        self.assertFalse(is_an_bn("aabbaabb"))
        self.assertFalse(is_an_bn("bbbaaa"))
        self.assertTrue(is_an_bn("aaaaabbbbb"))

if __name__ == '__main__':
    unittest.main()
