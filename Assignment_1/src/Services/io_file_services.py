# This module contains the functionality for reading / saving a DirectedGraph from/to file

# Imports Section
# --- Domain ---
from Assignment_1.src.Domain.directed_graph import DirectedGraph, DirectedGraphException


# FILE READING OPERATION IMPLEMENTATION
def read_graph(graph: DirectedGraph, file_path):
    """
    Adds to the specified DirectedGraph the data ( vertices, edges and costs ) read from the file at file_path
    Raises Exception for an invalid file_path or any other file reading related issues

    :param graph: The Graph to append data to
    :param file_path: The file path of the file to read from
    """
    try:
        with open(file_path, 'r') as file:
            file.readline()
            for line in file.readlines():
                source, target, cost = map(int, line.strip().split())
                graph.add_edge(source, target)
                graph.modify_cost(source, target, cost)

    except Exception as exc:
        raise DirectedGraphException("Encountered problems when reading from the file! Operation Aborted!")


# FILE SAVING OPERATION IMPLEMENTATION
def save_graph(graph: DirectedGraph, file_path):
    """
    Saves in the file at the specified file_path the data of the DirectedGraph ( vertices, edges and costs )
    Raises Exception for an invalid file_path or any other file writing related issues

    :param graph: The Graph to save data from
    :param file_path: The file path of the file to save to
    """
    try:
        with open(file_path, 'w') as file:
            content = ""
            content += f"{graph.vertices_count()} {graph.edges_count()}\n"
            vertex_iterator = graph.vertex_iterator()
            while vertex_iterator.valid():
                vertex = vertex_iterator.getCurrent()

                # Printing for each vertex only one set of edges ( Inbound / Outbound ) to avoid duplicates
                # Inbound Edges
                inbound_iterator = graph.inbound_iterator(vertex.number)
                while inbound_iterator.valid():
                    edge = inbound_iterator.getCurrent()
                    content += f"{edge.source.number} {edge.target.number} {graph.get_cost(edge.source.number, edge.target.number)}\n"
                    inbound_iterator.next()

                # Getting the next vertex
                vertex_iterator.next()

            file.write(content)

    except Exception as exc:
        raise DirectedGraphException("Encountered problems when writing to the file! Operation Aborted!")
