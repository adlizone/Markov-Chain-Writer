import random

class Vertex():
    def __init__(self, value):
        self.value = value
        self.adjacent = {}
        self.neighbors = []
        self.neighbors_weights = []

    def __str__(self):
        return self.value+' '+' '.join([node.value for node in self.adjacent.keys()])
        
    def add_edge_to(self, Vertex):
        self.adjacent[Vertex] = self.adjacent.get(Vertex, 0)+ 1
        self.neighbors.append(Vertex)
        self.neighbors_weights.append(self.adjacent[Vertex])


    def next_word(self):
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]

    
class Graph():
    def __init__(self):
        self.Vertices = {}
                               
    def add_vertex(self, value):
        self.Vertices[value] = Vertex(value)

    def get_vertex(self, value):
        if value not in self.Vertices:
            self.Vertices[value] = Vertex(value)
        return self.Vertices[value]

    def get_next_vertex(self, Vertex):
        return self.Vertices[Vertex.value].next_word()


