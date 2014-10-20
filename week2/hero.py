from entity import Entity


class Hero(Entity):

#watch -n 1 python3 hero-test.py
#всяка специфика в отделен тест
#няма смисъл да тестваме наследяването, смо новите функции за класа

    def __init__(self, name, health, nickname):
        super().__init__(name, health)
        self.nickname = nickname

    def known_as(self):
        return "{} the {}".format(self.name, self.nickname)
