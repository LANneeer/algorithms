from structures.trees import BinaryNode, Node
from structures.graphs import Graph

def test_binary_tree():
    tree_dict = {1: [{2: [{4: []}, {5: []}]}, {3: [{6: []}, {7: []}]}]}
    tree = BinaryNode(1)
    for node in range(2, 8):
        tree.node = BinaryNode(node)
    assert tree_dict == tree.to_dict(tree), tree.to_dict(tree)


def test_non_binary_tree():
    tree_dict = {1: [{2: [{5: []}]}, {3: []}, {4: []}]}
    tree = Node(1)
    tree.node = Node(2), 1
    tree.node = Node(3), 1
    tree.node = Node(4), 1
    tree.node = Node(5), 2
    assert tree_dict == tree.to_dict(tree), tree.to_dict(tree)


def test_graph():
    graph_dict = {1: [2, 3], 2: [1, 4], 3: [1], 4: [2], 5: [], 6: []}
    graph = Graph()
    for vertex in range(1, 7):
        graph.vertex = vertex
    graph.add_edge(1, 2)
    graph.add_edge(3, 1)
    graph.add_edge(4, 2)
    assert graph_dict == graph.vertex, graph.vertex


if __name__ == '__main__':
    test_binary_tree()
    test_non_binary_tree()
    test_graph()
