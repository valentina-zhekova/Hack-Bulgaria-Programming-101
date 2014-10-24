from song import Song
from copy import deepcopy
from functools import reduce
import json


class Playlist:

    def __init__(self, name):
        self.name = name
        self.collection = []

    def add_song(self, song):
        if isinstance(song, Song):
            self.collection.append(song)
            return True
        else:
            raise ValueError("That's not a song!")

    def remove_song(self, song_name):
        self.collection = list(filter(lambda x: x.title != song_name,
                               self.collection))

    def total_length(self):
        if len(self.collection) != 0:
            collection = deepcopy(self.collection)
            return reduce(lambda x, y: x.length + y.length, collection)
        else:
            return 0

    def remove_disrated(self, rating):
        if (rating >= Song.MIN_RATING and
                rating <= Song.MAX_RATING):
            self.collection = list(filter(lambda x: x.rating >= rating,
                                   self.collection))
        else:
            raise ValueError("Rating should be between {} and {}!".format(
                Song.MIN_RATING, Song.MAX_RATING))

    def remove_bad_quality(self):
        self.collection = list(filter(lambda x: x.bitrate >
                               Song.LOW_BITTRATE_UPPER_LIMIT, self.collection))

    def show_artists(self):
        if len(self.collection) != 0:
            collection = deepcopy(self.collection)
            collection = list(map(lambda x: x.artist, collection))
            collection = set(collection)
            return list(collection)
        else:
            return []

    def str(self):
        lst = ""
        for song in self.collection:
            lst = lst + "%s %s - %02d:%02d\n" % (song.artist, song.title,
                                                 song.length // 60,
                                                 song.length % 60)
        return lst

    def save(self, file_name):
        file = open(file_name, "w")
        # to find a better way later!!!
        self.collection = list(map(lambda x: json.dumps(x.__dict__),
                               self.collection))
        file.write(json.dumps(self.__dict__))
        file.close()

    @staticmethod
    def load(self, file_name):
        file = open(file_name, "r")
        content = file.read()
        file.close()
        return Playlist(json.loads(content))


def main():

    playlist = Playlist("The Named Playlist")
    song1 = Song("Loosing My Insanity", "DIO", "Magica", 5, 333, 256)
    song2 = Song("Last In Line", "DIO", "Last In Line", 4, 222, 191)
    playlist.add_song(song1)
    playlist.add_song(song2)
    playlist.save("test_file")

    Playlist.load("test_file")

if __name__ == '__main__':
    main()


# pip -> package manager python
# sudo zyper install python3 pip
# sudo pip3 install mutagen
# pip3 freeze
# static load()!!!
