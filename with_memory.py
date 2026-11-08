# with_memory.py
# Author: Fouzan Haider

from ollama import chat

MODEL_NAME = "granite4.1:3b"

# Keep all messages in one conversation history.
messages = [
    {
        "role": "system",
        "content": "You are Sunny, a friendly support assistant.",
    }
]

# First user message.
messages.append(
    {
        "role": "user",
        "content": "My name is Dana.",
    }
)

# Send the complete conversation history.
response = chat(
    model=MODEL_NAME,
    messages=messages,
)

# Save the assistant's response in the history.
messages.append(
    {
        "role": "assistant",
        "content": response.message.content,
    }
)

print("Sunny:", response.message.content)

# Second user message.
messages.append(
    {
        "role": "user",
        "content": "What is my name?",
    }
)

# Send the complete history again.
response = chat(
    model=MODEL_NAME,
    messages=messages,
)

# Save and display the second response.
messages.append(
    {
        "role": "assistant",
        "content": response.message.content,
    }
)

print("Sunny:", response.message.content)
