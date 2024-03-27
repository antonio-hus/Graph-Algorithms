# This module contains the functionality for reading / saving a DirectedGraph from/to file

# Imports Section
# --- Domain ---
from Assignment_1.src.Domain.vertex import Vertex
from Assignment_1.src.Domain.edge import Edge
from Assignment_1.src.Domain.directed_graph import DirectedGraph, DirectedGraphException
from Assignment_1.src.Domain.undirected_graph import UnDirectedGraph, UnDirectedGraphException


# FILE READING OPERATION IMPLEMENTATION
def read_graph(graph, file_path):
    """
    Adds to the specified Graph the data ( vertices, edges and costs ) read from the file at file_path
    Raises Exception for an invalid file_path or any other file reading related issues

    :param graph: The Graph to append data to
    :param file_path: The file path of the file to read from
    """
    try:
        with open(file_path, 'r') as file:
            file.readline()
            k = 0
            for line in file.readlines():
                print(k)
                k += 1
                source, target, cost = map(int, line.strip().split())
                graph.add_edge(source, target)
                graph.modify_cost(source, target, cost)

    except Exception as exc:
        if isinstance(graph, DirectedGraph):
            raise DirectedGraphException(f"Encountered problems when reading from the file! Operation Aborted! {exc}")
        elif isinstance(graph, UnDirectedGraph):
            raise UnDirectedGraphException(f"Encountered problems when reading from the file! Operation Aborted! {exc}")


# FILE SAVING OPERATION IMPLEMENTATION
def save_graph(graph, file_path):
    """
    Saves in the file at the specified file_path the data of the Graph ( vertices, edges and costs )
    Raises Exception for an invalid file_path or any other file writing related issues

    :param graph: The Graph to save data from
    :param file_path: The file path of the file to save to
    """
    try:
        with open(file_path, 'w') as file:
            content = ""
            content += f"{graph.vertices_count()} {graph.edges_count()}\n"

            # Keeping track of the visited edges to avoid duplicates
            visited_edges = set()

            vertex_iterator = graph.vertex_iterator()
            while vertex_iterator.valid():
                vertex = vertex_iterator.getCurrent()

                if isinstance(graph, DirectedGraph):
                    # Printing for each vertex only one set of edges ( Inbound / Outbound ) to avoid duplicates
                    # Inbound Edges
                    inbound_iterator = graph.inbound_iterator(vertex.number)
                    while inbound_iterator.valid():
                        edge = inbound_iterator.getCurrent()
                        content += f"{edge.source.number} {edge.target.number} {graph.get_cost(edge.source.number, edge.target.number)}\n"
                        inbound_iterator.next()
                elif isinstance(graph, UnDirectedGraph):
                    # Printing for each vertex the set of edges

                    iterator = graph.edges_iterator(vertex.number)
                    while iterator.valid():
                        edge = iterator.getCurrent()
                        cost = graph.get_cost(edge.source.number, edge.target.number)
                        if cost is None:
                            cost = 0

                        # Convert Edge objects to tuples for comparison
                        edge_tuple = (edge.source.number, edge.target.number)
                        reverse_edge_tuple = (edge.target.number, edge.source.number)

                        # Check if the edge or its reverse has already been visited
                        if (edge_tuple not in visited_edges) and (reverse_edge_tuple not in visited_edges):
                            visited_edges.add(edge_tuple)
                            content += f"{edge.source.number} {edge.target.number} {cost}\n"

                        iterator.next()

                # Getting the next vertex
                vertex_iterator.next()

            file.write(content)

    except Exception as exc:
        if isinstance(graph, DirectedGraph):
            raise DirectedGraphException(f"Encountered problems when writing to the file! Operation Aborted! {exc}")
        elif isinstance(graph, UnDirectedGraph):
            raise UnDirectedGraphException(f"Encountered problems when writing to the file! Operation Aborted! {exc}")
