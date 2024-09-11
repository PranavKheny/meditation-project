import time

class MeditationApp:
    def __init__(self):
        self.duration = 0
        self.remaining_time = 0
        self.is_session_active = False
        self.is_paused = False
        self.total_meditation_time = 0
        self.streak_count = 0
        self.background_sound = None
        self.daily_reminder_time = None
        self.audio_guide_playing = False
        self.end_sound_playing = False

    def set_duration(self, duration):
        self.duration = duration
        self.remaining_time = duration * 60  # Convert minutes to seconds

    def start_session(self):
        self.is_session_active = True
        self.end_sound_playing = False

    def get_remaining_time(self):
        return self.remaining_time

    def simulate_session_completion(self):
        self.is_session_active = False
        self.total_meditation_time += self.duration
        self.streak_count += 1
        self.end_sound_playing = True

    def is_end_sound_playing(self):
        return self.end_sound_playing

    def get_session_status(self):
        return "Complete" if not self.is_session_active else "In Progress"

    def select_guided_meditation(self):
        self.audio_guide_playing = True

    def is_audio_guide_playing(self):
        return self.audio_guide_playing

    def pause_session(self):
        self.is_paused = True

    def is_session_paused(self):
        return self.is_paused

    def resume_session(self):
        self.is_paused = False

    def end_session(self):
        self.is_session_active = False
        self.remaining_time = 0

    def is_on_main_menu(self):
        return not self.is_session_active

    def select_background_sounds(self):
        pass

    def choose_background_sound(self, sound):
        self.background_sound = sound.lower()

    def is_playing_background_sound(self, sound):
        return self.background_sound == sound.lower()

    def get_streak_count(self):
        return self.streak_count

    def open_settings(self):
        pass

    def set_daily_reminder(self, time):
        self.daily_reminder_time = time

    def get_daily_reminder_time(self):
        return self.daily_reminder_time

    def select_custom_duration(self):
        pass

    def set_custom_duration(self, duration):
        self.set_duration(duration)
