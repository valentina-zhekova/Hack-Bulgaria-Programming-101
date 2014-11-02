from dungeon import Dungeon
from hero import Hero
from orc import Orc
from weapon import Weapon
from os import remove
from copy import deepcopy
import unittest


class DungeonTests(unittest.TestCase):

    def setUp(self):
        file = open("test_file.txt", "w")
        content = ["S...S", "", "Spoon 4 0.2", "RustyFork 6 0.7"]
        file.write("\n".join(content))
        file.close()

        self.dungeon = Dungeon("test_file.txt")

        self.hero = Hero("Don Quixote", 20, "The Common Sense")
        self.orc = Orc("Oplik", 20, 1.5)

    def test_init(self):
        self.assertEqual([['S', '.', '.', '.', 'S']], self.dungeon.dungeon)
        weapons = list(map(lambda x: x.type, deepcopy(self.dungeon.weapons)))
        self.assertEqual(["Spoon", "RustyFork"], weapons)
        self.assertEqual({}, self.dungeon.players)

    def test_load_map(self):
        self.assertEqual([['S', '.', '.', '.', 'S']],
                         self.dungeon.load_map("test_file.txt"))

    def test_is_map_row(self):
        self.assertTrue(self.dungeon.is_map_row("#..S..#"))
        self.assertFalse(self.dungeon.is_map_row("##Not.really.a.row"))

    def test_set_weapons(self):
        self.dungeon.weapons = []
        self.dungeon.set_weapons(["Knife 7 0.3"])
        self.assertEqual("Knife", self.dungeon.weapons[0].type)
        self.assertEqual(7.0, self.dungeon.weapons[0].damage)
        self.assertEqual(0.3, self.dungeon.weapons[0].critical_strike_percent)

    def test_print_map(self):
        self.assertTrue(self.dungeon.print_map())

    def test_free_spawning_points(self):  # help function
        self.dungeon.dungeon = [['T'], ['T']]
        self.assertFalse(self.dungeon.free_spawning_points())
        self.dungeon.dungeon = [['T'], ['S']]
        self.assertTrue(self.dungeon.free_spawning_points())

    def test_spawn(self):
        self.assertTrue(self.dungeon.spawn("player 1", self.hero))
        self.assertTrue(self.dungeon.spawn("player 2", self.orc))
        self.assertEqual({"player 1": (self.hero, 0, 0),
                          "player 2": (self.orc, 4, 0)}, self.dungeon.players)

    def test_spawn_player_not_unique_value_error(self):
        self.dungeon.spawn("player 1", self.hero)
        with self.assertRaises(ValueError):
            self.dungeon.spawn("player 1", self.hero)

    def test_spawn_no_spawning_points(self):
        self.dungeon.dungeon = [['.', '.']]
        self.assertFalse(self.dungeon.spawn("player 1", self.hero))

    def test_entity_kind(self):
        self.assertEqual('H', self.dungeon.entity_kind(self.hero))
        self.assertEqual('O', self.dungeon.entity_kind(self.orc))

    def test_entity_kind_wrong_instance(self):
        with self.assertRaises(ValueError):
            self.dungeon.entity_kind("tomatoe")

    def test_move(self):
        self.dungeon.dungeon = [['S', '.']]
        self.dungeon.spawn("player", self.hero)
        self.dungeon.move("player", "right")
        self.assertEqual([['.', 'H']], self.dungeon.dungeon)

    def test_move_obstacle(self):
        self.dungeon.dungeon = [['S', '#']]
        self.dungeon.spawn("player", self.hero)
        self.assertFalse(self.dungeon.move("player", "right"))

    def test_move_out_of_bounds(self):
        self.dungeon.spawn("player", self.hero)
        self.assertFalse(self.dungeon.move("player", "up"))

    def test_move_weapon_found(self):
        self.dungeon.dungeon = [['S', '.']]
        weapon = Weapon("Knife", 7, 0.3)
        self.dungeon.weapons = [weapon]
        self.dungeon.spawn_weapons()
        self.dungeon.spawn("player", self.hero)
        self.dungeon.move("player", "right")
        self.assertEqual(weapon, self.dungeon.players["player"][0].weapon)
        self.assertEqual([['.', 'H']], self.dungeon.dungeon)

    def test_move_start_fight(self):
        self.dungeon.spawn("player 1", self.hero)
        self.dungeon.spawn("player 2", self.orc)
        self.dungeon.spawn_weapons()
        self.dungeon.move("player 1", "right")
        self.dungeon.move("player 1", "right")
        self.dungeon.move("player 2", "left")
        self.dungeon.move("player 2", "left")
        self.assertTrue([['.', '.', 'H', '.', '.']] == self.dungeon.dungeon or
                        [['.', '.', 'O', '.', '.']] == self.dungeon.dungeon)

    def test_go_to_field(self):
        self.dungeon.dungeon = [['.', '.', '.'],
                                ['.', 'S', '.'],
                                ['.', '.', '.']]
        self.assertEqual((1, 0), self.dungeon.go_to_field(1, 1, "up"))
        self.assertEqual((1, 2), self.dungeon.go_to_field(1, 1, "down"))
        self.assertEqual((2, 1), self.dungeon.go_to_field(1, 1, "right"))
        self.assertEqual((0, 1), self.dungeon.go_to_field(1, 1, "left"))

    def test_go_to_field_out_of_bounds(self):
        self.assertFalse(self.dungeon.go_to_field(0, 0, "down"))

    def test_go_to_field_wrong_direction(self):
        with self.assertRaises(ValueError):
            self.dungeon.go_to_field(0, 0, "tomatoe")

    def test_entity_at_field(self):
        self.dungeon.spawn("player 1", self.hero)
        self.dungeon.spawn("player 2", self.orc)
        self.assertEqual(("player 2", self.orc),
                         self.dungeon.entity_at_field(4, 0))

    def test_spawn_weapons(self):
        self.dungeon.dungeon = [['S', '.']]
        weapon = Weapon("Knife", 7, 0.3)
        self.dungeon.weapons = [weapon]
        self.dungeon.spawn_weapons()
        self.assertEqual([['S', 'W']], self.dungeon.dungeon)
        self.assertEqual((weapon, 1, 0), self.dungeon.weapons[0])

    def test_generate_coordinates(self):
        coord = self.dungeon.generate_coordinates()
        self.assertEqual('.', self.dungeon.dungeon[coord[1]][coord[0]])

    def test_get_weapon(self):
        self.dungeon.dungeon = [['S', '.']]
        weapon = Weapon("Knife", 7, 0.3)
        self.dungeon.weapons = [weapon]
        self.dungeon.spawn_weapons()
        self.assertEqual(weapon, self.dungeon.get_weapon(1, 0))
        self.assertTrue((weapon, 1, 0) not in self.dungeon.weapons)

    def tearDown(self):
        remove("test_file.txt")

if __name__ == '__main__':
    unittest.main()
