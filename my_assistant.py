# my_assistant.py
# Author: Fouzan Haider


class MyAssistant:
    """A mock appointment assistant that uses simple rules and a lookup tool."""

    def __init__(self, name, instructions, appointment_tool):
        # Store the assistant's name.
        self.name = name

        # Store the instructions describing the assistant's role.
        self.instructions = instructions

        # Store the appointment lookup tool.
        self.appointment_tool = appointment_tool

        # Create a separate conversation history.
        self.history = []

    def respond(self, user_message):
        """Record the user's message and return the assistant's reply."""

        # Record the customer's message in the conversation history.
        self.history.append({"role": "user", "content": user_message})

        # Choose a reply based on the customer's message.
        reply = self.choose_reply(user_message)

        # Record the assistant's reply.
        self.history.append({"role": "assistant", "content": reply})

        # Return the reply.
        return reply

    def choose_reply(self, user_message):
        """Choose a response using simple keyword rules."""

        # Convert the message to lowercase for matching.
        text = user_message.lower()

        # Send appointment booking requests to a human.
        if "book" in text or "booking" in text or "schedule" in text:
            return (
                "I'll pass your booking request to our front desk "
                "so they can assist you."
            )

        # Respond to greetings.
        if "hello" in text or "hi" in text:
            return f"Hello! I'm {self.name}. I can help you check appointment availability."

        # Check questions about available appointment times.
        if "available" in text or "appointment" in text or "times" in text:
            return self.appointment_reply(user_message)

        # Give a safe response to questions the assistant cannot handle.
        return (
            "I'm not sure how to help with that. "
            "I can check available appointment times."
        )

    def appointment_reply(self, user_message):
        """Use the appointment tool to check available times."""

        # Find the weekday mentioned in the customer's message.
        day = self.appointment_tool.find_day(user_message)

        # Ask which day the customer wants if none was identified.
        if day is None:
            return "Which day would you like to check?"

        # Look up available appointment times for that day.
        times = self.appointment_tool.available_times(day)

        # Handle days without available appointments.
        if not times:
            return f"Sorry, there are no available appointments on {day}."

        # Return the available appointment times.
        return f"Available appointments on {day}: {', '.join(times)}."
