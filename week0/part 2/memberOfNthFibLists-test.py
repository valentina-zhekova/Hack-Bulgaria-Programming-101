import unittest
from memberOfNthFibLists import *


class MemberOfNthFibListsTests(unittest.TestCase):

    def test_member_of_nth_fib_lists_true(self):
        self.assertTrue(member_of_nth_fib_lists(
            [1, 2], [3, 4], [1, 2, 3, 4, 3, 4, 1, 2, 3, 4]))
        self.assertTrue(member_of_nth_fib_lists(
            [7, 11], [2], [7, 11, 2, 2, 7, 11, 2]))

    def test_member_of_nth_fib_lists_false(self):
        self.assertFalse(member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))
        self.assertFalse(member_of_nth_fib_lists(
            [7, 11], [2], [11, 7, 2, 2, 7]))

if __name__ == '__main__':
    main()
