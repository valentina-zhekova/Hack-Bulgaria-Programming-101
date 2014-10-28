import unittest
from prepareMeal import *


class PrepareMealTests(unittest.TestCase):

    def test_prepare_meal(self):
        self.assertEqual("spam and eggs", prepare_meal(15))
        self.assertEqual("spam spam and eggs", prepare_meal(45))

    def test_prepare_meal_only_spam_condition_true(self):
        self.assertEqual("spam", prepare_meal(3))
        self.assertEqual("spam spam spam", prepare_meal(27))

    def test_prepare_meal_only_eggs_condition_true(self):
        self.assertEqual("eggs", prepare_meal(5))

    def test_prepare_meal_no_condition_true(self):
        self.assertEqual("", prepare_meal(7))

    def test_spam_condition_is_n_the_largest_possible(self):
        self.assertEqual(2, spam_condition(18))

    def test_spam_condition_is_not_possible(self):
        self.assertEqual(0, spam_condition(8))

    def test_spam_only_once(self):
        self.assertEqual("spam", spam(1))

    def test_spam_none(self):
        self.assertEqual("", spam(0))

    def test_spam_accurate_string_when_more_than_once(self):
        self.assertEqual("spam spam spam", spam(3))

    def test_eggs_true_but_zero_spam(self):
        self.assertEqual("eggs", eggs(5))

    def test_eggs_none(self):
        self.assertEqual("", eggs(7))

    def test_eggs_accurate_string_otherwise(self):
        self.assertEqual(" and eggs", eggs(45))

if __name__ == '__main__':
    unittest.main()

# ако имаме default arguments става кофти при инстанциране на много обекти
