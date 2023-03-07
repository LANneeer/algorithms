from main import gen_array
from sort.bubble import sort


def test_bubble_sort():
    array = gen_array(length=100)
    sorted_array = sorted(array)
    assert sort(array) == sorted_array, sort(array)


if __name__ == '__main__':
    test_bubble_sort()
