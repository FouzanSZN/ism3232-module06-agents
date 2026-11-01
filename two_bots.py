# two_bots.py
# Author: Fouzan Haider

from chatbot import SupportChatbot
from order_tool import OrderLookup
from stock_tool import StockLookup

# Create one shared order database.
ORDERS = {
    "A100": "shipped",
    "A101": "processing",
    "A102": "delivered",
}

# Create one shared stock database.
STOCK = {
    "rain jacket": 12,
    "hoodie": 8,
}

# Create the lookup tools.
order_tool = OrderLookup(ORDERS)
stock_tool = StockLookup(STOCK)

# Create Sunny with cheerful and brief instructions.
sunny = SupportChatbot(
    "Sunny",
    "You are cheerful and brief.",
    order_tool,
    stock_tool,
)

# Create River with formal and detailed instructions.
river = SupportChatbot(
    "River",
    "You are formal and detailed.",
    order_tool,
    stock_tool,
)

# Send two messages to Sunny.
sunny.respond("hello")
sunny.respond("Where is order A100?")

# Send one message to River.
river.respond("hello")

# Display each chatbot's name and conversation history length.
print(sunny.name, len(sunny.history))
print(river.name, len(river.history))

# Display each chatbot's first reply.
print(sunny.history[1]["content"])
print(river.history[1]["content"])

# Display each chatbot's instructions.
print(sunny.instructions)
print(river.instructions)
