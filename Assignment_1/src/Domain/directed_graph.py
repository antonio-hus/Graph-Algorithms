# This module contains the representation of the classes: Vertex, Edge and DirectedGraph

# VERTEX REPRESENTATION BELOW
class Vertex:

    # CLASS INITIALIZATION
    def __init__(self, number: int):
        """
        Initializes a Vertex Object having a unique ID
        :param number: The ID (Integer Number) of the Vertex
        """
        self.__number = number

    # CLASS PROPERTIES
    @property
    def number(self):
        """
        :return: The Vertex ID ( Number )
        """
        return self.__number

    # FORMATTING OPTIONS
    def __str__(self):
        """
        String Representation of a Vertex
        """
        return f"Vertex | NumID: {self.number}"

    def __eq__(self, other):
        """
        Equality condition of vertices ( Tests for equal IDs )
        """
        return self.number == other.number

    def __hash__(self):
        """
        :return: Hashed form of a Vertex ( Represented by the ID )
        """
        return self.number


# EDGE REPRESENTATION
class Edge:

    # CLASS INITIALIZATION
    def __init__(self, source_vertex: Vertex, target_vertex: Vertex):
        """
        Initializes an Edge Object having a source and a target Vertex
        :param source_vertex: The Source Vertex
        :param target_vertex: The Target Vertex
        """
        self.__source = source_vertex
        self.__target = target_vertex

    # CLASS PROPERTIES
    @property
    def source(self):
        """
        :return: The source Vertex of the Edge
        """
        return self.__source

    @property
    def target(self):
        """
        :return: The target Vertex of the Edge
        """
        return self.__target

    # FORMATTING OPTIONS
    def __str__(self):
        """
        String Representation of an Edge
        """
        return f"Edge | Source Vertex: {self.source.number} | Target Vertex: {self.target.number}"

    def __eq__(self, other):
        """
        Equality condition of edges ( Tests for equal Source and Target Vertices )
        """
        return self.source == other.source and self.target == other.target

    def __hash__(self):
        """
        :return: Hashed form of a Vertex ( Represented by the (sourceID, targetID) tuple )
        """
        return hash((self.source.number, self.target.number))


# EXCEPTION CLASS IMPLEMENTATION
class DirectedGraphException(Exception):
    """
    Custom Exception Class for the DirectedGraph
    """
    pass


