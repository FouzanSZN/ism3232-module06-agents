# no_memory.py
# Author: Fouzan Haider

from ollama import chat

MODEL_NAME = "granite4.1:3b"

# First conversation: tell the model the customer's name.
first_response = chat(
    model=MODEL_NAME,
    messages=[
        {
            "role": "user",
            "content": "My name is Dana.",
        }
    ],
)

print("Sunny:", first_response.message.content)

# Second conversation: this is a separate call with no earlier history.
second_response = chat(
    model=MODEL_NAME,
    messages=[
        {
            "role": "user",
            "content": "What is my name?",
        }
    ],
)

print("Sunny:", second_response.message.content)
