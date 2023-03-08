from main import gen_array
from sort.bubble import bubble_sort


def test_bubble_sort():
    array = gen_array(length=100)
    sorted_array = sorted(array)
    assert bubble_sort(array) == sorted_array, bubble_sort(array)


if __name__ == '__main__':
    test_bubble_sort()
