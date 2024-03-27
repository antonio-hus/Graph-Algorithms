# This module contains the representation of the class DirectedGraph
# Imports Section
from .edge import Edge
from .vertex import Vertex
from .edge import UEdge
from .directed_graph import DirectedGraph


# EXCEPTION CLASS IMPLEMENTATION
class UnDirectedGraphException(Exception):
    """
    Custom Exception Class for the DirectedGraph
    """
    pass


# ITERATOR CLASSES FOR THE UNDIRECTEDGRAPH IMPLEMENTATION
class UnDirectedGraphVertexIterator:
    def __init__(self, graph):
        """
        Parses using the index the set of all vertices from the specified DirectedGraph
        """
        self.__elements = graph.vertices()
        self.__index = 0

    def first(self):
        """
        Sets the index back at the beginning of the elements list
        """
        self.__index = 0

    def next(self):
        """
        Gets the next element's index if in bounds,
        Otherwise raises an UnDirectedGraphException
        """
        if self.valid():
            self.__index += 1
        else:
            raise UnDirectedGraphException("Out of vertices list bounds!")

    def valid(self):
        """
        Checks if the current index is in bounds of the element list length
        """
        return self.__index < len(self.__elements)

    def getCurrent(self):
        """
        Returns the element at the current index
        """
        return self.__elements[self.__index]


class UnDirectedGraphEdgesIterator:
    def __init__(self, graph, vertex: int):
        """
        Parses using the index the set of all inbound edges to a given vertex, from the specified DirectedGraph
        """
        self.__elements = graph.get_edges(vertex)
        self.__index = 0

    def first(self):
        """
        Sets the index back at the beginning of the elements list
        """
        self.__index = 0

    def next(self):
        """
        Gets the next element's index if in bounds,
        Otherwise raises an UnDirectedGraphException
        """
        if self.valid():
            self.__index += 1
        else:
            raise UnDirectedGraphException("Out of edges list bounds!")

    def valid(self):
        """
        Checks if the current index is in bounds of the element list length
        """
        return self.__index < len(self.__elements)

    def getCurrent(self):
        """
        Returns the element at the current index
        """
        return self.__elements[self.__index]


# UNDIRECTEDGRAPH CLASS IMPLEMENTATION
# Internal Representation Specifications:
# We keep 2 dictionaries for efficiency in getting the edges of a vertex, and one for the cost of an edge
# The edges dictionary takes as keys the vertices and as values a list of the edges
# The costs dictionary takes as keys the edges and as values the costs

