class Graph:
    def __init__(self):
        self.vertices = []
        self.adj = {}

    def add_edge(self, v1, v2):
        if v1 not in self.adj:
            self.adj[v1] = []
        if v2 not in self.adj:
            self.adj[v2] = []

        self.adj[v1].append(v2)
        self.adj[v2].append(v1)

    def add_edge_by_index(self, i1, i2):
        v1 = self.vertices[i1]
        v2 = self.vertices[i2]
        self.add_edge(v1, v2)

class Vertex:
    def __init__(self, content):
        self.content = content
