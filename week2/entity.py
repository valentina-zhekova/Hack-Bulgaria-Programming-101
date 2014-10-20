class Entity:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self._MAX_HEALTH = health

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
