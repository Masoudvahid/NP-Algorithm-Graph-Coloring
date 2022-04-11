import tkinter as tk
from tkinter import *
import ast
from struct import pack, unpack

import algorithms.greedy as gr
import algorithms.backtracking as bt

window = tk.Tk()

# Greedy algorithm

# Label for number of nodes
var = StringVar()
label = Label(window, textvariable=var)
var.set("Number of nodes:")
label.pack()


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
    greedy = gr.greedy_algorithm(number_of_nodes, edges)
    greedy.perform_greedy_algorith()
    greedy.draw_graph()
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
    backtracking = bt.backtracking_algorithm(number_of_nodes, adj_matrix, backtrack_value)
    backtracking.backtracking()
    backtracking.draw_graph()


adj_matrix_tb = tk.Entry(window, width=40)
adj_matrix_tb.pack(pady=10)

btn = tk.Button(window, height=1, width=10, text="Read", command=get_edges)
btn.pack()

# Backtracking algorithm presentation


window.title('Graph coloring')
window.geometry("300x250+10+10")
window.mainloop()

"""# Greedy algorithm presentation
# number_of_nodes = 6
# edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]
greedy = gr.greedy_algorithm(number_of_nodes, edges)
greedy.perform_greedy_algorith()
greedy.draw_graph()

# Backtracking algorithm presentation
number_of_nodes = 6
adj_matrix = [[0, 1, 0, 0, 1, 1],
              [1, 0, 0, 1, 1, 0],
              [0, 0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0, 0],
              [1, 1, 1, 0, 0, 1],
              [1, 0, 0, 0, 1, 0]]
backtrack_value = 3
backtracking = bt.backtracking_algorithm(number_of_nodes, adj_matrix, backtrack_value)
backtracking.backtracking()
backtracking.draw_graph()"""
