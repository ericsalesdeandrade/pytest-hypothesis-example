import pytest
from src.shopping_cart import ShoppingCart, Item


@pytest.fixture()
def cart():
    return ShoppingCart()


# Define Items
apple = Item.APPLE
orange = Item.ORANGE
gum = Item.GUM
soda = Item.SODA
water = Item.WATER
coffee = Item.COFFEE
tea = Item.TEA


# Example Based Testing
def test_add_item(cart):
    cart.add_item(apple, 1.00)
    assert cart.items == {"APPLE": 1.00}


def test_remove_item(cart):
    cart.add_item(orange, 1.00)
    cart.add_item(tea, 3.00)
    cart.add_item(coffee, 3.00)
    cart.remove_item(orange)
    assert cart.items == {"TEA": 3.00, "COFFEE": 3.00}


def test_view_cart(cart):
    cart.add_item(water, 1.00)
    cart.add_item(gum, 2.00)
    cart.add_item(soda, 2.50)
    cart.view_cart()
    assert cart.items == {"WATER": 1.00, "GUM": 2.00, "SODA": 2.50}


def test_total(cart):
    cart.add_item(orange, 1.00)
    cart.add_item(apple, 2.00)
    assert cart.total() == 3.00


def test_clear_cart(cart):
    cart.add_item(apple, 1.00)
    cart.add_item(soda, 2.00)
    cart.add_item(water, 1.00)
    cart.clear_cart()
    assert cart.items == {}


