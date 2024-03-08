# Import Section
from Assignment_1.src.Domain.directed_graph import DirectedGraph, DirectedGraphException
from Assignment_1.src.Services.generate_services import *
from Assignment_1.src.Services.io_file_services import *
from Assignment_1.src.UI.ui import UI


# Program Flow Controller
def start():

    # Object Initialization
    graph = DirectedGraph()
    display = UI(graph)

    # Controller
    display.welcome_screen()
    while True:
        try:
            display.main_menu()
        except InterruptedError:
            break


if __name__ == "__main__":
    start()
