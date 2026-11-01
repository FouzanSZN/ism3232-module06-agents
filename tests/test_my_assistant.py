# tests/test_my_assistant.py
# Author: Fouzan Haider

from my_assistant import MyAssistant
from my_tool import AppointmentLookup


def make_assistant():
    """Create an assistant with a sample appointment schedule."""

    # Create a mock appointment schedule.
    appointments = {
        "Monday": ["9:00 am", "2:30 pm"],
        "Tuesday": ["10:00 am", "1:00 pm"],
    }

    # Create the appointment lookup tool.
    appointment_tool = AppointmentLookup(appointments)

    # Return an assistant connected to the appointment tool.
    return MyAssistant(
        "Fouzan",
        "You are a helpful appointment assistant.",
        appointment_tool,
    )


def test_available_appointments_use_the_tool():
    bot = make_assistant()

    assert bot.respond("What times are available on Monday?") == (
        "Available appointments on Monday: 9:00 am, 2:30 pm."
    )


def test_missing_day_asks_for_clarification():
    bot = make_assistant()

    assert bot.respond("What appointment times are available?") == (
        "Which day would you like to check?"
    )


def test_booking_request_goes_to_human():
    bot = make_assistant()

    assert bot.respond("I want to book an appointment") == (
        "I'll pass your booking request to our front desk so they can assist you."
    )


def test_unknown_request_gets_safe_reply():
    bot = make_assistant()

    assert bot.respond("What is the parking situation?") == (
        "I'm not sure how to help with that. I can check available appointment times."
    )


def test_assistant_records_conversation_history():
    bot = make_assistant()

    bot.respond("hello")

    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"
