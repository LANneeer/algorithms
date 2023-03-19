from helpers.mock_data import gen_array
from search import linear_search, binary_search
from sort import quick_sort

def test_linear_search():
    array = gen_array(length=10)
    test_item = array[5]
    item = linear_search(array=array, element=array[5])
    assert item == test_item, item


def test_binary_search():
    array = gen_array(length=10)
    sorted_array = quick_sort(array=array)
    test_item = array[5]
    item = binary_search(array=sorted_array, element=array[5])
    assert item == test_item, item


if __name__ == '__main__':
    test_linear_search()
    test_binary_search()
