# This module implements the problem 6 from practical work no. 4
#
# Requirement:
# Write a program that, given an undirected connected graph,
# constructs a minimal spanning tree using the Prim's algorithm.
#

# IMPORTS SECTION
import heapq
from Assignment_1.src.Domain.vertex import Vertex
from Assignment_1.src.Domain.edge import Edge, UEdge
from Assignment_1.src.Domain.undirected_graph import (UnDirectedGraph, UnDirectedGraphVertexIterator,
                                                      UnDirectedGraphEdgesIterator, UnDirectedGraphException)


# PRIM'S ALGORITHM IMPLEMENTATION
def prim_minimum_spanning_tree(graph: UnDirectedGraph):

    # Initialize variables
    q = []
    edges = set()
    vertices = set()
    parent = {}
    dist = {}

    # Pick start vertex arbitrary
    start_vertex = graph.vertices()[0]
    vertices.add(start_vertex)

    iterator = graph.edges_iterator(start_vertex.number)
    while iterator.valid():

        # Getting the next vertex
        edge = iterator.getCurrent()
        if start_vertex != edge.target:
            new_vertex = edge.target
        else:
            new_vertex = edge.source

        # Processing the new vertex
        dist[new_vertex] = graph.get_cost(new_vertex.number, start_vertex.number)
        parent[new_vertex] = start_vertex
        heapq.heappush(q, (dist[new_vertex], new_vertex))

        iterator.next()

    while q:
        vertex = heapq.heappop(q)[1]
        if vertex not in vertices:
            edges.add((vertex, parent[vertex], graph.get_cost(vertex.number, parent[vertex].number)))
            vertices.add(vertex)

            iterator = graph.edges_iterator(vertex.number)
            while iterator.valid():

                # Getting the next vertex
                edge = iterator.getCurrent()
                if vertex != edge.target:
                    new_vertex = edge.target
                else:
                    new_vertex = edge.source

                if new_vertex not in dist.keys() or graph.get_cost(vertex.number, new_vertex.number) < dist[new_vertex]:
                    dist[new_vertex] = graph.get_cost(vertex.number, new_vertex.number)
                    heapq.heappush(q, (dist[new_vertex], new_vertex))
                    parent[new_vertex] = vertex

                iterator.next()

    # Returning the edges used in the resulting tree
    return edges

