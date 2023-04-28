def sum_list(input_list):
    return sum(input_list)


def reverse_string(input_string):
    return input_string[::-1]


def find_largest_smallest_item(input_array: list):

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





