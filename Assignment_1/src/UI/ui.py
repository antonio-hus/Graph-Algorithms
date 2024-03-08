from Assignment_1.src.Domain.directed_graph import DirectedGraph


class UI:

    def __init__(self, graph: DirectedGraph):
        self.__graph = graph

    @staticmethod
    def clear_screen():
        """
        Simulates clearing the screen by printing 40 new lines
        """
        print('\n'*40)

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
        print("0. Exit")

        op = input('>')
        if op == '0':
            raise InterruptedError
        elif op == '1':
            self.graph_statistics_screen()
        else:
            pass

    def graph_statistics_screen(self):
        UI.clear_screen()
        print("Here are the statistics of your graph: \n")
        print(f"Number of vertices: {self.__graph.vertices_count()}")
        print(f"Number of edges: {self.__graph.edges_count()}")
        print('\n')

        print("Press 'Enter' to go back to Main Menu")
        input()


