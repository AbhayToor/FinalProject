# ==============================================================================
# Author: Abhay Toor & Raafay Qureshi
# Title: MusyFilm
# Description: This program allows the users to choose between two options,
#              movie or music. Using APIs it generates the top 18 genres
#              from the two options. Then, using random module and the API
#              a random top track and artist from that genre is generated.
# ==============================================================================

import unittest
import project.music as music


class TestMusicGenre(unittest.TestCase):
    def test(self):
        genres = music.get_music_genre()
        self.assertIsInstance(genres, list)
        self.assertGreater(len(genres), 16)
        self.assertIsInstance(genres[0], str)


class TestSongs(unittest.TestCase):
    def test(self):
        genres = music.get_music_genre()
        for genre in genres:
            songs = music.get_songs(genre)
            self.assertIsInstance(songs, list)
            if len(songs) > 0:
                self.assertIsInstance(songs[0], tuple)
                self.assertIsInstance(songs[0][0], str)
                self.assertIsInstance(songs[0][1], str)

# Cannot test movie.py as testing requires user input


if __name__ == "__main__":
    unittest.main()
