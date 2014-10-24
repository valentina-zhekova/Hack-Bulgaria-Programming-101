from dungeon import Dungeon
from os import remove
import unittest


class DungeonTests(unittest.TestCase):

    def setUp(self):
        file = open("test_file.txt", "w")
        content = ["S.##......", "#.##..###.", "#.###.###.",
                   "#.....###.", "###.#####S"]
        file.write("\n".join(content))
        file.close()

        self.dungeon = Dungeon("test_file.txt")

    def test_init(self):
        self.assertEqual("test_file.txt", self.dungeon.filename)

    def test_print_map(self):
        self.assertTrue(self.dungeon.print_map())

    def test_free_spawning_points(self):  # help function
        self.assertFalse(self.dungeon.free_spawning_points("TTTTTTT"))
        self.assertTrue(self.dungeon.free_spawning_points("STTTTS"))

    def test_spawn_player_not_unique(self):

    def test_spawn_wrong_instance(self):

    def test_spawn_no_free_spawning()

    def tearDown(self):
        remove("test_file.txt")

if __name__ == '__main__':
    unittest.main()
