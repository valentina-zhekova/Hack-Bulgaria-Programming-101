from entity import Entity
import unittest

# проверки в конструктура не е добре,
# правим нова функция и я викаме в конструктура
# assertRaises(ValueError) .....


class EntityTests(unittest.TestCase):

    def setUp(self):
        self.the_entity = Entity("Spiridon", 99.9)

    def test_entity_init(self):
        self.assertEqual("Spiridon", self.the_entity.name)
        self.assertEqual(99.9, self.the_entity.health)

    def test_get_health(self):
        self.assertEqual(99.9, self.the_entity.get_health())

    def test_is_alive(self):
        self.assertTrue(self.the_entity.is_alive())

    def test_is_alive_dead(self):
        self.the_entity.health = 0
        self.assertFalse(self.the_entity.is_alive())

    def test_take_damage(self):
        self.the_entity.take_damage(20)
        self.assertEqual(79.9, self.the_entity.get_health())

    def test_take_damage_more_than_health(self):
        self.the_entity.take_damage(129)
        self.assertEqual(0, self.the_entity.get_health())

    def test_take_healing_dead_entity(self):
        self.the_entity.health = 0
        self.assertFalse(self.the_entity.take_healing(20))

    def test_take_healing_is_possible(self):
        self.the_entity.take_damage(59.9)
        self.assertTrue(self.the_entity.take_healing(30))
        self.assertEqual(70, self.the_entity.get_health())

    def test_take_healing_more_than_max_health(self):
        # the maximum remains
        self.the_entity.take_damage(20)
        self.assertTrue(self.the_entity.take_healing(30))
        self.assertEqual(99.9, self.the_entity.get_health())

if __name__ == '__main__':
    unittest.main()
