# Array Operations


def find_largest_smallest_item(input_array: list) -> tuple:
    """
    Function to find the largest and smallest items in an array
    :param input_array: Input array
    :return: Tuple of largest and smallest items
    """

    if len(input_array) == 0:
        raise ValueError
    # Set the initial values of largest and smallest to the first item in the array
    largest = input_array[0]
    smallest = input_array[0]

    # Iterate through the array
    for i in range(1, len(input_array)):
        # If the current item is larger than the current value of largest, update largest
        if input_array[i] > largest:
            largest = input_array[i]
        # If the current item is smaller than the current value of smallest, update smallest
        if input_array[i] < smallest:
            smallest = input_array[i]

    return largest, smallest


def sort_array(input_array: list, sort_key: str) -> list:
    """
    Function to sort an array
    :param sort_key: Sort key
    :param input_array: Input array
    :return: Sorted array
    """
    if len(input_array) == 0:
        raise ValueError
    if sort_key not in input_array[0]:
        raise KeyError
    if not isinstance(input_array[0][sort_key], int):
        raise TypeError
    sorted_data = sorted(input_array, key=lambda x: x[sort_key], reverse=True)
    return sorted_data


# String Operations


def reverse_string(input_string) -> str:
    """
    Function to reverse a string
    :param input_string: Input string
    :return: Reversed string
    """
    return input_string[::-1]


def complex_string_operation(input_string: str) -> str:
    """
    Function to perform a complex string operation
    :param input_string: Input string
    :return: Transformed string
    """
    # Remove Whitespace
    input_string = input_string.strip().replace(" ", "")

    # Convert to Upper Case
    input_string = input_string.upper()

    # Remove vowels
    vowels = ("A", "E", "I", "O", "U")
    for x in input_string.upper():
        if x in vowels:
            input_string = input_string.replace(x, "")

    return input_string
