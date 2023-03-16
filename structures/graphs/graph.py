class Graph:
    """
    Graph is a data structure that has vertices that can be connected like nodes in a tree,
    in a vertex graph they can be represented as a network, hierarchy,
    have a connections and have a direction of connections.
    """
    def __init__(self):
        self.vertices = {}

    def __repr__(self):
        return f'Graph<vertices: {self.vertices}>'

    @property
    def vertex(self) -> dict:
        """
        :return: set
        Create getter for vertex in graph
        """
        return self.vertices

    @vertex.setter
    def vertex(self, vertex: int) -> None:
        """
        :param vertex:
        :return:
        Create setter to add vertex in a graph
        """
        self.vertices[vertex] = []

    def add_edge(self, vertex1: int, vertex2: int) -> None:
        """
        :param vertex1:
        :param vertex2:
        :return:
        Create edges aka connections setter for a vertices,
        if it does not exist we just create it and create connection that named as edge
        """
        if vertex1 not in self.vertices:
            self.vertices[vertex1] = []
        if vertex2 not in self.vertices:
            self.vertices[vertex2] = []
        self.vertices[vertex1].append(vertex2)
        self.vertices[vertex2].append(vertex1)
