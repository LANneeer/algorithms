from helpers.mock_data import gen_array
from structures.graphs.graph import Graph
from search import (linear_search, binary_search, exponential_search, interpolation_search,
                    breadth_first_search, depth_first_search)

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


def test_breadth_first_search():
    graph_dict = {1: [2, 3], 2: [1, 4], 3: [1], 4: [2], 5: [], 6: []}
    graph = Graph()
    for vertex in range(1, 7):
        graph.vertex = vertex
    graph.add_edge(1, 2)
    graph.add_edge(3, 1)
    graph.add_edge(4, 2)
    graph.add_edge(4, 6)
    node = 6
    path = breadth_first_search(graph=graph, node=node)
    assert path == [1, 2, 4, 6], path


# def test_depth_first_search():
#     graph_dict = {1: [2, 3], 2: [1, 4], 3: [1], 4: [2], 5: [], 6: []}
#     graph = Graph()
#     for vertex in range(1, 7):
#         graph.vertex = vertex
#     graph.add_edge(1, 2)
#     graph.add_edge(3, 1)
#     graph.add_edge(4, 2)
#     start = 1
#     end = 6
#     path = depth_first_search(node=end)
#     assert path == [1, 2, 6], path


if __name__ == '__main__':
    test_linear_search()
    test_binary_search()
    test_exponential_search()
    test_interpolation_search()
    test_breadth_first_search()
    # test_depth_first_search()

