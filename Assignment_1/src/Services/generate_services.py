# This module contains the implementation of a Random Value Generator for Vertices and Edges inside a DirectedGraph

# Imports Section
# --- Domain ---
from Assignment_1.src.Domain.directed_graph import DirectedGraph, DirectedGraphException
from Assignment_1.src.Domain.undirected_graph import UnDirectedGraph, UnDirectedGraphException
# --- Misc ---
from random import randint


# GRAPH GENERATOR IMPLEMENTATION
def generate_graph(vertices_count: int, edges_count: int):
    """
    Creates and returns a DirectedGraph having a given number of vertices and edges.
    - Creates random vertices
    - Creates random edges
    - Assigns random costs to these edges

    Raises DirectedGraphException for negative value of vertices_count or edges_count
    Raises DirectedGraphException - invalid vertices / edges configurations ( too many edges )
    Otherwise, returns the generated graph

    :param vertices_count: The number of vertices to add
    :param edges_count: The number of edges to add
    """

    graph = DirectedGraph()
    # graph = UnDirectedGraph()

    if vertices_count < 0 or edges_count < 0:
        if isinstance(graph, DirectedGraph):
            raise DirectedGraphException("Vertices or edges count cannot be negative")
        elif isinstance(graph, UnDirectedGraph):
            raise UnDirectedGraphException("Vertices or edges count cannot be negative")

    if edges_count > vertices_count * (vertices_count - 1):
        if isinstance(graph, DirectedGraph):
            raise DirectedGraphException("Invalid Graph. Maximum number of edges is no.vertices * (no.vertices - 1)")
        elif isinstance(graph, UnDirectedGraph):
            raise UnDirectedGraphException("Invalid Graph. Maximum number of edges is no.vertices * (no.vertices - 1)")

    # Adding the Vertices numbered 1...n
    for i in range(1, vertices_count+1):
        graph.add_vertex(1)

    # Adding random Edges
    added_edges = 0
    while added_edges < edges_count:
        source_vertex = randint(1, vertices_count)
        target_vertex = randint(1, vertices_count)
        if source_vertex != target_vertex and not graph.find_edge(source_vertex, target_vertex):
            graph.add_edge(source_vertex, target_vertex)
            graph.modify_cost(source_vertex, target_vertex, randint(-100, 100))
            added_edges += 1

    return graph
