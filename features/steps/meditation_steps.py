from behave import given, when, then
from meditation_app import MeditationApp

@given('the meditation app is open')
def step_impl(context):
    context.app = MeditationApp()

@when('I select a {duration:d} minute meditation session')
def step_impl(context, duration):
    context.app.set_duration(duration)

@when('I start the session')
def step_impl(context):
    context.app.start_session()

@then('the app should display a timer counting down from {duration:d} minutes')
def step_impl(context, duration):
    assert context.app.get_remaining_time() == duration * 60

@when('the timer reaches 0')
def step_impl(context):
    context.app.simulate_session_completion()

@then('the app should play a gentle sound')
def step_impl(context):
    assert context.app.is_end_sound_playing()

@then('the app should display a "Session Complete" message')
def step_impl(context):
    assert context.app.get_session_status() == "Complete"

@when('I select the "Guided Meditation" option')
def step_impl(context):
    context.app.select_guided_meditation()

@then('the app should start playing an audio guide')
def step_impl(context):
    assert context.app.is_audio_guide_playing()

@when('I pause the session')
def step_impl(context):
    context.app.pause_session()

@then('the timer should stop')
def step_impl(context):
    assert context.app.is_session_paused()

@when('I resume the session')
def step_impl(context):
    context.app.resume_session()

@then('the timer should continue from where it left off')
def step_impl(context):
    assert not context.app.is_session_paused()
    assert context.app.get_remaining_time() > 0

@when('I end the session early')
def step_impl(context):
    context.app.end_session()

@then('the app should return to the main menu')
def step_impl(context):
    assert context.app.is_on_main_menu()

@when('I select "Background Sounds" from the menu')
def step_impl(context):
    context.app.select_background_sounds()

@when('I choose "{sound}"')
def step_impl(context, sound):
    context.app.choose_background_sound(sound)

@then('the app should play {sound} sounds')
def step_impl(context, sound):
    assert context.app.is_playing_background_sound(sound)

@when('I complete a {duration:d} minute meditation session')
def step_impl(context, duration):
    context.app.set_duration(duration)
    context.app.start_session()
    context.app.simulate_session_completion()

@then('the app should update my total meditation time')
def step_impl(context):
    assert context.app.total_meditation_time > 0

@then('the app should display a streak count')
def step_impl(context):
    assert context.app.get_streak_count() >= 1

@when('I go to "Settings"')
def step_impl(context):
    context.app.open_settings()

@when('I set a daily reminder for {time}')
def step_impl(context, time):
    context.app.set_daily_reminder(time)

@then('the app should send a notification at {time} every day')
def step_impl(context, time):
    assert context.app.get_daily_reminder_time() == time

@when('I select "Custom Duration"')
def step_impl(context):
    context.app.select_custom_duration()

@when('I set the duration to {duration:d} minutes')
def step_impl(context, duration):
    context.app.set_custom_duration(duration)
