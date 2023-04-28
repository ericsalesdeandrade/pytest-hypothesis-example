from hypothesis import given, strategies as st
import logging
from src.core import sum_list, reverse_string, find_largest_smallest_item

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_sum_list():
    assert sum_list([1, 2, 3]) == 6


def test_reverse_string():
    assert reverse_string("hello") == "olleh"


def test_find_largest_smallest_item():
    assert find_largest_smallest_item([1, 2, 3]) == (3, 1)


# @given(st.lists(st.integers()))
# def test_sum_list_hypothesis(input_list):
#     logger.info(f"input_list: {input_list}")
#     assert sum_list(input_list) == sum(input_list)
#
#
# @given(st.text())
# def test_reverse_string_hypothesis(input_string):
#     logger.info(f"input_string: {input_string}")
#     assert reverse_string(input_string) == input_string[::-1]

@given(st.lists(st.integers(), min_size=1))
def test_find_largest_smallest_item_hypothesis(input_list):
    logger.info(f"input_list: {input_list}")
    assert find_largest_smallest_item(input_list) == (max(input_list), min(input_list))


