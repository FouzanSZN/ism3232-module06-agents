# two_bots.py
# Author: Fouzan Haider

from chatbot import SupportChatbot
from mock_model import MockModel
from order_tool import OrderLookup
from stock_tool import StockLookup

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


sunny = SupportChatbot(
    "Sunny",
    "You are Sunny, a friendly support assistant for Bayside Outfitters.",
    OrderLookup(orders),
    StockLookup(stock),
    MockModel(),
)

river = SupportChatbot(
    "River",
    "You are River, a helpful support assistant for Bayside Outfitters.",
    OrderLookup(orders),
    StockLookup(stock),
    MockModel(),
)


print("Sunny:", sunny.respond("hello"))
print("River:", river.respond("hello"))

print("Sunny history:", sunny.history)
print("River history:", river.history)