class UnDirectedGraph:

    # CLASS INITIALIZATION
    def __init__(self):
        """
        Initializes a new UnDirectedGraph Object
        """

        # Number of vertices in the Graph is initially zero
        self.__verticesCount = 0
        self.__edgesCount = 0

        # Neighbours are initially empty
        self.__edges = {}

        # Costs of the Edges of the Graphs is initially empty
        self.__costs = {}

    # CLASS DIRECTEDGRAPH GENERAL STATISTICS
    def vertices_count(self):
        """
        Returns the number of vertices inside the UnDirected Graph
        """
        return self.__verticesCount

    def edges_count(self):
        """
        Returns the number of edges inside the UnDirected Graph
        """
        return self.__edgesCount

    # CLASS DIRECTEDGRAPH PARTICULAR STATISTICS
    def degree(self, vertex: int):
        """
        Returns the neighbouring edges count
        If the Vertex is not inside the Graph, returns None
        :param vertex: Vertex to Search
        """
        vertex = self.find_vertex(vertex)
        if not vertex:
            return None

        degree = 0

        if vertex in self.__edges.keys():
            degree = len(self.__edges[vertex])

        return degree

    # CLASS DIRECTEDGRAPH STRUCTURE GETTERS
    def find_vertex(self, number: int):
        """
        Returns the vertex with the specified numberID if found, None otherwise
        :param number: Source Vertex
        """
        vertex = Vertex(number)

        if vertex in self.__edges.keys():
            return vertex
        return None

    def find_edge(self, source: int, target: int):
        """
        Returns the edge between to given vertices if found, None otherwise
        :param source: Source Vertex
        :param target: Target Vertex
        """
        source = self.find_vertex(source)
        target = self.find_vertex(target)
        edge = UEdge(source, target)

        if (not source) or (not target):
            return None

        if edge in self.__edges[source]:
            return edge
        if edge in self.__edges[target]:
            return edge
        return None

    def vertices(self):
        """
        Returns all the vertices inside the Directed Graph
        """

        vertices_list = []
        for vertex in self.__edges.keys():
            vertices_list.append(vertex)

        return vertices_list.copy()

    def get_edges(self, vertex: int):
        """
        Returns all the edges of a specified vertex inside the UnDirected Graph
        If the vertex is not inside the Graph, return None

        :param vertex: The ID number of the Vertex to analyze
        """

        vertex = self.find_vertex(vertex)
        if not vertex:
            return None

        return self.__edges[vertex].copy()

    # CLASS DIRECTEDGRAPH STRUCTURE ITERATORS
    def vertex_iterator(self):
        """
        :return: Returns an Iterator of all Vertices inside the DirectedGraph
        """
        return UnDirectedGraphVertexIterator(self)

    def edges_iterator(self, vertex: int):
        """
        :return: Returns an Iterator of all Inbound Edges of a specified vertex, inside the DirectedGraph
                 Raises DirectedGraphException if the Vertex is not inside the Graph
        """
        if not self.find_vertex(vertex):
            raise UnDirectedGraphException("Vertex not inside the DirectedGraph")

        return UnDirectedGraphEdgesIterator(self, vertex)

    # CLASS DIRECTEDGRAPH EDGE COST RELATED METHODS
    # Get / Add/ Modify a cost to an Edge
    def get_cost(self, source: int, target: int):
        """
        Gets the cost of an Edge ( specified by source and target ) and returns it
        Returns None if either the Edge is not inside the Graph or does not have a cost

        :param source: Source Vertex
        :param target: Target Vertex
        """

        edge = self.find_edge(source, target)
        if not edge:
            return None

        opposite_edge = UEdge(Vertex(target), Vertex(source))
        if (edge not in self.__costs.keys()) and (opposite_edge not in self.__costs.keys()):
            return None

        if edge not in self.__costs.keys():
            return self.__costs[opposite_edge]
        else:
            return self.__costs[edge]

    def modify_cost(self, source: int, target: int, cost: int):
        """
        Adds / Updates the cost of an Edge ( specified by source and target ) and returns it
        Returns None if either the Edge is not inside the Graph

        :param source: Source Vertex
        :param target: Target Vertex
        :param cost: New Edge Cost
        """

        edge = self.find_edge(source, target)
        if not edge:
            return None

        self.__costs[edge] = cost

        return cost

    # CLASS STRUCTURE MODIFICATION METHODS
    # Add / Remove Vertices and Edges
    def add_vertex(self, vertex_number: int):
        """
        Adds a new vertex to the DirectedGraph and returns it
        If the vertex is already inside the Graph, return None

        :param vertex_number: The ID number of the Vertex
        """
        vertex = self.find_vertex(vertex_number)
        if vertex:
            return None

        vertex = Vertex(vertex_number)
        self.__verticesCount += 1
        self.__edges[vertex] = []

        return vertex

    def remove_vertex(self, vertex_number: int):
        """
        Removes a Vertex from the DirectedGraph and returns it
        Removes by cascade all the edges having the vertex as a source or target

        If the Vertex is not inside the graph, returns None

        :param vertex_number: The Vertex ID number
        """

        # If vertex inside the graph, remove it
        # Otherwise return None
        vertex = self.find_vertex(vertex_number)
        if not vertex:
            return None

        self.__verticesCount -= 1
        for edge in self.__edges[vertex]:
            self.remove_edge(edge.source.number, edge.target.number)
        del self.__edges[vertex]

        return vertex

    def add_edge(self, source: int, target: int):
        """
        Adds a new Edge to the Directed Graph
        If either the source or target vertices not in the graph, add them

        :param source: Source Vertex
        :param target: Target Vertex
        """
        source = Vertex(source)
        target = Vertex(target)
        edge = UEdge(source, target)

        if self.find_edge(source.number, target.number):
            return None

        if target not in self.__edges.keys():
            self.add_vertex(target.number)
        if source not in self.__edges.keys():
            self.add_vertex(source.number)

        self.__edgesCount += 1
        self.__edges[source].append(edge)
        self.__edges[target].append(edge)

        return edge

    def remove_edge(self, source: int, target: int):
        """
        Removes an Edge ( specified by source and target ) from the DirectedGraph and returns it
        If the Edge is not in the Graph, return None

        :param source: Source Vertex of the Edge
        :param target: Target Vertex of the Edge
        """

        # If edge inside the graph, remove it
        # Otherwise return None
        edge = self.find_edge(source, target)

        if not edge:
            return None

        self.__edgesCount -= 1
        self.__edges[Vertex(target)].remove(edge)

        return edge.source, edge.target

    # CLASS COPY CREATION METHOD
    def copy(self):
        """
        Returns a deep copy of the current state of the DirectedGraph
        ( Creates a new DirectedGraph with the same vertices and edges )
        """

        # Graph Structure
        graph_copy = DirectedGraph()

        # Copying all vertices and edges
        for edge in self.__edges.values():
            graph_copy.add_edge(edge.source.number, edge.target.number)

        # Copying all costs
        for (edge, cost) in self.__costs:
            graph_copy.modify_cost(edge.source.number, edge.target.number, cost)

        return graph_copy
