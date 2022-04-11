from algorithms.headers import *

class Graph:
    def __init__(self, edges, numebr_of_nodes):
        self.adjList = [[] for _ in range(numebr_of_nodes)]
        # Create corresponding undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


def greedy(graph, number_of_nodes):
    vertex_color_list = {}

    # assign a color to vertex one by one
    for vertex_index in range(number_of_nodes):
        assigned_color_to_adj_nodes = set(
            [vertex_color_list.get(i) for i in graph.adjList[vertex_index] if i in vertex_color_list])
        # check for the first free color
        color = 1
        for color_index in assigned_color_to_adj_nodes:
            if color != color_index:
                break
            color = color + 1
        vertex_color_list[vertex_index] = color
        used_colors = ["white"]
    for vertex in range(number_of_nodes):
        used_colors.append(colors[vertex_color_list[vertex]])
        print(f'Color assigned to vertex {vertex} is {used_colors[vertex]}')
    return used_colors

number_of_nodes = 6
edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]

# build a graph from the given edges
graph = Graph(edges, number_of_nodes)

# Perform greedy algorithm on the given graph
color  = greedy(graph, number_of_nodes)

# Draw the graph
G = nx.Graph()
G.add_node(6)
G.add_edges_from(edges)
nx.draw(G, node_color=color)
plt.show()
