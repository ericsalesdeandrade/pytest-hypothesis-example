import random
from enum import Enum, auto


class Item(Enum):
    """Item type"""

    APPLE = auto()
    ORANGE = auto()
    BANANA = auto()
    CHOCOLATE = auto()
    CANDY = auto()
    GUM = auto()
    COFFEE = auto()
    TEA = auto()
    SODA = auto()
    WATER = auto()

    def __str__(self):
        return self.name.upper()


class ShoppingCart:
    def __init__(self):
        """
        Creates a shopping cart object with an empty dictionary of items
        """
        self.items = {}

    def add_item(self, item: Item, price: int | float) -> None:
        """
        Adds an item to the shopping cart
        :param item: Item to add
        :param price: Price of the item
        :return: None
        """
        if item in self.items:
            self.items[item.name] += price
        else:
            self.items[item.name] = price

    def remove_item(self, item: Item) -> None:
        """
        Removes an item from the shopping cart
        :param item: Item to remove
        :return: None
        """
        if item.name in self.items:
            del self.items[item.name]

    def view_cart(self) -> None:
        """
        Prints the contents of the shopping cart
        :return: None
        """
        print("Shopping Cart:")
        for item, price in self.items.items():
            print("- {}: ${}".format(item, price))

    def total(self) -> float:
        """
        Calculates the total price of the items in the shopping cart
        :return: Total price
        """
        return sum(self.items.values())

    def clear_cart(self) -> None:
        """
        Clears the shopping cart
        :return: None
        """
        self.items = {}

    def checkout(self) -> None:
        """
        Checks out the shopping cart
        :return: None
        """
        print("Checking out...")
        print("Your total is: ${}".format(self.total()))
        print("Thank you for shopping with us!")
        self.clear_cart()


if __name__ == "__main__":

    # Initialise Cart
    cart = ShoppingCart()

    # Define Items
    banana = Item.BANANA
    orange = Item.ORANGE
    apple = Item.APPLE
    coffee = Item.COFFEE

    # Add Items to Cart
    cart.add_item(item=banana, price=2)
    cart.add_item(item=orange, price=5)
    cart.add_item(item=apple, price=3)
    cart.add_item(item=coffee, price=4)

    # View Cart
    cart.view_cart()
    cart.checkout()
