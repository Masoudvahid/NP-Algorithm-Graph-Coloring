import io
from io import StringIO
import sys
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
FAILURE = 'incorrect value'


class graph_coloring_Tests(unittest.TestCase):
    def setUp(self):
        self.brute_force = bf.brute_force
        self.backtracking = bc.backtracking_algorithm
        self.greedy = gr.greedy_algorithm

    def brute_force_testing(self):
        bb = self.brute_force(number_of_nodes, edges)
        ans = bb.perform_brute_force_algorithm()
        should_be = """('aliceblue', 'antiquewhite', 'aliceblue', 'aqua', 'aqua', 'aqua')"""
        self.assertEqual(ans, should_be)


unittest.main()
