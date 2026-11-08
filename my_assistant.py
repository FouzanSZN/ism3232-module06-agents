# my_assistant.py
# Author: Fouzan Haider


class MyAssistant:
    """An appointment assistant that uses rules, tools, and a model."""

    def __init__(self, name, instructions, appointment_tool, model):
        self.name = name
        self.instructions = instructions
        self.appointment_tool = appointment_tool
        self.model = model
        self.history = []

    def respond(self, user_message):
        """Record the conversation and return the assistant's reply."""

        self.history.append({"role": "user", "content": user_message})

        reply = self.choose_reply(user_message)

        self.history.append({"role": "assistant", "content": reply})

        return reply

    def choose_reply(self, user_message):
        """Apply important rules before asking the model."""

        text = user_message.lower()

        # Booking requests must go to the human front desk.
        if "book" in text or "booking" in text or "schedule" in text:
            return (
                "I'll pass your booking request to our front desk "
                "so they can assist you."
            )

        # Handle greetings directly.
        if "hello" in text or "hi" in text:
            return f"Hello! I'm {self.name}. I can help you check appointment availability."

        # Appointment questions must use the real lookup tool.
        if "available" in text or "appointment" in text or "times" in text:
            return self.appointment_reply(user_message)

        # Send other questions to the model.
        return self.model_reply()

    def model_reply(self):
        """Ask the model and provide a safe fallback if it fails."""

        reply = self.model.reply(self.instructions, self.history)

        if reply is None:
            return "Sorry, I can't answer that right now. Please try again in a moment."

        return reply

    def appointment_reply(self, user_message):
        """Use the appointment tool to check available times."""

        day = self.appointment_tool.find_day(user_message)

        if day is None:
            return "Which day would you like to check?"

        times = self.appointment_tool.available_times(day)

        if not times:
            return f"Sorry, there are no available appointments on {day}."

        return f"Available appointments on {day}: {', '.join(times)}."
