# tests/test_my_assistant.py
# Author: Fouzan Haider

from mock_model import MockModel
from my_assistant import MyAssistant
from my_tool import AppointmentLookup


class SilentModel:
    """A model that does not return an answer."""

    def reply(self, instructions, history):
        return None


def make_assistant(model=None):
    """Create an assistant with a sample appointment schedule."""

    appointments = {
        "Monday": ["9:00 am", "2:30 pm"],
        "Tuesday": ["10:00 am", "1:00 pm"],
    }

    appointment_tool = AppointmentLookup(appointments)

    if model is None:
        model = MockModel()

    return MyAssistant(
        "Fouzan",
        "You are a helpful appointment assistant.",
        appointment_tool,
        model,
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


def test_unknown_request_goes_to_model():
    bot = make_assistant()

    assert bot.respond("What is the parking situation?") == (
        "I'm not sure how to help with that. I can check an order or stock."
    )


def test_assistant_records_conversation_history():
    bot = make_assistant()

    bot.respond("hello")

    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"


def test_model_failure_gets_safe_fallback():
    bot = make_assistant(SilentModel())

    assert "try again" in bot.respond("What is the parking situation?")


def test_appointment_rule_works_without_model():
    bot = make_assistant(SilentModel())

    assert bot.respond("What times are available on Monday?") == (
        "Available appointments on Monday: 9:00 am, 2:30 pm."
    )
