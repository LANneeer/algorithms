class LNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.data}'


class LinkedList:
    """
    Yes, linked list is a part of graph structures, and use the same relation logic,
    Every object has a link to next object, it seems like one-directed graph
    """

    def __init__(self, nodes: list[LNode] = None):
        self.head = None
        if nodes:
            node = LNode(nodes.pop(0))
            self.head = node
            for item in nodes:
                node.next = LNode(item)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []

        while node:
            nodes.append(node.data)
            node = node.next
        return ' -> '.join([str(node) for node in nodes])

    def __iter__(self):
        node = self.head

        while node:
            yield node
            node = node.next

    def add_first(self, node: LNode) -> None:
        """
        :param node:
        :return:
        In linked list operation to add FIRST has the time of the algorithm O(1),
        because we not iterate all items in this list
        """
        node.next, self.head = self.head, node

    def add_last(self, node: LNode) -> None:
        """
        :param node:
        :return:
        However linked list operation to add LAST has the time of the algorithm O(n),
        because we need to get last item from this list, and we will iterate all items in list
        """
        if not self.head:
            self.head = node
        else:
            for current_node in self:
                pass
            current_node.next = node

