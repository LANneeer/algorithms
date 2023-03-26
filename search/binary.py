def binary_search(array: list, element: object) -> object:
    """
    :param array:
    :param element:
    :return: element
    Binary search is an uncommon search algorithm,
    because it can be used with only sorted array,
    however the time complexity of this algorithm is O(log n)
    """
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] > element:
            high = mid - 1
        elif array[mid] < element:
            low = mid + 1
        else:
            return mid
    return -1
