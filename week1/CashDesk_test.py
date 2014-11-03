import unittest
from CashDesk import CashDesk


class CashDeskTests(unittest.TestCase):

    def setUp(self):
        self.my_cash_desk = CashDesk()

    def test_init(self):
        self.assertEqual({100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0},
                         self.my_cash_desk.money)

    def test_take_money(self):
        self.my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
        self.assertEqual({100: 0, 50: 1, 20: 1, 10: 0, 5: 0, 2: 0, 1: 2},
                         self.my_cash_desk.money)

    def test_total(self):
        self.my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
        self.assertEqual(72, self.my_cash_desk.total())

    def test_can_withdraw_money_no_such_banknotes(self):
        self.my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
        self.assertFalse(self.my_cash_desk.can_withdraw_money(30))

    def test_can_withdraw_money_possible(self):
        self.my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
        self.assertTrue(self.my_cash_desk.can_withdraw_money(70))

if __name__ == '__main__':
    unittest.main()
