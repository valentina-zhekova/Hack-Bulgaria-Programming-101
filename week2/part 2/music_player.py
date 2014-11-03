from song import Song
from playlist import Playlist
from music_crawler import MusicCrawler


# very unfinished
class MusicPlayer:

    def __init__(self):
        self.playlists = []

    def get_user_opinion(self):
        print("\nHello, you can use one of the following commands:"
              "\nall_playlists - to view the current playlists"
              "\nopen_playlist <name> - to show its content, artists, "
              "\nnew_playlist <name> <path>"
              "\nexit - to exit from the program")

        while True:
            reply = input("\nYour choice: ")
            if reply == 'exit':
                break
            # elif part ...
            else:
                print("There is no such option...")


def main():
    MusicPlayer().get_user_opinion()

if __name__ == '__main__':
    main()
