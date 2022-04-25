import unittest
import algorithms.brute_force as bf
import algorithms.backtracking as bc
import algorithms.greedy as gr

number_of_nodes = 6
edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]
adj_matrix = [[0, 1, 0, 0, 1, 1],
              [1, 0, 0, 1, 1, 0],
              [0, 0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0, 0],
              [1, 1, 1, 0, 0, 1],
              [1, 0, 0, 0, 1, 0]]
FAILURE = 'Incorrect result'


class graph_coloring_Tests(unittest.TestCase):
    def setUp(self):
        self.brute_force = bf.brute_force
        self.backtracking = bc.backtracking_algorithm
        self.greedy = gr.greedy_algorithm

    def test_algorithms(self):
        # Getting minimum number of colors using brute force
        bb = self.brute_force(number_of_nodes, edges)
        answer = len(bb.perform_brute_force_algorithm())

        # Compare greedy algorithm with brute force
        greedy = self.greedy(number_of_nodes, edges)
        result = len(greedy.perform_greedy_algorith())
        self.assertEqual(result, answer)

        # Compare back_tracking algorithm with brute force
        back_tracking = self.backtracking(number_of_nodes, adj_matrix, 3)
        result = len(back_tracking.backtracking())
        self.assertEqual(result, answer)
