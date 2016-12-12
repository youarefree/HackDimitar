import unittest
from music_library import Song
from music_library import Playlist

class testMusic(unittest.TestCase):

    def setUp(self):
        self.song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", time="3:44")
        self.song1 = Song(title="Odin", artist="Manowar", album="Odin", time="6:26")

    def test_str(self):
        self.assertEqual(self.song.__str__(),"Odin - Manowar from The Sons of Odin - 3:44")

    def test_eq(self):
        self.assertTrue(self.song.__eq__(self.song, self.song1))

    def test_length(self):
        self.assertEqual(self.song1.length(minutes=True), 6)


class testPlaylist(unittest.TestCase):

    def setUp(self):
        self.pl = Playlist("ssss")
        self.pl.add_song(Song(title="Odin", artist="Manowar", album="The Sons of Odin", time="3:44"))
        self.pl.add_song(Song(title="Odin", artist="Manowar", album="Odin", time="6:26"))

    def test_next_song(self):
        self.assertEqual(self.pl.next_song(), "")

if __name__ == '__main__':
    unittest.main()
