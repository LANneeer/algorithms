from helpers.mock_data import gen_array
from search import linear_search, binary_search, exponential_search, interpolation_search
from sort import quick_sort


def test_linear_search():
    array = gen_array(length=10)
    item = linear_search(array=array, element=array[5])
    assert item == 5, item


def test_binary_search():
    array = gen_array(length=10)
    sorted_array = quick_sort(array=array)
    item = binary_search(array=sorted_array, element=sorted_array[5])
    assert item == 5, item


def test_exponential_search():
    array = gen_array(length=10)
    sorted_array = quick_sort(array=array)
    item = exponential_search(array=sorted_array, element=sorted_array[5])
    assert item == 5, item


def test_interpolation_search():
    array = gen_array(length=10)
    sorted_array = quick_sort(array=array)
    item = interpolation_search(array=sorted_array, element=sorted_array[5])
    assert item == 5, item


if __name__ == '__main__':
    test_linear_search()
    test_binary_search()
    test_exponential_search()
    test_interpolation_search()

