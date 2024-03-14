def merge_sort(array: list) -> list:
    """
    Merge sort is a sorting via separating array in two arrays and sort them easily,
    this algorithm runs recursively and have two functions,
    first is separate array and second merge them with sorting
    this algorithm has the time of the algorithm O(n log n)
    :param array:
    :return: list:
    """
    if len(array) <= 2:
        return array

    mid = len(array) // 2
    if mid % 2 != 0:
        mid += 1

    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)


def merge(left: list, right: list) -> list:
    """
    A function for merge and compare two arrays to one sorted array
    :param left:
    :param right:
    :return: array:
    """
    left_index = 0
    right_index = 0
    merged = []

    while left_index < len(left) and right_index < len(right):
        left_pair = (left[left_index], left[left_index + 1])
        right_pair = (right[right_index], right[right_index + 1])

        if left_pair <= right_pair:
            merged.extend(left_pair)
            left_index += 2
        else:
            merged.extend(right_pair)
            right_index += 2

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


array = [123, 1, 213, 3, 324, 4, 213, 2, 213, 5]
sorted_array = merge_sort(array)
print(sorted_array)
