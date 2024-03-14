from typing import Union, Any
import json


class Node:
    """
    Node is a part of Tree with some value and linked with other nodes with edges.
    In this example we created Heap which have two edges for each node
    """
    def __init__(self, data: Any):
        self.left: Union[Node, None] = None
        self.right: Union[Node, None] = None
        self.data: Any = data

    def __repr__(self):
        return f'Node<data: {self.data}, nodes: {self.node}>'

    @property
    def node(self) -> list:
        """
        :return: list

        Creating getter and make it as property
        """
        return [self.left, self.right]

    @node.setter
    def node(self, node: 'Node') -> None:
        """
        :param node:
        :return:

        Creating setter which set edges for each None edge,
        if we have two not None edges we get deep in Node and search in this Node None edge,
        if we again have two not None edges we repeat this cycle
        """
        if not self.left:
            self.left = node
        elif not self.right:
            self.right = node
        else:
            nodes = self.node
            while nodes:
                for child in nodes:
                    if not child.left:
                        child.left = node
                        nodes = False
                        break
                    elif not child.right:
                        child.right = node
                        nodes = False
                        break
                    else:
                        nodes = child.node

    def to_list(self, node: 'Node'):
        """
        :param node:
        :return:  list
        """
        node_list = []

        nodes = node
        while nodes:
            for child in nodes:
                if child.left:
                    node_list.append(child.left.data)
                    nodes = False
                    break
                elif child.right:
                    node_list.append(child.right.data)
                    nodes = False
                    break
                else:
                    nodes = child.node
        return node_list

    def to_dict(self, node: 'Node'):
        """
        :param node:
        :return: list
        """
        return {node.data: [self.to_dict(edge) for edge in node.node if edge]}


class Heap(Node):
    def heapify(self, node: Node) -> Union[Node, None]:
        """
        Heapify is a process of creating a heap from a node.
        :param node:
        :return: Node
        """
        if node is None:
            return None

        left = self.heapify(node.left)
        right = self.heapify(node.right)

        if left is not None and left.data < node.data:
            node.data, left.data = left.data, node.data
        if right is not None and right.data < node.data:
            node.data, right.data = right.data, node.data

        return node


my_heap = Heap(58)  # add 1st node
my_heap.node = Node(63)  # add 2nd node
my_heap.node = Node(100)  # add 3rd node
my_heap.node = Node(31)  # add 4th node
my_heap.node = Node(449)  # add 5th node
my_heap.node = Node(22)  # add 6th node
# show heap
print(json.dumps(my_heap.to_dict(my_heap), indent=4))
my_heap.heapify(my_heap)
my_heap.heapify(my_heap)
my_heap.heapify(my_heap)
print("======== SORT IS DONE ========")
# show sorted heap
print(json.dumps(my_heap.to_dict(my_heap), indent=4))
