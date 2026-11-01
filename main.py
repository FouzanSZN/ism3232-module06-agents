# main.py
# Author: Fouzan Haider

from chatbot import SupportChatbot
from order_tool import OrderLookup
from stock_tool import StockLookup

# Create a sample order database.
ORDERS = {
    "A100": "shipped",
    "A101": "processing",
    "A102": "delivered",
}

# Create a sample stock database.
STOCK = {
    "rain jacket": 12,
    "hoodie": 8,
}

# Create the order lookup tool using the sample database.
order_tool = OrderLookup(ORDERS)
# Create the order lookup tool using the sample database.
order_tool = OrderLookup(ORDERS)

# ADD THIS HERE
stock_tool = StockLookup(STOCK)

# Create the chatbot and give it the order lookup tool.
bot = SupportChatbot(
    "Sunny",
    "You are a friendly support assistant for Bayside Outfitters.",
    order_tool,
    stock_tool,
)


# Display instructions before starting the conversation.
print("Type a message, or type quit to stop.")

# Ask for the first user message.
user_message = input("You: ")

# Continue until the user types quit.
while user_message != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

# Display the total number of messages recorded.
print(f"Messages in this conversation: {len(bot.history)}")
