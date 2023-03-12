from main import gen_array
from sort import bubble_sort, insertion_sort, merge_sort, quick_sort, selection_sort, heap_sort


def test_bubble_sort():
    array = gen_array(length=100)
    sorted_array = sorted(array)
    assert bubble_sort(array) == sorted_array, bubble_sort(array)


def test_insertion_sort():
    array = gen_array(length=100)
    sorted_array = sorted(array)
    assert insertion_sort(array) == sorted_array, insertion_sort(array)


def test_merge_sort():
    array = gen_array(length=100)
    sorted_array = sorted(array)
    assert merge_sort(array) == sorted_array, merge_sort(array)


def test_quick_sort():
    array = gen_array(length=100)
    sorted_array = sorted(array)
    assert quick_sort(array) == sorted_array, quick_sort(array)


def test_selection_sort():
    array = gen_array(length=100)
    sorted_array = sorted(array)
    assert selection_sort(array) == sorted_array, selection_sort(array)


def test_heap_sort():
    array = gen_array(length=100)
    sorted_array = sorted(array)
    assert heap_sort(array) == sorted_array, heap_sort(array)


if __name__ == '__main__':
    test_bubble_sort()
    test_insertion_sort()
    test_merge_sort()
    test_quick_sort()
    test_selection_sort()
    test_heap_sort()
