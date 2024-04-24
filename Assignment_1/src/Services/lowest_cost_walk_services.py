# This module contains the functionality for getting the lowest cost walk between two vertices on a graph
#
# Requirement:
# Write a program that, given a graph with costs and two vertices, finds a lowest cost walk between the given vertices
# or prints a message if there are negative cost cycles accessible from the starting vertex.
# The program will use a matrix defined as d[x,k]=the cost of the lowest cost walk from s to x and of length equal to k
# where s is the starting vertex.
#

# Includes Section
from Assignment_1.src.Domain.vertex import Vertex
from Assignment_1.src.Domain.edge import Edge, UEdge
from Assignment_1.src.Domain.directed_graph import (DirectedGraph, DirectedGraphVertexIterator,
                                                      DirectedGraphInboundIterator, DirectedGraphOutboundIterator, DirectedGraphException)


# Definition Section
# Define a constant for infinity (representing unreachable nodes)
INF = 10000000000


# Implementation of the Algorithm
def get_minpath(graph: DirectedGraph, source: Vertex, target: Vertex):

    # Initialize the matrix to store the minimum cost walks
    verticesCount = graph.vertices_count()

    # Initializing the matrix
    d = {}
    for vertex in graph.vertices():
        d[vertex] = ([INF for _ in range(0, verticesCount)])

    # Only the source is accessible with a path length of 0 and a cost of 0
    d[source][0] = 0

    # Keeping track of the parents tree
    parent = {}

    # Filling in the matrix by relaxing the edges verticesCount - 1 times
    for k in range(0, verticesCount):
        for vertex in graph.vertices():
            for neighbor_edge in graph.outbound_edges(vertex.number):
                neighbor = neighbor_edge.target
                cost = graph.get_cost(vertex.number, neighbor.number)
                if d[vertex][k - 1] + cost < d[neighbor][k]:
                    d[neighbor][k] = d[vertex][k - 1] + cost
                    parent[neighbor] = vertex

    # Check for negative cycles
    # If we have another edge that can be reduced, we are dealing with a negative cycle
    for vertex in graph.vertices():
        for neighbor_edge in graph.outbound_edges(vertex.number):
            neighbor = neighbor_edge.target
            cost = graph.get_cost(vertex.number, neighbor.number)
            if d[vertex][verticesCount-1] + cost < d[neighbor][verticesCount-2]:
                raise DirectedGraphException("Negative cost cycle detected!")

    # Rebuilding the minimum cost path and final cost
    path = [target]
    cost = 0
    while target != source:

        # Getting the cost from source to target
        cost += graph.get_cost(parent[target].number, target.number)

        # Getting the parent of the vertex
        target = parent[target]

        # Appending the new vertex
        path.append(target)

    # Reversing the list to get the source -> target order in place
    path.reverse()
    return path, cost
