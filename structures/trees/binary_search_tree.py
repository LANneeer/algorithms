from .tree import Node


class BinarySearchNode(Node):
    """
    Node is a part of Tree with some value and linked with other nodes with edges.
    In this example we created Binary Search Tree which have two edges for each node,
    and balance tree by adding new nodes in right or left side of tree
    """

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return f'Node<data: {self.data}, nodes: {self.node}>'

    def __eq__(self, other):
        return self.data == other.data

    def __gt__(self, other):
        return self.data > other.data

    def __lt__(self, other):
        return self.data < other.data

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
        if we again have two not None edges we repeat this cycle,
        if new node value is less than current node value we add new node in left side,
        else we add new node in right side
        """
        if self > node:
            if not self.left:
                self.left = node
            else:
                self.left.node = node
        if self < node:
            if not self.right:
                self.right = node
            else:
                self.right.node = node

    def to_dict(self, node: 'Node'):
        """
        :param node:
        :return: list
        """
        return {node.data: [self.to_dict(edge) for edge in node.node if edge]}

    def binary_search(self, element: object) -> Node:
        """
        :param element:
        :return: element
        Binary search is an uncommon search algorithm,
        because it can be used with only sorted array,
        however the time complexity of this algorithm is O(log n)
        """
        if self.data == element:
            return self
        if self.data > element:
            return self.left.binary_search(element) if self.left else None
        else:
            return self.right.binary_search(element) if self.right else None

    def delete(self, value: object) -> None:
        """
        :param value:
        :return: None
        """
        if not self:
            return None
        if self.data == value:
            if self.left:
                self.data = self.left.data
                self.left.delete(self.left.data)
            else:
                if self.right:
                    self.data = self.right.data
                    self.right.delete(self.right.data)
                else:
                    self.data = None
                    return None
        if self.left and self.data > value:
            self.left.delete(value)
        else:
            if self.right:
                self.right.delete(value)
