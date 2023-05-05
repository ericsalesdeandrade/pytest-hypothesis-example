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


input_strategy = st.lists(st.tuples(items_strategy(),
                                    st.integers(min_value=1, max_value=10),
                                    price_strategy()),
                          min_size=1, max_size=2)


# Property Based Testing
@given(input_strategy)
def test_add_item_hypothesis(input_list):
    cart = ShoppingCart()

    # Assert that the quantity of items in the cart is equal to the number of items added
    for item, qty, price in input_list:
        cart.add_item(item=item, quantity=qty, price=price)
        assert item.name in cart.items

    assert sum(item['quantity'] for item in cart.items.values()) == sum(item[1] for item in input_list)


# @given(st.lists(st.tuples(items_strategy(),
#                           st.integers(min_value=1, max_value=10),
#                           price_strategy()),
#                 min_size=1, max_size=2))
# def test_remove_item_hypothesis(input_list):
#     cart = ShoppingCart()
#
#     # Add items to cart
#     for item, qty, price in input_list:
#         cart.add_item(item=item, quantity=qty, price=price)
#         assert item.name in cart.items
#
#     # Remove items from cart
#     for item, qty, price in input_list:
#         cart.remove_item(item=item)
#         print(cart.items)
# assert item.name not in cart.items

@given(input_strategy)
def test_calculate_total_hypothesis(input_list):
    cart = ShoppingCart()

    # Add items to cart
    for item, qty, price in input_list:
        cart.add_item(item=item, quantity=qty, price=price)

    # Calculate total
    total = cart.get_total_price()

    # Assert that the total is equal to the sum of the price of each item multiplied by the quantity of each item
    print(input_list)
    print(total)
    print(sum(item[1] * item[2] for item in input_list))
    assert total == sum(item[1] * item[2] for item in input_list)
