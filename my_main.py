# my_main.py
# Author: Fouzan Haider

from my_assistant import MyAssistant
from my_tool import AppointmentLookup

# Create a mock appointment schedule.
APPOINTMENTS = {
    "Monday": ["9:00 am", "2:30 pm"],
    "Tuesday": ["10:00 am", "1:00 pm"],
    "Wednesday": ["9:30 am", "3:00 pm"],
    "Thursday": ["11:00 am", "2:00 pm"],
    "Friday": ["10:30 am", "1:30 pm"],
}

# Create the appointment lookup tool.
appointment_tool = AppointmentLookup(APPOINTMENTS)

# Create Fouzan's appointment assistant.
bot = MyAssistant(
    "Fouzan",
    "You are a helpful appointment assistant.",
    appointment_tool,
)

# Display instructions before starting the conversation.
print("Welcome! Type a message, or type quit to stop.")

# Ask for the first customer message.
user_message = input("You: ")

# Continue until the customer types quit.
while user_message.lower() != "quit":
    # Display Fouzan's response.
    print(f"{bot.name}: {bot.respond(user_message)}")

    # Ask for the next customer message.
    user_message = input("You: ")

# Display the total number of messages recorded.
print(f"Messages in this conversation: {len(bot.history)}")
