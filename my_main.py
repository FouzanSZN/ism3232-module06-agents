# my_main.py
# Author: Fouzan Haider

from my_assistant import MyAssistant
from my_tool import AppointmentLookup
from ollama_model import OllamaModel

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """
You are Fouzan's helpful appointment assistant.
Answer in one short sentence.
The office is open Monday through Friday.
Appointments can be checked using the appointment schedule.
If you do not know an answer, say so instead of guessing.
Offer to connect the customer with the front desk when needed.
"""

APPOINTMENTS = {
    "Monday": ["9:00 am", "2:30 pm"],
    "Tuesday": ["10:00 am", "1:00 pm"],
    "Wednesday": ["9:30 am", "3:00 pm"],
    "Thursday": ["11:00 am", "2:00 pm"],
    "Friday": ["10:30 am", "1:30 pm"],
}

appointment_tool = AppointmentLookup(APPOINTMENTS)
model = OllamaModel(MODEL_NAME)

bot = MyAssistant(
    "Fouzan",
    INSTRUCTIONS,
    appointment_tool,
    model,
)

print("Welcome! Type a message, or type quit to stop.")

user_message = input("You: ")

while user_message.lower() != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
