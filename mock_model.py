# mock_model.py
# Author: Fouzan Haider


class MockModel:
    """A simple model used to test chatbot responses without Ollama."""

    def reply(self, instructions, history):
        # Get the most recent message from the conversation.
        last_message = history[-1]["content"].lower()

        # Return a fixed greeting when the user says hello.
        if "hello" in last_message:
            return "Hello! How can I help you today?"

        # Return a default response for other messages.
        return "I'm not sure how to help with that. I can check an order or stock."
