def bubble_sort(array: list) -> list:
    """
    :param array:
    :return: list:

    Bubble Sort is a simple sort and has the time of the algorithm O(n^2)
    """

    length = len(array)
    for i in range(length):
        for j in range(i, length):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
