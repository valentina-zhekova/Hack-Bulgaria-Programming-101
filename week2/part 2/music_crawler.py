from mutagen.mp3 import MP3
from song import Song
from playlist import Playlist
from os import listdir


class MusicCrawler:
    KNOWN_FORMATS = ('.mp3',)
    DEFAULT_TITLE = 'Unknown Title'
    DEFAULT_ARTIST = 'Unknown Artist'
    DEFAULT_ALBUM = 'Unknown Album'
    DEFAULT_RATING = 0

    AUDIO_TITLE_TAG = 'TIT2'
    AUDIO_ARTIST_TAG = 'TPE1'
    AUDIO_ALBUM_TAG = 'TALB'

    def __init__(self, path):
        self.__path = path

    def _get_audio_files(self, folder):
        files = listdir(self.__path)
        return filter(lambda filename: filename.endswith(self.KNOWN_FORMATS),
                      files)

    def _get_audio_tags(self, audio_obj):
        tags_dict = {}
        tags_dict['title'] = audio_obj.get(self.AUDIO_TITLE_TAG,
                                           self.DEFAULT_TITLE)
        tags_dict['arist'] = audio_obj.get(self.AUDIO_ARTIST_TAG,
                                           self.DEFAULT_ARTIST)
        tags_dict['album'] = audio_obj.get(self.AUDIO_ALBUM_TAG,
                                           self.DEFAULT_ALBUM)
        return tags_dict

    def _get_audio_length(self, audio_obj):
        return int(audio_obj.info.length)

    def _get_audio_bitrate(self, audio_obj):
        return audio_obj.info.bitrate

    def _create_song(self, audio_obj):
        song_tags = self._get_audio_tags(audio_obj)
        song_length = self._get_audio_length(audio_obj)
        song_bitrate = self._get_audio_bitrate(audio_obj)

        song = Song(song_tags['title'], song_tags['artist'],
                    song_tags['album'], song_length, song_bitrate)
        return song

    def generate_playlist(self, playlist_name):
        output_playlist = Playlist(playlist_name)
        files = self._get_audio_files(self.__path)
        for filename in files:
            audio_obj = MP3(filename)
            song = self._create_song(audio_obj)
            output_playlist.add(song)
        return output_playlist
