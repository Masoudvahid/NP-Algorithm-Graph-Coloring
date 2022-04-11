class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    # A helper function to check if the current color assignment is safe for vertex v
    def is_safe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    # A recursive helper function to solve m coloring problem
    def graph_colour_helper(self, m, colour, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.is_safe(v, colour, c) == True:
                colour[v] = c
                if self.graph_colour_helper(m, colour, v + 1) == True:
                    return True
                colour[v] = 0

    def backtracking(self, m):
        colour = [0] * self.V
        if self.graph_colour_helper(m, colour, 0) is None:
            return False

        # Print the solution
        print("Solution exist and Following are the assigned colours:")
        for c in colour:
            print(c, end=' ')
        return True


# Driver Code
g = Graph(4)
g.graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
m = 3
g.backtracking(m)
