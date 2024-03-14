# This module contains the implementation of a Random Value Generator for Vertices and Edges inside a DirectedGraph

# Imports Section
# --- Domain ---
from Assignment_1.src.Domain.directed_graph import DirectedGraph
# --- Misc ---
from random import randint


# GRAPH GENERATOR IMPLEMENTATION
def generate_graph(vertices_count: int, edges_count: int) -> DirectedGraph:
    """
    Creates and returns a DirectedGraph having a given number of vertices and edges.
    - Creates random vertices
    - Creates random edges
    - Assigns random costs to these edges

    Raises DirectedGraphException for negative value of vertices_count or edges_count

    :param vertices_count: The number of vertices to add
    :param edges_count: The number of edges to add
    """
    pass
