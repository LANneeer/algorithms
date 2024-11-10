import json

from structures.trees import Node


class RedBlackNode(Node):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = None
        self.color = False  # False for Red, True for Black
        self.data = data

    def __repr__(self):
        return f"RedBlackNode(data={self.data}, color={'Black' if self.color else 'Red'})"


class RedBlackTree:
    def __init__(self):
        self.root = None

    def to_dict(self):
        """ Convert the entire tree to a dictionary. """
        if not self.root:
            return "The tree is empty"
        return self._to_dict_helper(self.root)

    def _to_dict_helper(self, node):
        """ Helper function to recursively convert the tree to a dictionary. """
        if not node:
            return None
        node_repr = f"{node.data} ({'Black' if node.color else 'Red'})"
        result = {node_repr: {}}
        if node.left:
            result[node_repr]['left'] = self._to_dict_helper(node.left)
        if node.right:
            result[node_repr]['right'] = self._to_dict_helper(node.right)
        return result

    def insert(self, data):
        new_node = RedBlackNode(data)
        if not self.root:
            self.root = new_node
            self.root.color = True  # Root is always black
        else:
            self._insert(self.root, new_node)
        self.insert_fix_up(new_node)

    def _insert(self, current, node):
        if node.data < current.data:
            if current.left is None:
                current.left = node
                node.parent = current
            else:
                self._insert(current.left, node)
        else:
            if current.right is None:
                current.right = node
                node.parent = current
            else:
                self._insert(current.right, node)

    def insert_fix_up(self, node):
        while node != self.root and node.parent.color == False:
            parent = node.parent
            grandparent = parent.parent
            if parent == grandparent.left:
                uncle = grandparent.right
                if uncle and uncle.color == False:
                    parent.color = uncle.color = True
                    grandparent.color = False
                    node = grandparent
                else:
                    if node == parent.right:
                        self.left_rotate(parent)
                        node = parent
                    parent.color = True
                    grandparent.color = False
                    self.right_rotate(grandparent)
            else:
                uncle = grandparent.left
                if uncle and uncle.color == False:
                    parent.color = uncle.color = True
                    grandparent.color = False
                    node = grandparent
                else:
                    if node == parent.left:
                        self.right_rotate(parent)
                        node = parent
                    parent.color = True
                    grandparent.color = False
                    self.left_rotate(grandparent)
            self.root.color = True

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y


tree = RedBlackTree()
tree.insert(50)
tree.insert(4)
tree.insert(3)
tree.insert(22)
tree.insert(1)
tree.insert(10)

data = json.dumps(tree.to_dict(), indent=4)
print(data)
