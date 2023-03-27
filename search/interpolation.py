def interpolation_search(array: list, element: object) -> object:
    """
    :param array:
    :param element:
    :return: element

    Interpolation search is an uncommon algorithm,
    that works by using a position formula
    to estimate the probable position of the target element in a sorted array
    the time complexity of this algorithm is amazing O(log(log(n)))
    """
    low = 0
    high = len(array) - 1
    while low <= high and array[low] <= element <= array[high]:
        position = low + (
                (element - array[low]) * (high -low) //
                (array[high] - array[low])
        )

        if array[position] > element:
            high = position - 1
        elif array[position] < element:
            low = position + 1
        else:
            return position
    return -1
