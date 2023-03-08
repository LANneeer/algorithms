def insertion_sort(array: list) -> list:
    """
    :param array:
    :return: list:

    Insertion Sort is similar to Bubble sort and too has the time of the algorithm O(n^2)
    """

    length = len(array)
    for i in range(1, length):
        item = array[i]
        j = i - 1
        while j >= 0 and item < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = item
    return array
