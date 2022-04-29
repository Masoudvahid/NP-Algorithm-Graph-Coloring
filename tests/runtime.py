import sys
from timeit import default_timer as time
import algorithms.greedy as gr
import algorithms.backtracking as bt
import algorithms.brute_force as bf
import matplotlib.pyplot as plt


def plot_runtime_graph(number_of_nodes, brute_force_runtime, greedy_runtime, back_tracking_runtime):
    # Number of nodes on the x_axis
    x = number_of_nodes
    plt.plot(x, brute_force_runtime)
    plt.plot(x, greedy_runtime)
    plt.plot(x, back_tracking_runtime, linestyle=':')
    plt.legend(["brute_force", "greedy", "back_tracking"])
    plt.show()


def perform_runtime_test():
    file_path = r'../tests/output.txt'
    sys.stdout = open(file_path, "w")

    number_of_nodes = [7, 6, 4]
    adjacency_list_input = [
        [(0, 1), (0, 2), (0, 6), (1, 2), (1, 3), (2, 4), (3, 4), (4, 5)],
        [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)],
        [(0, 1), (0, 3), (1, 2), (2, 3)],
        # [(0, 4), (0, 8), (1, 2), (1, 3), (1, 7), (3, 7), (4, 6), (5, 6), (6, 7)]
    ]

    brute_force_runtime = list()
    greedy_runtime = list()
    back_tracking_runtime = list()

    # Brute force method client code
    print("Brute force method presentation\n")
    for index, edges in enumerate(adjacency_list_input):
        start_time = time()
        brute_force = bf.brute_force(number_of_nodes[index], edges)
        brute_force.perform_brute_force_algorithm(for_test=1)
        elapsed_time = time() - start_time
        brute_force_runtime.append(elapsed_time)
        print(f"--- %s seconds for {number_of_nodes[index]} elements ---\n" % elapsed_time)
    print("\n")
    # Greedy algorithm presentation
    print("Greedy algorithm presentation\n")
    for index, edges in enumerate(adjacency_list_input):
        start_time = time()
        greedy = gr.greedy_algorithm(number_of_nodes[index], edges)
        greedy.perform_greedy_algorith(for_test=1)
        elapsed_time = time() - start_time
        greedy_runtime.append(elapsed_time)
        print(f"--- %s seconds for {number_of_nodes[index]} elements ---\n" % elapsed_time)
    print("\n")
    # Backtracking algorithm presentation
    print("Backtracking algorithm presentation\n")
    backtrack_value = 3
    for index, edges in enumerate(adjacency_list_input):
        start_time = time()
        backtracking = bt.backtracking_algorithm(number_of_nodes[index], edges, backtrack_value)
        backtracking.backtracking(for_test=1)
        elapsed_time = time() - start_time
        back_tracking_runtime.append(elapsed_time)
        print(f"--- %s seconds for {number_of_nodes[index]} elements ---\n" % elapsed_time)

    plot_runtime_graph(number_of_nodes, brute_force_runtime, greedy_runtime, back_tracking_runtime)
