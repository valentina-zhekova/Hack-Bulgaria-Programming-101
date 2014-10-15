class CashDesk():

    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, taken_money):
        for key in taken_money:
            self.money[key] = self.money[key] + taken_money[key]

    def total(self):
        total = 0
        for key in self.money:
            total += key * self.money[key]
        return total

    def can_withdraw_money(self, amount_of_money):
        if self.total() >= amount_of_money:
            # update money dictionary !!!
            return True
        return False

my_cash_desk = CashDesk()
my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
print(my_cash_desk.total())
print(my_cash_desk.can_withdraw_money(30))
print(my_cash_desk.can_withdraw_money(70))
