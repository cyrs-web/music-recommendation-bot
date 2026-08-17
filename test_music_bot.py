"""
Unit & Functional verification for music_bot.py
"""

import unittest
from music_bot import (
    SONGS,
    ALL_MOODS,
    ALL_GENRES,
    get_recommendations_by_mood,
    get_recommendations_by_genre,
    get_recommendations_by_artist,
    get_random_recommendations,
    format_song_list,
    parse_freeform_input,
)

class TestMusicBot(unittest.TestCase):
    
    def test_database_integrity(self):
        """Ensure all songs have required keys and non-empty values."""
        self.assertGreater(len(SONGS), 10, "Song database should have multiple songs")
        for song in SONGS:
            self.assertIn("title", song)
            self.assertIn("artist", song)
            self.assertIn("genre", song)
            self.assertIn("mood", song)
            self.assertTrue(song["title"])
            self.assertTrue(song["artist"])
            self.assertTrue(song["genre"])
            self.assertTrue(song["mood"])

    def test_mood_recommendation(self):
        """Test mood recommendation returns 3-5 songs when available."""
        recs = get_recommendations_by_mood("happy", count=4)
        self.assertGreaterEqual(len(recs), 3)
        self.assertLessEqual(len(recs), 5)
        for song in recs:
            self.assertEqual(song["mood"], "happy")

        # Unknown mood
        unknown = get_recommendations_by_mood("extraterrestrial")
        self.assertEqual(len(unknown), 0)

    def test_genre_recommendation(self):
        """Test genre recommendation returns matching songs."""
        recs = get_recommendations_by_genre("rock", count=3)
        self.assertGreaterEqual(len(recs), 2)
        for song in recs:
            self.assertIn("rock", song["genre"].lower())

    def test_artist_recommendation(self):
        """Test artist recommendation with partial and case-insensitive query."""
        recs = get_recommendations_by_artist("taylor")
        self.assertGreaterEqual(len(recs), 1)
        for song in recs:
            self.assertIn("taylor swift", song["artist"].lower())

    def test_random_recommendation(self):
        """Test random discovery picks."""
        recs = get_random_recommendations(count=4)
        self.assertEqual(len(recs), 4)

    def test_format_song_list(self):
        """Test song list formatting."""
        sample = [
            {"title": "Test Track", "artist": "Test Artist", "genre": "Pop", "mood": "happy"}
        ]
        formatted = format_song_list(sample)
        self.assertIn("Test Track", formatted)
        self.assertIn("Test Artist", formatted)
        self.assertIn("Pop", formatted)
        self.assertIn("Happy", formatted)

    def test_input_parser(self):
        """Test intent classification from freeform input."""
        self.assertEqual(parse_freeform_input("1"), ("mood", None))
        self.assertEqual(parse_freeform_input("by genre"), ("genre", None))
        self.assertEqual(parse_freeform_input("artist"), ("artist", None))
        self.assertEqual(parse_freeform_input("surprise me"), ("random", None))
        self.assertEqual(parse_freeform_input("exit"), ("exit", None))
        self.assertEqual(parse_freeform_input("quit"), ("exit", None))
        self.assertEqual(parse_freeform_input("help"), ("help", None))
        self.assertEqual(parse_freeform_input("happy"), ("direct_mood", "happy"))
        self.assertEqual(parse_freeform_input("lo-fi"), ("direct_genre", "lo-fi"))
        self.assertEqual(parse_freeform_input("adele"), ("direct_artist", "Adele"))
        self.assertEqual(parse_freeform_input("xyzunknown"), ("unknown", "xyzunknown"))


if __name__ == "__main__":
    unittest.main()
