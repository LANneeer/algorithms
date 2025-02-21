import matplotlib
matplotlib.use("MacOSX")
import matplotlib.pyplot as plt
from structures.trees.red_and_black_tree import tree


def draw_node(ax, name, position, color):
    circle = plt.Circle(position, 0.15, color=color, ec='black', lw=1.5, zorder=2)
    ax.add_artist(circle)
    ax.text(*position, name, color='white', ha='center', va='center', fontsize=12, zorder=3)


def plot_tree(ax, tree, x=0, y=0, dx=1, node_info=None):
    if tree is None:
        return x, None
    if node_info is None:
        node_info = {}

    name = next(iter(tree))  # Get the root node name
    color = 'black' if 'Black' in name else 'red'
    if y not in node_info:
        node_info[y] = [x, None, None]  # position, left child position, right child position

    left_child = tree[name].get('left')
    right_child = tree[name].get('right')

    next_y = y - 1
    left_x = None
    right_x = None

    # Plot left subtree
    if left_child:
        x, left_x = plot_tree(ax, left_child, x, next_y, dx / 2, node_info)
        node_info[next_y][1] = left_x

    # This node's position
    current_position = x

    # Plot right subtree
    if right_child:
        x += dx
        x, right_x = plot_tree(ax, right_child, x, next_y, dx / 2, node_info)
        node_info[next_y][2] = right_x

    # Draw this node
    draw_node(ax, name, (current_position, y), color)

    # Draw lines to children
    if left_x is not None:
        ax.plot([current_position, left_x], [y, next_y], 'k-', lw=2, zorder=1)
    if right_x is not None:
        ax.plot([current_position, right_x], [y, next_y], 'k-', lw=2, zorder=1)

    return x, current_position


def visualize_red_black_tree(tree):
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_aspect('equal')
    ax.axis('off')
    tree_dict = tree.to_dict()
    if isinstance(tree_dict, str):  # Tree is empty
        print(tree_dict)
    else:
        _, root_pos = plot_tree(ax, tree_dict)
        # Adjust the plot limits
        ax.set_xlim(root_pos - 1, root_pos + 1)
        ax.set_ylim(-len(tree_dict) - 1, 1)

    # Optionally disable clipping for text
    for artist in ax.get_children():
        if isinstance(artist, plt.Text):
            artist.set_clip_on(False)

    plt.autoscale()
    plt.show()


# Example usage, assuming the tree has methods to insert and to_dict already implemented


visualize_red_black_tree(tree)
