# This module implements the problem 6 from practical work no. 5
#
# Requirement:
# Given a digraph with costs, find a minimum cost Hamiltonian cycle (i.e., solve the TSP)
#

# IMPORTS SECTION
from Assignment_1.src.Domain.vertex import Vertex
from Assignment_1.src.Domain.edge import Edge, UEdge
from Assignment_1.src.Domain.directed_graph import (DirectedGraph, DirectedGraphVertexIterator,
                                                      DirectedGraphInboundIterator, DirectedGraphOutboundIterator, DirectedGraphException)


# Definition Section
# Define a constant for infinity (representing unreachable nodes)
INF = 10000000000


# Solving the Traveling Salesman Problem
def travelling_salesman_problem(graph: DirectedGraph, start_vertex: Vertex):
    vertices_count = graph.vertices_count()

    # Initialize the matrix
    d = {}
    for vertex in graph.vertices():
        d[vertex] = [INF for _ in range(vertices_count)]

    # Only the start vertex is accessible with a path length of 0 and a cost of 0
    d[start_vertex][0] = 0

    # Keeping track of the parents tree
    parent = {}

    # Filling in the matrix by relaxing the edges verticesCount - 1 times
    for k in range(1, vertices_count):
        for vertex in graph.vertices():
            for neighbor_edge in graph.outbound_edges(vertex.number):
                neighbor = neighbor_edge.target
                cost = graph.get_cost(vertex.number, neighbor.number)
                if d[vertex][k - 1] + cost < d[neighbor][k]:
                    d[neighbor][k] = d[vertex][k - 1] + cost
                    parent[neighbor] = vertex

    # Check for negative cycles
    for vertex in graph.vertices():
        for neighbor_edge in graph.outbound_edges(vertex.number):
            neighbor = neighbor_edge.target
            cost = graph.get_cost(vertex.number, neighbor.number)
            if d[vertex][vertices_count - 1] + cost < d[neighbor][vertices_count - 2]:
                raise DirectedGraphException("Negative cost cycle detected!")

    # Find the minimum cost Hamiltonian cycle
    min_cost = INF
    min_cycle = None
    for vertex in graph.vertices():
        cost = d[vertex][vertices_count - 1]
        if cost < min_cost:
            min_cost = cost
            min_cycle = vertex

    # Reconstruct the minimum cost cycle
    cycle = [min_cycle]
    current_vertex = min_cycle
    while len(cycle) < vertices_count:
        current_vertex = parent[current_vertex]
        cycle.append(current_vertex)

    return cycle, min_cost