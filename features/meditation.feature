Feature: Meditation App
  As a user
  I want to use a meditation app
  So that I can practice mindfulness

  Scenario: Start a timed meditation session
    Given the meditation app is open
    When I select a 10 minute meditation session
    And I start the session
    Then the app should display a timer counting down from 10 minutes

  Scenario: Complete a meditation session
    Given the meditation app is open
    When I select a 5 minute meditation session
    And I start the session
    And the timer reaches 0
    Then the app should play a gentle sound
    And the app should display a "Session Complete" message

  Scenario: Use guided meditation
    Given the meditation app is open
    When I select the "Guided Meditation" option
    Then the app should start playing an audio guide

  Scenario: Pause and resume a session
    Given the meditation app is open
    When I select a 15 minute meditation session
    And I start the session
    And I pause the session
    Then the timer should stop
    When I resume the session
    Then the timer should continue from where it left off

  Scenario: End session early
    Given the meditation app is open
    When I select a 20 minute meditation session
    And I start the session
    And I end the session early
    Then the app should return to the main menu
