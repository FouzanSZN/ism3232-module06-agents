# echo_model.py
# Author: Fouzan Haider


class EchoModel:
    """Repeat the user's most recent message."""

    def reply(self, instructions, history):
        # Get the most recent message from the conversation.
        last_message = history[-1]["content"]

        # Return the message with a short introduction.
        return "You said: " + last_message
