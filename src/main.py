import random
import tkinter as tk
from tkinter import *
import ast
import networkx as nx

from tests.program_testing import *

perform_tests(runtime=0, unittest=0)

# """
window = tk.Tk()

# Label for number of nodes
var = StringVar()
label = Label(window, textvariable=var)
var.set("Number of nodes:")
label.pack()
number_of_nodes = None


def get_vertex_count():
    global number_of_nodes
    number_of_nodes = int(vertex_count_tb.get())


vertex_count_tb = tk.Entry(window, width=40)
vertex_count_tb.pack(pady=10)

# Label for adjacency vector
var = StringVar()
label = Label(window, textvariable=var)
var.set("adjacency vector:")
label.pack()


def get_edges():
    global number_of_nodes
    if vertex_count_tb.get() == "":
        # Generate graph if no graph was provided
        number_of_nodes = random.choice(range(3, 7))
        connect_edges_probability = 0.5
        graph = nx.gnp_random_graph(number_of_nodes, connect_edges_probability)
        edges = list(graph.edges)
        print(number_of_nodes)
        print(edges)
        print(type(edges))

    else:
        # Consider the input as graph
        edges = ast.literal_eval(edge_tb.get())
        get_vertex_count()
        print(number_of_nodes)
        print(edges)
        print(type(edges))

    # Greedy algorithm
    start_time = time()
    greedy = gr.greedy_algorithm(number_of_nodes, edges)
    greedy.perform_greedy_algorith()
    greedy.draw_graph()
    print("--- %s seconds ---\n\n" % (time() - start_time))
    # Brute force algorithm
    start_time = time()
    brute_force = bf.brute_force(number_of_nodes, edges)
    brute_force.perform_brute_force_algorithm()
    brute_force.draw_graph()
    print("--- %s seconds ---\n\n" % (time() - start_time))
    # back_tracking algorithm
    backtrack_value = 3
    start_time = time()
    backtracking = bt.backtracking_algorithm(number_of_nodes, edges, backtrack_value)
    backtracking.backtracking()
    backtracking.draw_graph()
    print("--- %s seconds ---\n\n   " % (time() - start_time))


edge_tb = tk.Entry(window, width=40)
edge_tb.pack(pady=10)

btn = tk.Button(window, height=1, width=10, text="Read", command=get_edges)
btn.pack()

# Backtracking algorithm presentation
window.title('Graph coloring')
window.geometry("300x250+10+10")
window.mainloop()
# """
