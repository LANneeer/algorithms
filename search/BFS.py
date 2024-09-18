from structures.graphs.graph import Graph


def breadth_first_search(graph: Graph, node):
    # node is the starting position
    # graph is the graph in dictionary format
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:
        print(queue, visited)
        s = queue.pop(0)

        for x in graph.vertices[s]:
            if x not in visited:
                visited.append(x)
                queue.append(x)
    visited.reverse()
    return visited
