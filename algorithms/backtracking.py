from algorithms.headers import *


def convert_to_adj_matrix(adj_vector, number_of_vertices):
    # Initialize a matrix
    matrix = [[0 for j in range(number_of_vertices)]
              for i in range(number_of_vertices)]
    for column, row in adj_vector:
        matrix[row][column] = 1
        matrix[column][row] = 1
    return matrix


class backtracking_algorithm:

    def __init__(self, vertices, adj_vector, backtrack_value):
        self.vertices = vertices
        self.adj_matrix = convert_to_adj_matrix(adj_vector, vertices)
        self.backtrack_value = backtrack_value
        self.used_colors = list()

    # A helper function to check if the current color assignment is safe for vertices
    def is_safe(self, vertices, color, c):
        for vertex in range(self.vertices):
            if self.adj_matrix[vertices][vertex] == 1 and color[vertex] == c:
                return False
        return True

    # A recursive helper function to solve m coloring problem
    def graph_colour_helper(self, backtrack_value, colors, vertices):
        if vertices == self.vertices:
            return True

        for color in range(1, backtrack_value + 1):
            if self.is_safe(vertices, colors, color):
                colors[vertices] = color
                if self.graph_colour_helper(backtrack_value, colors, vertices + 1):
                    return True
                colors[vertices] = 0

    def backtracking(self):
        colors_id = [0] * self.vertices
        if self.graph_colour_helper(self.backtrack_value, colors_id, 0) is None:
            return False

        # Print the solution
        print("Coloring the graph using backtracking algorithm.\n")
        for vertex, color in zip(range(self.vertices), colors_id):
            self.used_colors.append(colors[color])
            print(f'Color assigned to vertex {vertex} is {self.used_colors[vertex]}')
        return self.used_colors

    def draw_graph(self):
        G = nx.from_numpy_array(np.array(self.adj_matrix))
        nx.draw(G, node_color=self.used_colors, with_labels=True)
        plt.show()
