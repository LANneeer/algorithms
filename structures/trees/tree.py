class Node:
    """
    Node is a part of Tree with some value and linked with other nodes with edges.
    In this example we created Binary Tree which have two edges for each node
    """
    def __init__(self, data):
        self.nodes = []
        self.data = data

    def __repr__(self):
        return f'Node<data: {self.data}, nodes: {self.node}>'

    @property
    def node(self) -> list:
        """
        :return: list

        Creating getter and make it as property
        """
        return self.nodes

    @node.setter
    def node(self, node_and_root: list['Node', int]) -> None:
        """
        :param node:
        :return:

        Creating setter which set edges for each None edge,
        if we have two not None edges we get deep in Node and search in this Node None edge,
        if we again have two not None edges we repeat this cycle
        """
        node, root = node_and_root
        if root:
            if root == self.data:
                self.nodes.append(node)
            nodes = self.node
            while nodes:
                for child in nodes:
                    if child.data == root:
                        child.node.append(node)
                        nodes = False
                        break
                    else:
                        nodes = child.node
        else:
            self.nodes.append(node)

    def to_list(self, node: 'Node'):
        """
        :param node:
        :return:  list
        """
        node_list = []
        for edge in node.node:
            if edge:
                node_list.append(edge.data)
                node_list.append(self.to_list(node=edge))
        return node_list

    def to_dict(self, node: 'Node'):
        """
        :param node:
        :return: list
        """
        return {node.data: [self.to_dict(edge) for edge in node.node if edge]}
