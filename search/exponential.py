from .binary import binary_search


def exponential_search(array: list, element: object) -> object:
    """
    :param array:
    :param element:
    :return: element
    Exponential search is an uncommon algorithm
    It works by first finding a range in which the target value is likely to be found,
    then performing a binary search within that range to find the exact location of the target value.
    the time complexity of this algorithm is O(log n) such as in Binary search
    """
    if array[0] == element:
        return 0
    index = 1
    length = len(array)
    while index < length and array[index] <= element:
        index *= 2
    diff = min(index, length-1) - (index//2)
    return binary_search(array=array[index//2:min(index, length-1)], element=element) + diff
