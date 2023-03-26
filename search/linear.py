def linear_search(array: list, element: object) -> object:
    """
    :param array:
    :param element:
    :return: element
    Linear search is the most common search algorithm,
    this algorithm is used under hood of python interpreter, in operator "in",
    the time complexity of this algorithm is O(n)
    """
    index = 0
    length = len(array)
    while index < length:
        if array[index] == element:
            return index
        index += 1
    return -1
