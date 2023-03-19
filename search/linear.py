def linear_search(array: list, element: object) -> object:
    """
    :param array:
    :param element:
    :return: element
    Linear search is the most common search algorithm,
    this algorithm is used under hood of python interpreter, in operator "in",
    the time complexity of this algorithm is O(n)
    """
    for item in array:
        if item == element:
            return item
    return -1
