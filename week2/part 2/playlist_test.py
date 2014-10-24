from playlist import Playlist
from song import Song
from copy import deepcopy
import unittest


class PlaylistTests(unittest.TestCase):

    def setUp(self):
        self.playlist = Playlist("The Named Playlist")
        self.song1 = Song("Loosing My Insanity", "DIO", "Magica", 5, 333, 256)
        self.song2 = Song("Last In Line", "DIO", "Last In Line", 4, 222, 191)

    def test_init(self):
        self.assertEqual("The Named Playlist", self.playlist.name)
        self.assertEqual([], self.playlist.collection)

    def test_add_song(self):
        self.assertTrue(self.playlist.add_song(self.song1))

    def test_add_song_value_error(self):
        with self.assertRaises(ValueError):
            self.playlist.add_song("tomatoe")

    def test_remove_song(self):
        self.playlist.add_song(self.song1)
        self.playlist.add_song(self.song2)
        self.playlist.remove_song("Last In Line")
        lst = deepcopy(self.playlist.collection)
        lst = list(map(lambda x: x.title, lst))
        self.assertEqual(0, lst.count("Last In Line"))

    def test_total_length(self):
        self.playlist.add_song(self.song1)
        self.playlist.add_song(self.song2)
        self.assertEqual(555, self.playlist.total_length())

    def test_total_length_empty_collection(self):
        self.assertEqual(0, self.playlist.total_length())

    def test_remove_disrated(self):
        self.playlist.add_song(self.song1)
        self.playlist.add_song(self.song2)
        self.playlist.remove_disrated(5)
        lst = deepcopy(self.playlist.collection)
        lst = list(map(lambda x: x.rating, lst))
        self.assertEqual(0, lst.count(4))

    def test_remove_disrated_value_error(self):
        with self.assertRaises(ValueError):
            self.playlist.remove_disrated(8)

    def test_remove_bad_quality(self):
        self.playlist.add_song(self.song1)
        self.playlist.add_song(self.song2)
        self.playlist.remove_bad_quality()
        lst = deepcopy(self.playlist.collection)
        lst = list(map(lambda x: x.bitrate, lst))
        self.assertEqual(0, lst.count(191))

    def test_show_artists(self):
        self.playlist.add_song(self.song1)
        self.playlist.add_song(self.song2)
        self.assertEqual(["DIO"], self.playlist.show_artists())

    def test_show_artists_empty_collection(self):
        self.assertEqual([], self.playlist.show_artists())

    def test_str(self):
        self.playlist.add_song(self.song1)
        self.playlist.add_song(self.song2)
        self.assertEqual("DIO Loosing My Insanity - 05:33\n" +
                         "DIO Last In Line - 03:42\n", self.playlist.str())

if __name__ == '__main__':
    unittest.main()
