import itertools
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

    def brute_force(self, for_test=0):
        colors_list = colors[:self.number_of_nodes]
        # Generate all possible combinations of colors for every node
        all_possible_choices = list(itertools.product(colors_list, repeat=self.number_of_nodes))

        def iterate_over_all_edges(possible_choice):
            for edge_i in self.edges:
                if possible_choice[edge_i[0]] == possible_choice[edge_i[1]]:
                    return
            starting_index = 0
            for edge_i in self.edges:
                starting_index += 1
                for edge_j in self.edges[starting_index:]:
                    if possible_choice[edge_i[0]] == possible_choice[edge_i[1]]:
                        return
                    if possible_choice[edge_i[0]] == possible_choice[edge_j[1]] or \
                            possible_choice[edge_i[1]] == possible_choice[edge_j[1]]:
                        return
                return possible_choice

        if for_test == 0:
            print("Coloring the graph using brute force algorithm.\n")
        proper_colors = [i for i in set(map(iterate_over_all_edges, all_possible_choices)) if i]
        minimum_color_choice = tuple(map(lambda string: (string, len(set(string))), proper_colors))
        minimum_color_choice = dict(map(reversed, minimum_color_choice))
        best_color_choice = minimum_color_choice[min(minimum_color_choice.keys())]
        for index, used_color in enumerate(best_color_choice):
            if for_test == 0:
                print(f'Color assigned to vertex {index} is {used_color}')
        return best_color_choice

    def draw_graph(self):
        G = nx.Graph()
        G.add_node(self.number_of_nodes - 1)
        G.add_edges_from(self.edges)
        nx.draw_kamada_kawai(G, nodelist=list(range(self.number_of_nodes)), node_color=brute_force.color,
                             with_labels=True)
        plt.show()

    def perform_brute_force_algorithm(self, for_test=0):
        # Perform brute force on the given graph
        brute_force.color = self.brute_force(for_test=for_test)
        return brute_force.color
