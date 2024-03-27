# This module contains the representation of the class Edge
# Imports Section
from .vertex import Vertex

# EDGE FOR DIRECTEDGRAPH REPRESENTATION
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


# EDGE REPRESENTATION FOR UNDIRECTED GRAPH
class UEdge(Edge):
    def __eq__(self, other):
        """
        Equality condition of edges ( Tests for equal Source and Target Vertices )
        """
        return (self.source == other.source and self.target == other.target) or (self.source == other.target and self.target == other.source)

    def __hash__(self):
        """
        :return: Hashed form of a Vertex ( Represented by the (sourceID, targetID) tuple )
        """
        return hash((self.source.number, self.target.number))