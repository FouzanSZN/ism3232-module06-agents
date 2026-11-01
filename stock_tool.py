# stock_tool.py
# Author: Fouzan Haider


class StockLookup:
    """A tool that stores product stock counts."""

    def __init__(self, stock):
        # Store the product inventory dictionary.
        self.stock = stock

    def find_product(self, text):
        """Find the first known product mentioned in the message."""

        # Convert the message to lowercase for matching.
        text = text.lower()

        # Check each product in the inventory.
        for product in self.stock:
            # Return the product if it appears in the message.
            if product.lower() in text:
                return product

        # Return None when no product is found.
        return None

    def count_for(self, product):
        """Return the available stock count for a product."""

        # Check whether the product exists in inventory.
        if product in self.stock:
            return self.stock[product]

        # Return None for an unknown product.
        return None
