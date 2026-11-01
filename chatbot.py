# chatbot.py
# Author: Fouzan Haider

# These words identify requests that need a human agent.
HANDOFF_WORDS = ["address", "payment", "card"]


class SupportChatbot:
    """A mock support chatbot. Its replies come from simple rules, not from AI."""

    def __init__(self, name, instructions, order_tool, stock_tool):
        # Store the chatbot's name so it can identify itself.
        self.name = name

        # Store the instructions that describe the chatbot's role.
        self.instructions = instructions

        # Store the OrderLookup object so the chatbot can check orders.
        self.order_tool = order_tool

        # Store the stock lookup object for inventory questions.
        self.stock_tool = stock_tool

        # Create a separate conversation history for this chatbot.
        self.history = []

    def respond(self, user_message):
        # Record the message received from the user.
        self.history.append({"role": "user", "content": user_message})

        # Ask choose_reply to determine the appropriate response.
        reply = self.choose_reply(user_message)

        # Record the chatbot's response in the conversation history.
        self.history.append({"role": "assistant", "content": reply})

        # Return the response so it can be displayed.
        return reply

    def choose_reply(self, user_message):
        """Choose a reply with keyword rules. This is the mock part."""

        # Convert the message to lowercase for consistent keyword matching.
        text = user_message.lower()

        # Check for requests that must be handled by a human first.
        if self.needs_human(text):
            return "I can't help with that here. I'm passing you to a human agent."

        # If the message mentions an order, use the order lookup tool.
        if "order" in text:
            return self.order_reply(user_message)

        # Check inventory questions using the stock lookup tool.
        if "stock" in text:
            return self.stock_reply(user_message)

        # Respond with a greeting if the user says hello.
        if "hello" in text:
            return f"Hello! I'm {self.name}. I can check an order status for you."

        # Use a safe fallback when no rule matches.
        return "I'm not sure how to help with that. I can check an order status."

    def needs_human(self, text):
        """Return True if the message is about something a person must handle."""

        # Check each word in the handoff keyword list.
        for word in HANDOFF_WORDS:
            if word in text:
                return True

        # Return False when no handoff keyword is found.
        return False

    def order_reply(self, user_message):
        """Use the order tool to answer a question about an order."""

        # Search the customer's message for a known order ID.
        order_id = self.order_tool.find_order_id(user_message)

        # Ask the customer for an ID if no known ID was found.
        if order_id is None:
            return "Which order? Please send an order ID like A100."

        # Look up the status using the order tool.
        status = self.order_tool.find_status(order_id)

        # Return the order ID and its current status.
        return f"Order {order_id} is {status}."

    def count_user_messages(self):
        """Count how many messages were sent by users."""

        # Start the user message counter at zero.
        count = 0

        # Examine every message stored in the conversation history.
        for message in self.history:
            # Count only messages whose role is user.
            if message["role"] == "user":
                count += 1

        # Return the final number of user messages.
        return count

    def stock_reply(self, user_message):
        """Use the stock tool to answer inventory questions."""

        # Search the customer's message for a known product.
        product = self.stock_tool.find_product(user_message)

        # Ask which product if no known product was found.
        if product is None:
            return "Which product? Please tell me the product name."

        # Look up the available quantity for the product.
        count = self.stock_tool.count_for(product)

        # Return the available stock information.
        return f"We have {count} of the {product} in stock."
