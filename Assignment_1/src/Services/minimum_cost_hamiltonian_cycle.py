# This module implements the problem 6 from practical work no. 5
#
# Requirement:
# Given a digraph with costs, find a minimum cost Hamiltonian cycle (i.e., solve the TSP)
#

# IMPORTS SECTION
from itertools import combinations
from Assignment_1.src.Domain.vertex import Vertex
from Assignment_1.src.Domain.edge import Edge, UEdge
from Assignment_1.src.Domain.directed_graph import (DirectedGraph, DirectedGraphVertexIterator,
                                                      DirectedGraphInboundIterator, DirectedGraphOutboundIterator, DirectedGraphException)


# Definition Section
# Define a constant for infinity (representing unreachable nodes)
INF = 10000000000

# TSP - Travelling Salesman Problem
# Given a list of cities and the distances between each pair of cities,
# what is the shortest possible route that visits each city exactly once and returns to the origin city?

# NOTE:
# frozenset() is used instead of set, due to the ease of excluding elements from its set, and being immutable


# Solving the Traveling Salesman Problem
def travelling_salesman_problem(graph: DirectedGraph, start_vertex: int):

    # Vertices
    n = graph.vertices_count()
    vertices = [vertex.number for vertex in graph.vertices()]
    vertices = frozenset(vertices)

    # Initialize g dictionary to store the minimum costs
    g = {}

    # Initialize parent dictionary to store the parents
    parent = {}

    # Calculate costs for sets of size 0 (base case)
    for k in vertices-{start_vertex}:
        g[(frozenset([k]), k)] = graph.get_cost(start_vertex, k)
        parent[(frozenset([k]), k)] = start_vertex

    # Iterate over all set sizes
    for size in range(2, n):

        # Iterate over all subsets of size s
        for include_set in combinations(vertices-{start_vertex}, size):
            include_set = frozenset(include_set)

            for vertex in include_set:

                # Initialize minimum cost and best predecessor
                min_cost = INF
                best_previous_vertex = None

                # Find minimum cost of reaching the vertex from include_set
                for previous_vertex in include_set:
                    if vertex != previous_vertex:
                        cost = g.get((include_set-{vertex}, previous_vertex)) + graph.get_cost(previous_vertex, vertex)
                        if cost < min_cost:
                            min_cost = cost
                            best_previous_vertex = previous_vertex
                g[(include_set, vertex)] = min_cost
                parent[(include_set, vertex)] = best_previous_vertex

    # Find the minimum cost Hamiltonian cycle
    min_cost = INF
    best_end_vertex = None
    for vertex in vertices:
        if vertex != start_vertex:
            cost = g.get((frozenset(vertices) - {start_vertex}, vertex), INF) + graph.get_cost(vertex, start_vertex)
            if cost < min_cost:
                min_cost = cost
                best_end_vertex = vertex

    # Rebuilding the path
    path = [start_vertex, best_end_vertex]
    include_set = frozenset(vertices) - {start_vertex}
    while len(include_set) > 0:
        vertex = parent.get((include_set, best_end_vertex))
        if vertex is None:
            return INF, None
        path.append(vertex)
        include_set -= {best_end_vertex}
        best_end_vertex = vertex
    path.reverse()

    # Returning the result
    return min_cost, path


