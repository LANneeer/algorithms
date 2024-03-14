def heap_sort(array: list) -> list:
    """
    Heap sort is similar to Quick sort and also "separate" array to left and right sides,
    Heap sort use one array and shift items in array
    :param array:
    :return: list:
    """

    length = len(array)

    for i in range(length//2-1, -1, -1):
        heaping(array=array, length=length, index=i)

    for i in range(length-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heaping(array=array, length=i, index=0)

    return array


def heaping(array: list, length: int, index: int) -> list:
    max_ = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < length and array[left] > array[max_]:
        max_ = left

    if right < length and array[right] > array[max_]:
        max_ = right

    if max_ != index:
        array[index], array[max_] = array[max_], array[index]
        heaping(array=array, length=length, index=max_)
