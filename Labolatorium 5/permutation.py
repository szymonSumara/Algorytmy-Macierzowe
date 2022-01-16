
class Vertex:
    def __init__(self, vertex_id):
        self.neighbors = {}
        self.vertex_id = vertex_id

    def add_neighbor(self, neighbor):
        self.neighbors[neighbor.vertex_id] = neighbor

    def remove_neighbor(self, neighbor):
        del self.neighbors[neighbor.vertex_id]

    def pop_out(self):
        for other_vertex in self.neighbors.values():
            other_vertex.remove_neighbor(self)

    def degree(self):
        return len(self.neighbors)

    def __str__(self):
        return "Vertex " + str(self.vertex_id) + " : " + str([other.vertex_id for other in self.neighbors.values()])

class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id in self.vertices:
            raise Exception('Vertex already added')
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, first_vertex_id, second_vertex_id):
        if first_vertex_id not in self.vertices:
            raise Exception('First of vertices was not added before')

        if second_vertex_id not in self.vertices:
            raise Exception('Second of vertices was not added before')


        self.vertices[first_vertex_id].add_neighbor(self.vertices[second_vertex_id])
        self.vertices[second_vertex_id].add_neighbor(self.vertices[first_vertex_id])

    def remove_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            raise Exception('Vertex is not in the graph')
        self.vertices[vertex_id].pop_out()
        del self.vertices[vertex_id]

    def has_vertex(self, vertex_id):
        return vertex_id in self.vertices

    def get_vertex_neighbors(self, vertex):
        return self.vertices[vertex].neighbors.keys()

    def size(self):
        return len(self.vertices.values())

    def get_min_degree_vertex(self):
        min_degree_vertex_id, min_degree = None, 100000000

        for vertex in self.vertices.values():
            print(min_degree_vertex_id)
            if vertex.degree() < min_degree:
                min_degree_vertex_id = vertex.vertex_id
                min_degree = vertex.degree()

        return min_degree_vertex_id

    def __str__(self):
        return 'Graph:\n' + '\n'.join([str(vertex) for vertex in self.vertices.values()])

    def size(self):
        return len(self.vertices)

def graf_gauss_elimination(graph):
    fill_in_graph = Graph()

    graph_size = graph.size()

    for k in range(graph_size):
        fill_in_graph.add_vertex(k)

    for k in range(graph_size):
        n = graph.get_vertex_neighbors(k)
        graph.remove_vertex(k)
        for i in n:
            for j in n:
                if i != j:
                    graph.add_edge(i, j)
                    fill_in_graph.add_edge(i, j)
    print(fill_in_graph)
# def build_elimination_graph(matrix_in_coordinate_format):
#
#     elimination_graph = Graph()
#
#     val = matrix_in_coordinate_format.VAL
#     irn = matrix_in_coordinate_format.IRN
#     jcn = matrix_in_coordinate_format.JCN
#
#     for (v, r, c) in zip(val, irn, jcn):
#         if not elimination_graph.has_vertex(r):
#             elimination_graph.add_vertex(r)
#
#         if c < r:
#             elimination_graph.add_edge(r, c)
#
#     return elimination_graph


def build_elimination_graph(matrix):

    elimination_graph = Graph()

    for row_index, row in enumerate(matrix):
        for column_index, value in enumerate(row):
            if abs(value) > 10**(-7):
                if not elimination_graph.has_vertex(row_index):
                    elimination_graph.add_vertex(row_index)

                if column_index < row_index:
                    elimination_graph.add_edge(row_index, column_index)

    return elimination_graph

def get_permutation_minimum_degree_algorithm(graph):
    permutation_matrix = [[0 for j in range(graph.size())] for i in range(graph.size())]
    row_position_in_permutation_table = 0

    while graph.size() > 0:
        minimum_degree_vertex_id = graph.get_min_degree_vertex()
        permutation_matrix[row_position_in_permutation_table][minimum_degree_vertex_id] = 1
        print(minimum_degree_vertex_id)
        graph.remove_vertex(minimum_degree_vertex_id)
        row_position_in_permutation_table += 1
    return permutation_matrix