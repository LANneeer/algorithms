def merge_sort(array: list) -> list:
    """
    :param array:
    :return: list:

    Merge sort is a sorting via separating array in two arrays and sort them easily,
    this algorithm runs recursively and have two functions,
    first is separate array and second merge them with sorting
    this algorithm has the time of the algorithm O(n log n)
    """
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left=left, right=right)


def merge(left: list, right: list) -> list:
    """
    :param left:
    :param right:
    :return: array:
    A function for merge and compare two arrays to one sorted array
    """
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    array = []
    left_index = 0
    right_index = 0

    while len(array) < len(left) + len(right):
        if left[left_index] <= right[right_index]:
            array.append(left[left_index])
            left_index += 1
        else:
            array.append(right[right_index])
            right_index += 1

        if right_index == len(right):
            array += left[left_index:]
            break

        if left_index == len(left):
            array += right[right_index:]
            break
    return array
