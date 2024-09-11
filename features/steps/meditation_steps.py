from behave import given, when, then
from meditation_app import MeditationApp

# This is the correct location for our step definitions

@given('the meditation app is open')
def step_impl(context):
    context.app = MeditationApp()

@when('I select a {duration} minute meditation session')
def step_impl(context, duration):
    context.app.set_duration(int(duration))

@when('I start the session')
def step_impl(context):
    context.app.start_session()

@then('the app should display a timer counting down from {duration} minutes')
def step_impl(context, duration):
    assert context.app.get_remaining_time() == int(duration) * 60

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
