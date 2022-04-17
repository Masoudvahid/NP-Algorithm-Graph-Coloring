import tkinter as tk
from tkinter import *
import ast

###### Testing started ######

# Runtime testing
# import tests.runtime
# Functionality
import tests.testing as test
test.unittest.main(module=test)
###### Testing finished ######


"""
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

# Label for adjacency list
var = StringVar()
label = Label(window, textvariable=var)
var.set("Enter adjacency list:")
label.pack()


def get_edges():
    edges = ast.literal_eval(edge_tb.get())
    get_vertex_count()
    # Greedy algorithm
    start_time = time.time()
    greedy = gr.greedy_algorithm(number_of_nodes, edges)
    greedy.perform_greedy_algorith()
    greedy.draw_graph()
    print("--- %s seconds ---\n\n" % (time.time() - start_time))
    # Brute force algorithm
    start_time = time.time()
    brute_force = bf.brute_force(number_of_nodes, edges)
    brute_force.perform_brute_force_algorithm()
    brute_force.draw_graph()
    print("--- %s seconds ---\n\n" % (time.time() - start_time))
    get_adj_matrix()


edge_tb = tk.Entry(window, width=40)
edge_tb.pack(pady=10)

# Label for adjacency list
var = StringVar()
label = Label(window, textvariable=var)
var.set("enter adjacency matrix:")
label.pack()


def get_adj_matrix():
    adj_matrix = ast.literal_eval(adj_matrix_tb.get())
    backtrack_value = 3
    start_time = time.time()
    backtracking = bt.backtracking_algorithm(number_of_nodes, adj_matrix, backtrack_value)
    backtracking.backtracking()
    backtracking.draw_graph()
    print("--- %s seconds ---\n\n   " % (time.time() - start_time))


adj_matrix_tb = tk.Entry(window, width=40)
adj_matrix_tb.pack(pady=10)

btn = tk.Button(window, height=1, width=10, text="Read", command=get_edges)
btn.pack()

# Backtracking algorithm presentation


window.title('Graph coloring')
window.geometry("300x250+10+10")
window.mainloop()
"""
