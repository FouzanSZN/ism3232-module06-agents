# tests/test_chatbot.py
# Author: Fouzan Haider

from chatbot import SupportChatbot
from order_tool import OrderLookup
from stock_tool import StockLookup


def make_bot():
    """Create a chatbot with sample orders and stock for testing."""

    # Create sample order and stock databases.
    orders = {
        "A100": "shipped",
        "A101": "processing",
    }

    stock = {
        "rain jacket": 12,
        "hoodie": 8,
    }

    # Create both lookup tools.
    order_tool = OrderLookup(orders)
    stock_tool = StockLookup(stock)

    # Give both tools to the chatbot.
    return SupportChatbot(
        "Sunny",
        "You are a friendly support assistant.",
        order_tool,
        stock_tool,
    )


def test_tool_finds_known_status():
    bot = make_bot()
    assert bot.order_tool.find_status("A100") == "shipped"


def test_tool_returns_none_for_unknown_order():
    bot = make_bot()
    assert bot.order_tool.find_status("A999") is None


def test_respond_records_both_messages():
    bot = make_bot()
    reply = bot.respond("hello")

    assert reply == "Hello! I'm Sunny. I can check an order status for you."
    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"


def test_order_question_uses_the_tool():
    bot = make_bot()
    assert bot.respond("Where is order A100?") == "Order A100 is shipped."


def test_order_question_without_an_id_asks_for_one():
    bot = make_bot()
    assert bot.respond("Where is my order?") == (
        "Which order? Please send an order ID like A100."
    )


def test_address_change_goes_to_a_human():
    bot = make_bot()
    assert bot.respond("Please change my shipping address") == (
        "I can't help with that here. I'm passing you to a human agent."
    )


def test_unknown_request_gets_a_safe_reply():
    bot = make_bot()
    assert bot.respond("What is the weather?") == (
        "I'm not sure how to help with that. I can check an order status."
    )


def test_two_chatbots_keep_separate_histories():
    bot1 = make_bot()
    bot2 = make_bot()

    bot1.respond("hello")

    assert len(bot1.history) == 2
    assert len(bot2.history) == 0


def test_count_user_messages():
    bot = make_bot()

    bot.respond("hello")
    bot.respond("Where is order A100?")

    assert bot.count_user_messages() == 2


def test_stock_question_uses_the_tool():
    bot = make_bot()

    assert bot.respond("Is the rain jacket in stock?") == (
        "We have 12 of the rain jacket in stock."
    )


def test_stock_question_without_product_asks_for_one():
    bot = make_bot()

    assert bot.respond("Do you have it in stock?") == (
        "Which product? Please tell me the product name."
    )
