from structures.graphs.graph import Graph


def depth_first_search(graph: Graph, node: Graph):
    visited = []
    stack = [node]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend([n for n in node.vertices if n not in visited])
    return visited
