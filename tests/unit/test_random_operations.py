import pytest
from hypothesis import given, strategies as st
from hypothesis import assume as hypothesis_assume
import logging
from src.random_operations import (
    reverse_string,
    find_largest_smallest_item,
    complex_string_operation,
    sort_array,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Example Based Unit Testing
def test_find_largest_smallest_item():
    assert find_largest_smallest_item([1, 2, 3]) == (3, 1)


def test_reverse_string():
    assert reverse_string("hello") == "olleh"


def test_sort_array():
    data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 20},
        {"name": "David", "age": 35},
    ]
    assert sort_array(data, "age") == [
        {"name": "David", "age": 35},
        {"name": "Bob", "age": 30},
        {"name": "Alice", "age": 25},
        {"name": "Charlie", "age": 20},
    ]


def test_complex_string_operation():
    assert complex_string_operation("  Hello World  ") == "HLLWRLD"


# Property Based Unit Testing
@given(st.lists(st.integers(), min_size=1, max_size=25))
def test_find_largest_smallest_item_hypothesis(input_list):
    assert find_largest_smallest_item(input_list) == (max(input_list), min(input_list))


@given(
    st.lists(
        st.fixed_dictionaries({"name": st.text(), "age": st.integers()}),
    )
)
def test_sort_array_hypothesis(input_list):
    if len(input_list) == 0:
        with pytest.raises(ValueError):
            sort_array(input_list, "age")

    hypothesis_assume(len(input_list) > 0)
    assert sort_array(input_list, "age") == sorted(
        input_list, key=lambda x: x["age"], reverse=True
    )


@given(st.text())
def test_reverse_string_hypothesis(input_string):
    assert reverse_string(input_string) == input_string[::-1]


@given(st.text())
def test_complex_string_operation_hypothesis(input_string):
    assert complex_string_operation(input_string) == input_string.strip().replace(
        " ", ""
    ).upper().replace("A", "").replace("E", "").replace("I", "").replace(
        "O", ""
    ).replace(
        "U", ""
    )
