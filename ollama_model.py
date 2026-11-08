# ollama_model.py
# Author: Fouzan Haider

from ollama import ResponseError, chat


class OllamaModel:
    """Connect the chatbot to a local Ollama model."""

    def __init__(self, model_name):
        # Store the name of the local model.
        self.model_name = model_name

    def reply(self, instructions, history):
        # Start the conversation with the system instructions.
        messages = [
            {
                "role": "system",
                "content": instructions,
            }
        ]

        # Add the complete conversation history.
        messages.extend(history)

        try:
            # Send the messages to the local Ollama model.
            response = chat(
                model=self.model_name,
                messages=messages,
            )
        except ConnectionError:
            # Return None if Ollama is unavailable.
            return None
        except ResponseError:
            # Return None if Ollama reports a model error.
            return None

        # Return the model's text response.
        return response.message.content
