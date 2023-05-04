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
    cart.add_item(orange, 1.00)
    cart.add_item(gum, 2.00)
    cart.add_item(soda, 2.50)
    assert cart.items == {'APPLE': {'price': 1.0, 'quantity': 1}, 'ORANGE': {'price': 1.0, 'quantity': 1},
                          'GUM': {'price': 2.0, 'quantity': 1}, 'SODA': {'price': 2.5, 'quantity': 1}}
    #


def test_remove_item(cart):
    cart.add_item(orange, 1.00)
    cart.add_item(tea, 3.00)
    cart.add_item(coffee, 3.00)
    cart.remove_item(orange)
    assert cart.items == {'TEA': {'price': 3.0, 'quantity': 1}, 'COFFEE': {'price': 3.0, 'quantity': 1}}


def test_total(cart):
    cart.add_item(orange, 1.00)
    cart.add_item(apple, 2.00)
    cart.add_item(soda, 2.00)
    cart.add_item(water, 1.00)
    cart.remove_item(apple)
    assert cart.get_total_price() == 4.00
#
#
# def test_clear_cart(cart):
#     cart.add_item(apple, 1.00)
#     cart.add_item(soda, 2.00)
#     cart.add_item(water, 1.00)
#     cart.clear_cart()
#     assert cart.items == {}
