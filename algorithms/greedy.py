from algorithms.headers import *


class Graph:
    def __init__(self, edges, numebr_of_nodes):
        self.adjList = [[] for _ in range(numebr_of_nodes)]
        # Create corresponding undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


class greedy_algorithm:
    number_of_nodes: int
    edges: []
    color: []

    def __init__(self, number_of_nodes, edges):
        self.edges = edges
        self.number_of_nodes = number_of_nodes

    def greedy(self, graph):
        vertex_color_list = {}

        # assign a color to vertex one by one
        for vertex_index in range(self.number_of_nodes):
            assigned_color_to_adj_nodes = set(
                [vertex_color_list.get(i) for i in graph.adjList[vertex_index] if i in vertex_color_list])
            # check for the first free color
            color = 1
            for color_index in assigned_color_to_adj_nodes:
                if color != color_index:
                    break
                color = color + 1
            vertex_color_list[vertex_index] = color
            used_colors = []
        print("Coloring the graph using greedy algorithm.\n")
        for vertex in range(self.number_of_nodes):
            used_colors.append(colors[vertex_color_list[vertex]])
            print(f'Color assigned to vertex {vertex} is {used_colors[vertex]}')
        return used_colors

    def draw_graph(self):
        G = nx.Graph()
        G.add_node(self.number_of_nodes - 1)
        G.add_edges_from(self.edges)
        nx.draw(G, node_color=color, with_labels=True)
        plt.show()

    def perform_greedy_algorith(self):
        # build a graph from the given edges
        graph = Graph(self.edges, self.number_of_nodes)

        # Perform greedy algorithm on the given graph
        global color
        color = self.greedy(graph)
