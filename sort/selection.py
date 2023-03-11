def selection_sort(array: list) -> list:
    """
    :param array:
    :return: list:

    Selection Sort is very similar to Bubble sort and too has the time of the algorithm O(n^2)
    In Selection Sort we select item with minimum value and compare with each array item
    """

    length = len(array)
    for i in range(length):
        min_ = i
        for j in range(i+1, length):
            if array[min_] > array[j]:
                min_ = j
        array[i], array[min_] = array[min_], array[i]
    return array
