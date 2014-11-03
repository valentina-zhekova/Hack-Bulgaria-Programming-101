class CashDesk:

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
            banknotes = [100, 50, 20, 10, 5, 2, 1]
            for banknote in banknotes:
                if self.money[banknote] > 0:
                    times = min(amount_of_money // banknote,
                                self.money[banknote])
                    amount_of_money -= banknote * times
            return amount_of_money == 0
        return True
