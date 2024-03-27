# This module contains the functionality for getting the Connected Components of an Undirected Graph
# Includes Section
from Assignment_1.src.Domain.vertex import Vertex
from Assignment_1.src.Domain.edge import Edge, UEdge
from Assignment_1.src.Domain.undirected_graph import (UnDirectedGraph, UnDirectedGraphVertexIterator,
                                                      UnDirectedGraphEdgesIterator, UnDirectedGraphException)


# DEPTH FIRST SEARCH ALGORITHM
def depth_first_search(graph, vertex, visited, component):
    """
    Perform depth-first search in the given graph
    Starts from the given vertex
    Adds the visited vertices to the connected component.
    """

    # Adding the new vertex to the given component and visit it
    visited.add(vertex)
    component.append(vertex.number)

    # Iterating all neighbouring edges
    iterator = graph.edges_iterator(vertex.number)
    while iterator.valid():

        # Getting the next vertex
        edge = iterator.getCurrent()
        if vertex != edge.target:
            new_vertex = edge.target
        else:
            new_vertex = edge.source

        # Going in depth for the new vertex
        if new_vertex not in visited:
            depth_first_search(graph, new_vertex, visited, component)

        iterator.next()


# CONNECTED COMPONENTS GETTER
def connected_components(graph: UnDirectedGraph):
    """
    Returns the list of all connected components inside an UnDirectedGraph
    :param graph: The given Graph
    """

    # Set of visited vertices
    visited = set()

    # List of connected components
    components = []

    # Getting the components of all currently not visited vertices
    iterator = graph.vertex_iterator()
    while iterator.valid():

        vertex = iterator.getCurrent()
        if vertex not in visited:

            # Getting all connected vertices
            component = []
            depth_first_search(graph, vertex, visited, component)
            components.append(component)

        iterator.next()

    return components
