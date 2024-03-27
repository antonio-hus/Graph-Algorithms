# This module contains the implementation of the UI, permitting the user to interact with a specified DirectedGraph

# Imports Section
# --- Domain ---
from Assignment_1.src.Domain.vertex import Vertex
from Assignment_1.src.Domain.edge import Edge
from Assignment_1.src.Domain.directed_graph import DirectedGraph
from Assignment_1.src.Domain.undirected_graph import UnDirectedGraph

# --- Services ---
from Assignment_1.src.Services.generate_services import *
from Assignment_1.src.Services.io_file_services import *
from Assignment_1.src.Services.connected_component_services import *


# UI Class Implementation
class UI:

    # CLASS INITIALIZATION
    def __init__(self, graph):
        """
        User Interface displays data and allows interactivity with a given DirectedGraph or UnDirectedGraph
        :param graph: The specified graph to analyze and modify
        """
        self.__graph = graph

    # UX OPERATIONS
    @staticmethod
    def clear_screen():
        """
        Simulates clearing the screen by printing 40 new lines
        """
        print('\n'*40)

    # USER GUIDANCE SCREENS
    @staticmethod
    def welcome_screen():
        """
        Displays a welcome screen to the user
        """
        UI.clear_screen()
        print("Welcome to my Graph Manager")
        print("Made by Hus Lucian-Antonio, Group 914/1")
        print('\n'*3)
        print("Press 'Enter' to proceed...")
        input()

    # MAIN MENU OPTIONS SCREEN
    def main_menu(self):
        """
        Option Controller for the User
        """
        UI.clear_screen()
        print("Enter the desired operation id: \n")
        print("1. Graph Statistics ( Vertices / Edges List)")
        print("2. Particular Vertex Statistics")
        print("3. Edge Operations")
        print("4. Modify the Graph Structure")
        print("5. Connected Components via DFS ( UnDirectedGraphs Only )")
        print("0. Exit")

        op = input('>')
        if op == '0':
            raise InterruptedError
        elif op == '1':
            self.graph_statistics_screen()
        elif op == '2':
            self.vertex_statistics_screen()
        elif op == '3':
            self.edge_operations_screen()
        elif op == '4':
            self.graph_modification_screen()
        elif op == '5':
            self.connected_components_screen()
        else:
            pass

    # TASK RELATED SCREENS
    def graph_statistics_screen(self):
        """
        Displays General Graph Statistics
        - No. of vertices
        - No. of edges
        - Vertices of the Graph
        """
        UI.clear_screen()

        print("Here are the statistics of your graph: \n")
        print(f"Number of vertices: {self.__graph.vertices_count()}")
        print(f"Number of edges: {self.__graph.edges_count()}")
        print()

        # Displaying the vertices of the Graph
        print("Vertices inside the graph: ")
        vertex_iter = self.__graph.vertex_iterator()
        while vertex_iter.valid():
            print(vertex_iter.getCurrent())
            vertex_iter.next()

        print('\n')
        print("Press 'Enter' to go back to Main Menu")
        input()

    def vertex_statistics_screen(self):
        """
        Displays Particular Vertex Statistics if the Vertex is in the Graph
        - Inbound / Outbound Degree
        - Inbound / Outbound Edges
        Otherwise, an error message
        """
        UI.clear_screen()

        try:

            op = int(input("Enter the number of the vertex to show details for: "))
            if not self.__graph.find_vertex(op):
                raise Exception("Vertex is not inside the graph!")

            print("Here are the statistics of your vertex: \n")
            if isinstance(self.__graph, DirectedGraph):
                inbound, outbound = self.__graph.degree(op)
                print(f"Inbound Edges: {inbound}")
                edges_iter = self.__graph.inbound_iterator(op)
                while edges_iter.valid():
                    print(edges_iter.getCurrent())
                    edges_iter.next()
                print()

                print(f"Outbound Edges: {outbound}")
                edges_iter = self.__graph.outbound_iterator(op)
                while edges_iter.valid():
                    print(edges_iter.getCurrent())
                    edges_iter.next()
                print()
            elif isinstance(self.__graph, UnDirectedGraph):
                degree = self.__graph.degree(op)
                print(f"Edges: {degree}")
                edges_iter = self.__graph.edges_iterator(op)
                while edges_iter.valid():
                    print(edges_iter.getCurrent())
                    edges_iter.next()
                print()

        except Exception as exc:
            print(f"There has been an error! {exc}")

        print("Press 'Enter' to go back to Main Menu")
        input()

    def edge_operations_screen(self):
        """
        Allows user to perform Edge Related Operations
        - Find if an Edge is inside the Graph
        - Get / Add / Modify an Edge Cost
        """
        UI.clear_screen()

        print("Choose from the set of Edge Operations: \n")
        print("1. Find if Edge exists")
        print("2. Get Edge Cost")
        print("3. Add/Modify Edge Cost")
        print("0. Back to Main Menu")
        op = input(">")
        print()

        try:

            if op == '0':
                return

            elif op == '1':

                source = int(input("The numberID of the Source Vertex: "))
                target = int(input("The numberID of the Target Vertex: "))
                edge = self.__graph.find_edge(source, target)

                if edge:
                    print("Edge is in the Graph!")
                    print(edge)
                else:
                    print("Edge does not Exist inside the Graph!")
                print()

            elif op == '2':

                source = int(input("The numberID of the Source Vertex: "))
                target = int(input("The numberID of the Target Vertex: "))
                cost = self.__graph.get_cost(source, target)
                edge = self.__graph.find_edge(source, target)

                # Edge exists and has a Cost
                if cost:
                    print(f"The cost of the specified edge is: {cost}")

                # Edge exists but does not have a Cost
                elif edge:
                    print("Edge does not have an associated Cost!")

                # Edge not inside the Graph
                else:
                    raise Exception("Edge is not inside the Graph")

            elif op == '3':

                source = int(input("The numberID of the Source Vertex: "))
                target = int(input("The numberID of the Target Vertex: "))
                edge = self.__graph.find_edge(source, target)
                cost = self.__graph.get_cost(source, target)

                # Edge exists and has a cost => Modify Cost
                if cost:
                    print(f"The cost of the selected edge is: {cost}")
                    new_cost = int(input("Enter the new cost of the edge: "))
                    self.__graph.modify_cost(source, target, new_cost)

                # Edge exists but has no cost => Add Cost
                elif edge:
                    print("The selected edge does not have a cost")
                    new_cost = int(input("Enter the new cost of the edge: "))
                    self.__graph.modify_cost(source, target, new_cost)

                # Edge not in the Graph
                else:
                    raise Exception("Edge not in the Graph!")

            else:
                raise Exception("Invalid Operation ID")

        except Exception as exc:
            print(f"There has been an error with the operation! {exc}")

        print("Press 'Enter' to go back to Main Menu")
        input()

    def graph_modification_screen(self):
        """
        Allows the user to perform modifications to the structure of a graph
        - Add / Remove a Vertex
        - Add / Remove an Edge
        """
        UI.clear_screen()
        print("How should we modify the Graph: \n")
        print("1. Add a new Vertex")
        print("2. Remove a Vertex")
        print("3. Add a new Edge")
        print("4. Remove an Edge")
        print("0. Back to Main Menu")

        op = input('>')
        print()
        if op == '0':
            return
        elif op == '1':
            try:
                vertex_number = int(input("Enter a number for the vertex to add: "))
                if self.__graph.add_vertex(vertex_number):
                    print("Operation successful! The new vertex was added")
                else:
                    print("Operation Failed! Vertex already in the Graph")
            except ValueError:
                print("Operation Failed! Vertex was not added")
        elif op == '2':
            try:
                vertex_number = int(input("Enter the number of the vertex to remove: "))
                if self.__graph.remove_vertex(vertex_number):
                    print("Operation successful! The vertex was removed")
                else:
                    print("Operation Failed! Vertex not in the Graph")
            except Exception as exc:
                print(f"Operation Failed! {exc}")
        elif op == '3':
            try:
                print("Now enter the edge's details: ")
                source_vertex = int(input("Enter the number of the source vertex: "))
                target_vertex = int(input("Enter the number of the target vertex: "))
                if self.__graph.add_edge(source_vertex, target_vertex):
                    print("Operation successful! The edge was added")
                else:
                    print("Operation Failed! Edge already in the Graph")
            except Exception as exc:
                print(f"Operation Failed! {exc}")
        elif op == '4':
            try:
                print("Now enter the edge's details: ")
                source_vertex = int(input("Enter the number of the source vertex: "))
                target_vertex = int(input("Enter the number of the target vertex: "))
                if self.__graph.remove_edge(source_vertex, target_vertex):
                    print("Operation successful! The edge was removed")
                else:
                    print("Operation Failed! Edge not in the Graph")
            except Exception as exc:
                print(f"Operation Failed! {exc}")
        else:
            print("Operation Failed! Invalid Operation ID")

        print("Press 'Enter' to go back to Main Menu")
        input()

    def connected_components_screen(self):
        UI.clear_screen()
        print("Here is the list of all connected components")

        k = 0
        for component in connected_components(self.__graph):
            k += 1
            print(f"Component {k}: ")
            for vertex in component:
                print(vertex, end=" ")
            print()
            print("-------------------------")

        print()
        print("Press 'Enter' to go back to Main Menu")
        input()
