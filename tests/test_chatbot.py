# tests/test_chatbot.py
# Author: Fouzan Haider

from chatbot import SupportChatbot
from echo_model import EchoModel
from mock_model import MockModel
from order_tool import OrderLookup
from stock_tool import StockLookup


class SilentModel:
    """A model that returns no answer for testing the safe fallback."""

    def reply(self, instructions, history):
        return None


def make_bot():
    """Create a chatbot with sample orders, stock, and a mock model."""

    orders = {
        "A100": "shipped",
        "A101": "processing",
    }

    stock = {
        "rain jacket": 12,
        "hoodie": 8,
    }

    order_tool = OrderLookup(orders)
    stock_tool = StockLookup(stock)
    model = MockModel()

    return SupportChatbot(
        "Sunny",
        "You are a friendly support assistant.",
        order_tool,
        stock_tool,
        model,
    )


def make_bot_with_silent_model():
    """Create a chatbot whose model does not return an answer."""

    orders = {
        "A100": "shipped",
        "A101": "processing",
    }

    stock = {
        "rain jacket": 12,
        "hoodie": 8,
    }

    order_tool = OrderLookup(orders)
    stock_tool = StockLookup(stock)
    model = SilentModel()

    return SupportChatbot(
        "Sunny",
        "You are a friendly support assistant.",
        order_tool,
        stock_tool,
        model,
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

    assert reply == "Hello! How can I help you today?"
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


def test_unknown_request_gets_a_model_reply():
    bot = make_bot()
    assert bot.respond("What is the weather?") == (
        "I'm not sure how to help with that. I can check an order or stock."
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


def test_other_messages_go_to_the_model():
    bot = make_bot()
    assert bot.respond("hello") == "Hello! How can I help you today?"


def test_safe_reply_when_the_model_has_no_answer():
    bot = make_bot_with_silent_model()
    assert "try again" in bot.respond("hello")


def test_order_rule_does_not_need_the_model():
    bot = make_bot_with_silent_model()
    assert bot.respond("Where is order A100?") == "Order A100 is shipped."


def test_handoff_rule_does_not_need_the_model():
    bot = make_bot_with_silent_model()
    assert bot.respond("I need to change my address") == (
        "I can't help with that here. I'm passing you to a human agent."
    )


def test_echo_model_repeats_user_message():
    bot = SupportChatbot(
        "Sunny",
        "You are a support assistant.",
        OrderLookup({"A100": "shipped"}),
        StockLookup({"rain jacket": 12}),
        EchoModel(),
    )

    assert bot.respond("good morning") == "You said: good morning"
