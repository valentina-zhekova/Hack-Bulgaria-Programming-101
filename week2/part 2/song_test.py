from song import Song
import unittest


class SongTests(unittest.TestCase):

    def setUp(self):
        self.song = Song("Drunken Sailor", "Irish Rovers",
                         "Some Album", 5, 213, 42)

    def test_init(self):
        self.assertEqual("Drunken Sailor", self.song.title)
        self.assertEqual("Irish Rovers", self.song.artist)
        self.assertEqual("Some Album", self.song.album)
        self.assertEqual(5, self.song.rating)
        self.assertEqual(213, self.song.length)
        self.assertEqual(42, self.song.bitrate)

    def test_rate(self):
        self.song.rate(5)
        self.assertEqual(5, self.song.rating)

    def test_rate_value_error(self):
        with self.assertRaises(ValueError):
            self.song.rate(7)

if __name__ == '__main__':
    unittest.main()
