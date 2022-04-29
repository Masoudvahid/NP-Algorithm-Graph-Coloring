import sys
from timeit import default_timer as time
import algorithms.greedy as gr
import algorithms.backtracking as bt
import algorithms.brute_force as bf


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

    adjacency_matrix_input = [
        [[0, 1, 1, 0, 0, 0, 1],
         [1, 0, 1, 1, 0, 0, 0],
         [1, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 0, 0],
         [0, 0, 1, 1, 0, 1, 0],
         [0, 0, 0, 0, 1, 0, 0],
         [1, 0, 0, 0, 0, 0, 0]],
        [[0, 1, 0, 0, 1, 1],
         [1, 0, 0, 1, 1, 0],
         [0, 0, 0, 1, 1, 0],
         [0, 1, 1, 0, 0, 0],
         [1, 1, 1, 0, 0, 1],
         [1, 0, 0, 0, 1, 0]],
        [[0, 1, 0, 1],
         [1, 0, 1, 0],
         [0, 1, 0, 1],
         [1, 0, 1, 0]]
    ]

    # """
    # Greedy algorithm presentation
    print("Greedy algorithm presentation\n")
    for index, edges in enumerate(adjacency_list_input):
        start_time = time()
        greedy = gr.greedy_algorithm(number_of_nodes[index], edges)
        greedy.perform_greedy_algorith()
        print(f"--- %s seconds for {number_of_nodes[index]} elements ---\n" % (time() - start_time))
    # """
    print("\n")
    # """
    # Backtracking algorithm presentation
    print("Backtracking algorithm presentation\n")
    backtrack_value = 3
    for index, edges in enumerate(adjacency_list_input):
        start_time = time()
        backtracking = bt.backtracking_algorithm(number_of_nodes[index], edges, backtrack_value)
        backtracking.backtracking()
        print(f"--- %s seconds for {number_of_nodes[index]} elements ---\n" % (time() - start_time))
    # """
    print("\n")
    # """
    # Brute force method client code
    print("Brute force method presentation\n")
    for index, edges in enumerate(adjacency_list_input):
        start_time = time()
        brute_force = bf.brute_force(number_of_nodes[index], edges)
        brute_force.perform_brute_force_algorithm()
        print(f"--- {(time() - start_time)} seconds for {number_of_nodes[index]} elements ---\n")
    # """
