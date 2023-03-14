from structures.trees import BinaryNode, Node


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


if __name__ == '__main__':
    test_binary_tree()
    test_non_binary_tree()
