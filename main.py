# main.py
# Author: Fouzan Haider

from chatbot import SupportChatbot
from ollama_model import OllamaModel
from order_tool import OrderLookup
from stock_tool import StockLookup

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """
You are Sunny, a support assistant for Bayside Outfitters.
Answer in one short sentence.
Store hours are 10 am to 7 pm every day.
Returns are accepted within 30 days with a receipt.
Shipping takes 3 to 5 business days.
Sale items cannot be returned.
Only state facts provided in these instructions.
If you do not know an answer, say so and offer a human agent.

ORDERS:
A100: shipped
A101: processing
A102: delivered

STOCK:
Rain jacket: 12
Day pack: 0
Trail hat: 5
"""

orders = {
    "A100": "shipped",
    "A101": "processing",
    "A102": "delivered",
}

stock = {
    "rain jacket": 12,
    "day pack": 0,
    "trail hat": 5,
}

order_tool = OrderLookup(orders)
stock_tool = StockLookup(stock)
model = OllamaModel(MODEL_NAME)

bot = SupportChatbot(
    "Sunny",
    INSTRUCTIONS,
    order_tool,
    stock_tool,
    model,
)

while True:
    user_message = input("You: ")

    if user_message.lower() in ["quit", "exit"]:
        print("Sunny: Goodbye!")
        break

    print("Sunny:", bot.respond(user_message))
