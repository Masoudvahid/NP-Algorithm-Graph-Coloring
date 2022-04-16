import itertools
import cardinality

from algorithms.headers import *


class Graph:
    def __init__(self, edges, number_of_nodes):
        self.adjList = [[] for _ in range(number_of_nodes)]
        # Create corresponding undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


class brute_force:
    number_of_nodes: int
    edges: []
    color: []

    def __init__(self, number_of_nodes, edges):
        self.edges = edges
        self.number_of_nodes = number_of_nodes

    def brute_force(self, graph):
        # colors_list = list(range(1, self.number_of_nodes + 1))
        colors_list = colors[:self.number_of_nodes]
        # Generate all possible combinations of colors for every node
        all_possible_choices = list(itertools.product(colors_list, repeat=self.number_of_nodes))

        def iterate_over_all_edges(possible_choice):
            index = 0
            for edge_i in self.edges:
                if possible_choice[edge_i[0]] == possible_choice[edge_i[1]]:
                    return
                index += 1
                for edge_j in self.edges[index:]:
                    if possible_choice[edge_i[0]] == possible_choice[edge_j[1]] or \
                            possible_choice[edge_i[1]] == possible_choice[edge_j[1]]:
                        return
                return possible_choice

        color = []
        for possible_choice in all_possible_choices:
            if iterate_over_all_edges(possible_choice) != None:
                color.append(iterate_over_all_edges(possible_choice))
        return color

    def draw_graph(self):
        G = nx.Graph()
        G.add_node(self.number_of_nodes - 1)
        G.add_edges_from(self.edges)
        nx.draw(G, node_color=color[1], with_labels=True)
        plt.show()

    def perform_brute_force_algorith(self):
        # build a graph from the given edges
        graph = Graph(self.edges, self.number_of_nodes)

        # Perform greedy algorithm on the given graph
        global color
        color = self.brute_force(graph)