# ITERATOR CLASSES FOR THE DIRECTEDGRAPH IMPLEMENTATION
class DirectedGraphVertexIterator:
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
        Otherwise raises a DirectedGraphException
        """
        if self.valid():
            self.__index += 1
        else:
            raise DirectedGraphException("Out of vertices list bounds!")

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


class DirectedGraphOutboundIterator:
    def __init__(self, graph, vertex: int):
        """
        Parses using the index the set of all inbound edges to a given vertex, from the specified DirectedGraph
        """
        self.__elements = graph.outbound_edges(vertex)
        self.__index = 0

    def first(self):
        """
        Sets the index back at the beginning of the elements list
        """
        self.__index = 0

    def next(self):
        """
        Gets the next element's index if in bounds,
        Otherwise raises a DirectedGraphException
        """
        if self.valid():
            self.__index += 1
        else:
            raise DirectedGraphException("Out of outbound edges list bounds!")

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


class DirectedGraphInboundIterator:
    def __init__(self, graph, vertex: int):
        """
        Parses using the index the set of all outbound edges from a given vertex, from the specified DirectedGraph
        """
        self.__elements = graph.inbound_edges(vertex)
        self.__index = 0

    def first(self):
        """
        Sets the index back at the beginning of the elements list
        """
        self.__index = 0

    def next(self):
        """
        Gets the next element's index if in bounds,
        Otherwise raises a DirectedGraphException
        """
        if self.valid():
            self.__index += 1
        else:
            raise DirectedGraphException("Out of inbound edges list bounds!")

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


# DIRECTEDGRAPH CLASS IMPLEMENTATION
# Internal Representation Specifications:
# We keep 3 dictionaries for efficiency in getting the inbound, outbound edges of a vertex, or cost of an edge
# The inbound/outbound edges dictionary takes as keys the vertices and as values a list of the inbound/outbound edges
# The costs dictionary takes as keys the edges and as values the costs

class DirectedGraph:

    # CLASS INITIALIZATION
    def __init__(self):
        """
        Initializes a new DirectedGraph Object
        """

        # Number of vertices in the Graph is initially zero
        self.__vertices = 0
        self.__edges = 0

        # Inbound / Outbound Neighbours are initially empty
        self.__inbound = {}
        self.__outbound = {}

        # Costs of the Edges of the Graphs is initially empty
        self.__costs = {}

    # CLASS DIRECTEDGRAPH GENERAL STATISTICS
    def vertices_count(self):
        """
        Returns the number of vertices inside the Directed Graph
        """
        return self.__vertices

    def edges_count(self):
        """
        Returns the number of edges inside the Directed Graph
        """
        return self.__edges

    # CLASS DIRECTEDGRAPH PARTICULAR STATISTICS
    def degree(self, vertex: int):
        """
        Returns the inbound, outbound edges count tuple
        If the Vertex is not inside the Graph, returns None
        :param vertex: Vertex to Search
        """
        vertex = self.find_vertex(vertex)
        if not vertex:
            return None

        inbound = 0
        outbound = 0

        if vertex in self.__inbound.keys():
            inbound = len(self.__inbound[vertex])
        if vertex in self.__outbound.keys():
            outbound = len(self.__outbound[vertex])

        return inbound, outbound

    # CLASS DIRECTEDGRAPH STRUCTURE GETTERS
    def find_vertex(self, number: int):
        """
        Returns the vertex with the specified numberID if found, None otherwise
        :param number: Source Vertex
        """
        vertex = Vertex(number)

        if vertex in self.vertices():
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
        edge = Edge(source, target)

        if (not source) or (not target):
            return None

        if edge in self.__outbound[source]:
            return edge
        return None

    def vertices(self):
        """
        Returns all the vertices inside the Directed Graph
        """

        vertices_list = []
        for vertex in self.__inbound.keys():
            vertices_list.append(vertex)

        return vertices_list.copy()

    def inbound_edges(self, vertex: int):
        """
        Returns all the inbound edges of a specified vertex inside the Directed Graph
        If the vertex is not inside the Graph, return None

        :param vertex: The ID number of the Vertex to analyze
        """

        vertex = self.find_vertex(vertex)
        if not vertex:
            return None

        return self.__inbound[vertex].copy()

    def outbound_edges(self, vertex: int):
        """
        Returns all the outbound edges of a specified vertex inside the Directed Graph
        If the vertex is not inside the Graph, return None

        :param vertex: The ID number of the Vertex to analyze
        """

        vertex = self.find_vertex(vertex)
        if not vertex:
            return None

        return self.__outbound[vertex].copy()

    # CLASS DIRECTEDGRAPH STRUCTURE ITERATORS
    def vertex_iterator(self):
        """
        :return: Returns an Iterator of all Vertices inside the DirectedGraph
        """
        return DirectedGraphVertexIterator(self)

    def outbound_iterator(self, vertex: int):
        """
        :return: Returns an Iterator of all Inbound Edges of a specified vertex, inside the DirectedGraph
                 Raises DirectedGraphException if the Vertex is not inside the Graph
        """
        if not self.find_vertex(vertex):
            raise DirectedGraphException("Vertex not inside the DirectedGraph")

        return DirectedGraphOutboundIterator(self, vertex)

    def inbound_iterator(self, vertex: int):
        """
        :return: Returns an Iterator of all Inbound Edges of a specified vertex, inside the DirectedGraph
                 Raises DirectedGraphException if the Vertex is not inside the Graph
        """
        if not self.find_vertex(vertex):
            raise DirectedGraphException("Vertex not inside the DirectedGraph")

        return DirectedGraphInboundIterator(self, vertex)

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
        if edge not in self.__costs.keys():
            return None

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
        self.__vertices += 1
        self.__inbound[vertex] = []
        self.__outbound[vertex] = []

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

        self.__vertices -= 1
        for edge in self.__inbound[vertex]:
            self.remove_edge(edge.source.number, edge.target.number)
        for edge in self.__outbound[vertex]:
            self.remove_edge(edge.source.number, edge.target.number)

        del self.__inbound[vertex]
        del self.__outbound[vertex]

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
        edge = Edge(source, target)

        if self.find_edge(source.number, target.number):
            return None

        self.__edges += 1
        if target not in self.__inbound:
            self.add_vertex(target.number)
        self.__inbound[target].append(edge)

        if source not in self.__outbound:
            self.add_vertex(source.number)
        self.__outbound[source].append(edge)

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

        self.__edges -= 1
        self.__inbound[Vertex(target)].remove(edge)
        self.__outbound[Vertex(source)].remove(edge)

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
        for edge in self.__inbound.values():
            graph_copy.add_edge(edge.source.number, edge.target.number)
        for edge in self.__outbound.values():
            graph_copy.add_edge(edge.source.number, edge.target.number)

        # Copying all costs
        for (edge, cost) in self.__costs:
            graph_copy.modify_cost(edge.source.number, edge.target.number, cost)

        return graph_copy
