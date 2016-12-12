from random import randint
from prettytable import PrettyTable
import json
import os

class Song:

    def __init__(self, title, artist, album, time):
        self.title = title
        self.artist = artist
        self.album = album
        self.time = time

    def __str__(self):
        return "{0} - {1} from {2} - {3}".format(self.title, self.artist, self.album, self.time)

    def __eq__(self, ob1, ob2):
        if ob1.__hash__ == ob2.__hash__:
            return True
        else:
            return False

    def __hash__(self):
        return self.__str__

    def length(self, hours=False, minutes=False, seconds=False):
        arr = self.time.split(":")
        if hours:
            if len(arr) > 2:
                return int(arr[0])
            else:
                return 0
        if minutes:
            if len(arr) > 1:
                return int(arr[0])
            else:
                return 0
        if seconds:
            if len(arr) > 0:
                return int(arr[0]) * 60 + (arr[1]) * 60 + (arr[2])
            else:
                return 0
        if not hours and minutes and seconds:
            return self.time


class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.playlist = []
        self.current = 0

    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, song):
        self.playlist.remove(song)

    def add_songs(self, songs):
        for song in songs:
            self.playlist.append(song)

    def total_length(self):
        total = 0
        for song in self.playlist:
            total += song.legnth(minutes=True)

    def artists(self):
        my_dict = {}
        for i in self.playlist:
            if i.artist in my_dict:
                my_dict[i.artist] = my_dict[i.artist] + 1
            else:
                my_dict[i.artist] = 1

    def next_song(self):
        if self.shuffle:
            return self.playlist[randint(0, range(len(self.playlist)))]
        elif self.repeat:
            return self.playlist[self.current]
        else:
            self.playlist[self.current + 1]

    def pprint_playlist(self):
        t = PrettyTable(['Artist', 'Song', 'Length'])
        for i in self.playlist:
            t.add_row([i.artist, i.title, i.time])
        print(t)

    def save(self):
        my_list = []
        fileName = self.name.replace(" ", "-") + ".json"
        os.
        path = "/home/101/week7/music/playlists/" + fileName
        for i in self.playlist:
            my_list.append((i.artist, i.title))
        with open(path, 'w') as outfile:
            json.dump(my_list, outfile)

    @staticmethod
    def load(fileName):
        with open(fileName, 'r') as infile:
            data = json.load(infile)
        return data


class MusicCrawer:

    def __init__(self, path):
        self.path = path

def main():
    print(1)
    pl = Playlist("playlist")
    pl.add_song(Song(title="Odin", artist="Manowar", album="The Sons of Odin", time="3:44"))
    pl.add_song(Song(title="The sons of Odin", artist="Manowar", album="Odin", time="6:26"))
    pl.pprint_playlist()
    pl.save()
    # print(pl.load("playlist.json"))


# | Artist  | Song             | Length |
# | --------|------------------|--------|
# | Manowar | Odin             | 3:44   |
# | Manowar | The Sons of Odin | 6:26   |


if __name__ == "__main__":
    main()
