from entity import Entity
from weapon import Weapon
from random import randint
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

    def test_has_weapon_false(self):
        self.assertFalse(self.the_entity.has_weapon())

    def test_has_weapon_true(self):
        self.the_entity.weapon = Weapon("daggers", 16, 0.5)
        self.assertTrue(self.the_entity.has_weapon())

    def test_equip_weapon(self):
        weapon1 = Weapon("daggers", 16, 0.5)
        weapon2 = Weapon("spoon", 2, 0.7)
        self.the_entity.weapon = weapon1
        self.the_entity.equip_weapon(weapon2)
        self.assertNotEqual(weapon1, self.the_entity.weapon)
        self.assertEqual(weapon2, self.the_entity.weapon)

    def test_equip_weapon_value_error(self):
        with self.assertRaises(ValueError):
            self.the_entity.equip_weapon("pancake")

    def test_attack_no_weapon(self):
        self.assertEqual(0, self.the_entity.attack())

# fix this test later; self.assertIn
    def test_attack(self):
        weapon = Weapon("spoon", 2, 0.7)
        self.the_entity.equip_weapon(weapon)
        critical = False
        normal = False
        for i in range(0, 1000):
            critical = critical or (4 == self.the_entity.attack())
            normal = normal or (2 == self.the_entity.attack())
        self.assertTrue(critical)
        self.assertTrue(normal)
# buffer before hard disk
# file -> write -> close file -> read file

if __name__ == '__main__':
    unittest.main()
