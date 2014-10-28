from weapon import Weapon


class Entity:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self._MAX_HEALTH = health
        self.weapon = None

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage_points):
        if damage_points > self.health:
            self.health = 0
        else:
            self.health -= damage_points

    def take_healing(self, healing_points):
        if healing_points > 0 and self.health > 0:
            self.health += healing_points
            if self.health > self._MAX_HEALTH:
                self.health = self._MAX_HEALTH
            return True
        else:
            return False

    def has_weapon(self):
        return self.weapon is not None

    def equip_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.weapon = weapon
        else:
            raise ValueError
            print("That's not a weapon")  # order?

    def attack(self):
        if self.has_weapon():
            if self.weapon.critical_hit():
                return self.weapon.damage * 2
            else:
                return self.weapon.damage
        else:
            return 0
