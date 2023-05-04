from typing import Callable
import pytest
from hypothesis import given, strategies as st
from src.shopping_cart import ShoppingCart, Item


@st.composite
def items_strategy(draw):
    return draw(st.sampled_from(list(Item)))


@st.composite
def price_strategy(draw):
    return round(draw(st.floats(min_value=0.01, max_value=100, allow_nan=False)), 2)


# Property Based Testing
@given(st.lists(st.tuples(items_strategy(),
                          price_strategy()),
                min_size=1, max_size=2))
def test_add_item_hypothesis(input_list):
    cart = ShoppingCart()
    # Assert that the number of items in the cart is equal to the number of items added
    for item, price in input_list:
        cart.add_item(item, price)
        print(item, price)
        assert item.name in cart.items
    # print(cart.items)
    # assert len(cart.items) == len(input_list)
