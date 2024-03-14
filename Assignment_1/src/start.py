# This is the main module of the program

# Import Section
# --- Domain ---
from Assignment_1.src.Domain.directed_graph import DirectedGraph, DirectedGraphException
# --- Services
from Assignment_1.src.Services.generate_services import *
from Assignment_1.src.Services.io_file_services import *
# --- UI ---
from Assignment_1.src.UI.ui import UI


# PROGRAM STARTUP
def start():

    # OBJECT INITIALIZATION
    graph = DirectedGraph()
    display = UI(graph)

    # GENERATE RANDOM GRAPH DATA
    # Uncomment the function to get random graph data at program startup
    # random_graph1 = generate_graph(7, 20)
    # random_graph2 generate_graph(6, 40)
    # Uncomment the save to file to save the random graphs to their files
    # save_graph(random_graph1, "../random_graph1.txt")
    # save_graph(random_graph2, "../random_graph2.txt")

    # GET GRAPH DATA FROM FILES
    # Uncomment the functions with the appropriate file_path to read from
    # read_graph(graph, "../graph1k.txt")
    # read_graph(graph, "../graph10k.txt")
    # read_graph(graph, "../graph100k.txt")
    # read_graph(graph, "../graph1m.txt")

    # SAVE GRAPH DATA TO FILES
    # Uncomment the functions with the appropriate file_path to save to
    # save_graph(graph, "../graph1k_modif.txt")
    # save_graph(graph, "../graph10k_modif.txt")
    # save_graph(graph, "../graph100k_modif.txt")
    # save_graph(graph, "../graph1m_modif.txt")

    # UI CONTROLLER
    display.welcome_screen()
    while True:
        try:
            display.main_menu()
        except InterruptedError:
            break


# RUN FROM THE CURRENT FILE
if __name__ == "__main__":
    start()
