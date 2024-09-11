import unittest
from meditation_app import MeditationApp

class TestMeditationApp(unittest.TestCase):
    def setUp(self):
        self.app = MeditationApp()

    def test_set_duration(self):
        self.app.set_duration(10)
        self.assertEqual(self.app.duration, 10)

    def test_start_session(self):
        self.app.start_session()
        self.assertTrue(self.app.is_session_active)

    def test_choose_background_sound(self):
        self.app.choose_background_sound("Ocean Waves")
        self.assertEqual(self.app.background_sound, "ocean waves")

    def test_is_playing_background_sound(self):
        self.assertFalse(self.app.is_playing_background_sound("Ocean Waves"))
        self.app.choose_background_sound("Ocean Waves")
        self.assertTrue(self.app.is_playing_background_sound("Ocean Waves"))
        self.assertTrue(self.app.is_playing_background_sound("ocean waves"))
        self.assertFalse(self.app.is_playing_background_sound("Rain"))

if __name__ == '__main__':
    unittest.main()
