from hero import Hero
from orc import Orc
from random import randint


class Fight():

    def __init__(self, hero, orc):
        self.hero = self.set_hero(hero)
        self.orc = self.set_orc(orc)

    def set_hero(self, hero):
        if isinstance(hero, Hero):
            return hero
        else:
            print("That's not a hero")
            raise ValueError

    def set_orc(self, orc):
        if isinstance(orc, Orc):
            return orc
        else:
            print("That's not an orc")
            raise ValueError

    def get_player_sequence(self):
        if randint(0, 100) < 50:
            return (self.hero, self.orc)
        else:
            return (self.orc, self.hero)

    def simulate_fight(self):
        attacker, deffender = self.get_player_sequence()

        if not attacker.has_weapon():
            print("{} has no weapon and dies!".format(attacker.name))

        elif not deffender.has_weapon():
            print("{} has no weapon and dies!".format(deffender.name))

        else:
            while attacker.is_alive() and deffender.is_alive():
                damage = attacker.attack()
                deffender.take_damage(damage)
                print(("{} suffered {} damage and has {} "
                       "health after the attack of {}").format(
                    deffender.name, damage, deffender.get_health(),
                    attacker.name))
                attacker, deffender = deffender, attacker
