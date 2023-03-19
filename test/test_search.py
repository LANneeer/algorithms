from helpers.mock_data import gen_array
from search import linear_search


def test_linear_search():
    array = gen_array(length=10)
    test_item = array[5]
    item = linear_search(array=array, element=array[5])
    assert item == test_item, item


if __name__ == '__main__':
    test_linear_search()
