from main import gen_array
from sort.bubble import bubble_sort
from sort.insertion import insertion_sort
from sort.merge import merge_sort
from sort.quick import quick_sort


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


if __name__ == '__main__':
    test_bubble_sort()
    test_insertion_sort()
    test_merge_sort()
    test_quick_sort()
