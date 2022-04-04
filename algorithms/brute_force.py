def brute_force(vertices, edges):
    number_of_nodes = len(vertices)
    for vertex_index in range(number_of_nodes):
        vertices[vertex_index].color = 0
    if number_of_nodes == 1:
        return
    else:
        # for
        pass

class vertex:
    def __init__(self, name, color):
        self.name = name
        self.color = color


vertices = (vertex(1, -1), vertex(2, -1), vertex(3, -1))
edges = ((1, 2), (2, 1), (3, 1))
brute_force(vertices, edges)
