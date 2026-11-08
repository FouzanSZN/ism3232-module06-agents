# first_chat.py
# Author: Fouzan Haider

from ollama import chat

MODEL_NAME = "granite4.1:3b"

# Give the model its role and basic instructions.
messages = [
    {
        "role": "system",
        "content": (
            "You are Sunny, a friendly support assistant for Bayside Outfitters."
        ),
    },
    {
        "role": "user",
        "content": "What time does your store close?",
    },
]

# Send the conversation to the local Ollama model.
response = chat(
    model=MODEL_NAME,
    messages=messages,
)

# Display the model's response.
print("Sunny:", response.message.content)
