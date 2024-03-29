from structures.trees import BinaryNode, Node, BinarySearchNode
from structures.graphs import Graph, LinkedList, LNode
from structures.queue import Queue
from structures.stack import Stack
from helpers.mock_data import gen_array


def test_binary_tree():
    tree_dict = {1: [{2: [{4: []}, {5: []}]}, {3: [{6: []}, {7: []}]}]}
    tree = BinaryNode(1)
    for node in range(2, 8):
        tree.node = BinaryNode(node)
    assert tree_dict == tree.to_dict(tree), tree.to_dict(tree)


def test_binary_search_tree():
    tree_dict = {
        1:
            [
                {0: [
                    {-2: [
                        {-1: []}
                    ]}
                ]},
                {2: [
                    {3: []}
                ]}
            ]
    }
    tree = BinarySearchNode(1)
    tree.node = BinarySearchNode(0)
    tree.node = BinarySearchNode(2)
    tree.node = BinarySearchNode(-2)
    tree.node = BinarySearchNode(3)
    tree.node = BinarySearchNode(-1)
    assert tree_dict == tree.to_dict(tree), tree.to_dict(tree)
    assert -2 == tree.binary_search(-2).data, tree.binary_search(-2).data
    tree.delete(-2)
    assert tree_dict != tree.to_dict(tree), tree.to_dict(tree)


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


def test_linked_list():
    native_list = gen_array(length=10)
    linked_list = LinkedList(nodes=[item for item in native_list])
    native_list.append(12)
    linked_list.add_last(LNode(12))
    list_of_linked_list = [node.data for node in linked_list]
    assert native_list == list_of_linked_list, list_of_linked_list


def test_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue_list = [item for item in queue]
    assert [1, 2, 3] == queue_list, queue_list
    assert [] == list(queue.items), queue.items


def test_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack_pack = [item for item in stack]
    assert [3, 2, 1] == stack_pack, stack_pack
    assert [] == list(stack.items), stack.items


if __name__ == '__main__':
    test_binary_tree()
    test_non_binary_tree()
    test_graph()
    test_queue()
    test_linked_list()
    test_stack()
