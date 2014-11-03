from song import Song
from song import SongEncoder
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
        file.write(json.dumps(self.__dict__, cls=SongEncoder))
        file.close()

    # help function for load
    def set_collection_from_json(self, json_collection):
        result = deepcopy(json_collection)
        result = list(map(lambda x: self.set_song_from_json(x), result))
        return result

    # help function for load
    def set_song_from_json(self, json_song):
        return Song(json_song['title'],
                    json_song['artist'],
                    json_song['album'],
                    json_song['rating'],
                    json_song['length'],
                    json_song['bitrate'])

    # This is very stupid implementation of load()
    # but I have problems with better ones
    @staticmethod
    def load(self):
        file = open("test_file", "r")
        content = file.read()
        file.close()
        json_data = json.loads(content)
        new_playlist = Playlist("")
        new_playlist.name = json_data['name']
        new_playlist.collection = new_playlist.set_collection_from_json(
            json_data['collection'])
        return new_playlist
