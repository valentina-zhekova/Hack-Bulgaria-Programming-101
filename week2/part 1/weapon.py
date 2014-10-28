from random import randint


class Weapon:

    def __init__(self, type, damage, critical_strike_percent):
        self.type = type
        self.damage = damage
        self.set_critical_strike_percent(critical_strike_percent)

    def set_critical_strike_percent(self, critical_strike_percent):
        if critical_strike_percent >= 0 and critical_strike_percent <= 1:
            self.critical_strike_percent = critical_strike_percent
        else:
            raise ValueError

    def critical_hit(self):
        return randint(0, 1) <= self.critical_strike_percent
