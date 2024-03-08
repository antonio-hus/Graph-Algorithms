# Representation of the Directed Graph


# Vertex Representation
class Vertex:
    def __init__(self, number):
        self.__number = number

    @property
    def number(self):
        return self.__number


# Edge Representation
class Edge:
    def __init__(self, source_vertex: Vertex, target_vertex: Vertex):
        self.__source = source_vertex
        self.__target = target_vertex

    @property
    def source(self):
        return self.__source

    @property
    def target(self):
        return self.__target


# Custom Exception Class
class DirectedGraphException(Exception):
    pass


# Graph Iterators
class DirectedGraphVertexIterator:
    def __init__(self, graph):
        self.__elements = graph.vertices()
        self.__index = 0

    def first(self):
        self.__index = 0

    def next(self):
        if self.valid():
            self.__index += 1
        else:
            raise DirectedGraphException("Out of vertices list bounds!")

    def valid(self):
        return self.__index < len(self.__elements)

    def getCurrent(self):
        return self.__elements[self.__index]


class DirectedGraphOutboundIterator:
    def __init__(self, graph):
        self.__graph = graph


class DirectedGraphInboundIterator:
    def __init__(self, graph):
        self.__graph = graph


# Directed Graph Class
class DirectedGraph:

    def __init__(self):
        # Number of vertices in the Graph
        self.__vertices = 0
        self.__edges = 0

        # Inbound / Outbound Neighbours
        self.__inbound = {}
        self.__outbound = {}

        # Costs of the Edges of the Graphs
        self.__costs = {}

    # Get The Number Of Vertices
    def vertices_count(self):
        """
        Returns the number of vertices inside the Directed Graph
        """
        return self.__vertices

    def vertices(self):
        """
        Returns the vertices inside the Directed Graph
        """
        vertices_list = []

        # When added all vertices are both in the inbound and outbound map keys
        # Thus we can parse any one of them
        for vertex in self.__inbound.keys():
            vertices_list.append(vertex)
        return vertices_list

    # Get the Number of Edges
    def edges_count(self):
        """
        Returns the number of edges inside the Directed Graph
        """
        return self.__edges

    # Iterate Vertices
    def vertex_iterator(self):
        return DirectedGraphVertexIterator(self)

    # Parse Outbound Edges
    def outbound_iterator(self):
        return DirectedGraphOutboundIterator(self)

    # Parse Outbound Edges
    def inbound_iterator(self):
        return DirectedGraphInboundIterator(self)

    # Find Edge
    def find_edge(self, source: int, target: int):
        """
        Returns the edge between to given vertices if found, None otherwise
        :param source: Source Vertex
        :param target: Target Vertex
        """
        source = Vertex(source)
        target = Vertex(target)
        edge = Edge(source, target)

        if edge in self.__outbound[source]:
            return edge
        return None

    # Get In / Out Degree of specified Vertex
    def degree(self, vertex: int):
        """
        Returns the inbound, outbound edges count tuple
        :param vertex: Vertex to Search
        """
        vertex = Vertex(vertex)
        inbound = 0
        outbound = 0

        if vertex in self.__inbound.keys():
            inbound = len(self.__inbound[vertex])
        if vertex in self.__outbound.keys():
            outbound = len(self.__outbound[vertex])

        return inbound, outbound

    # Get the cost of an edge
    def get_cost(self, source: int, target: int):
        source = Vertex(source)
        target = Vertex(target)
        edge = Edge(source, target)

        if edge not in self.__costs.keys():
            return None
        return self.__costs[edge]

    # Add or modify cost of an edge
    def modify_cost(self, source: int, target: int, cost: int):
        edge = self.find_edge(source, target)

        # If edge is in the graph
        # Add Value / Update Value from the dictionary
        if edge:
            self.__costs[edge] = cost

    # Add an edge
    def add_edge(self, source: int, target: int):
        """
        Adds a new Edge to the Directed Graph
        If either the source or target vertices not in the graph, add them
        Add the new Edge to the respective inbound and outbound dicts
        :param source: Source Vertex
        :param target: Target Vertex
        """
        source = Vertex(source)
        target = Vertex(target)
        edge = Edge(source, target)

        self.__edges += 1
        if target not in self.__inbound:
            self.add_vertex(target.number)
        self.__inbound[target].append(edge)

        if source not in self.__outbound:
            self.add_vertex(source.number)
        self.__outbound[source].append(edge)

    # Remove an edge
    def remove_edge(self, source: int, target: int):

        # If edge inside the graph, remove it
        # Otherwise return None
        edge = self.find_edge(source, target)
        if edge:
            self.__edges -= 1
            self.__inbound[Vertex(target)].remove(edge)
            self.__outbound[Vertex(source)].remove(edge)
            return edge
        return None

    # Add a vertex
    def add_vertex(self, vertex_number: int):

        # If vertex inside the graph, return None
        # Otherwise add it
        vertex = Vertex(vertex_number)
        if vertex in self.__inbound.keys() or vertex in self.__outbound.keys():
            return None
        self.__vertices += 1
        self.__inbound[vertex] = []
        self.__outbound[vertex] = []
        return vertex

    # Remove vertex
    def remove_vertex(self, vertex_number: int):

        # If vertex inside the graph, remove it
        # Otherwise return None
        vertex = Vertex(vertex_number)
        if vertex not in self.__inbound.keys() or vertex not in self.__outbound.keys():
            return None
        self.__vertices -= 1

        for edge in self.__inbound[vertex]:
            self.remove_edge(edge.source.number, edge.target.number)
        for edge in self.__outbound[vertex]:
            self.remove_edge(edge.source.number, edge.target.number)

        del self.__inbound[vertex]
        del self.__outbound[vertex]

        return vertex

    # Return a copy of the graph
    def copy(self):

        # Graph Structure
        graph_copy = DirectedGraph()

        # Copying all vertices and edges
        for edge in self.__inbound.values():
            graph_copy.add_edge(edge.source.number, edge.target.number)
        for edge in self.__outbound.values():
            graph_copy.add_edge(edge.source.number, edge.target.number)

        # Copying all costs
        for (edge, cost) in self.__costs:
            graph_copy.modify_cost(edge.source.number, edge.target.number, cost)

        return graph_copy
