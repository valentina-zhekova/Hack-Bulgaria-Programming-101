import json


class Song:

    MAX_RATING = 5
    MIN_RATING = 0
    LOW_BITTRATE_UPPER_LIMIT = 200

    def __init__(self, title, artist, album, rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate

    def rate(self, rating):
        if (type(rating) == int and
                rating >= self.MIN_RATING and rating <= self.MAX_RATING):
            self.rating = rating
        else:
            error_message = ("Rating should be between {} and {}!")
            raise ValueError(error_message.format(
                self.MIN_RATING, self.MAX_RATING))


class SongEncoder(json.JSONEncoder):

    def default(self, o):
        return o.__dict__
