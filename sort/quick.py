def quick_sort(array: list) -> list:
    """
    :param array:
    :return: list:

    Quick Sort is similar to merge sort, it is also runs algorithm recursively but separate it via pivot,
    which uses it for comparing, this algorithm too has the time of the algorithm O(n log n)
    """

    length = len(array)
    if length <= 1:
        return array

    left, right = [], []
    pivot = array[0]
    for item in array[1:]:
        if item <= pivot:
            left.append(item)
        if item > pivot:
            right.append(item)

    return quick_sort(left) + [pivot] + quick_sort(right)
