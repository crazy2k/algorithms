from collections import deque

from graph import Graph, Vertex

WHITE = 0
GRAY = 1
BLACK = 2
INFINIT = 9999

def bfs(g, s):
    for u in g.vertices:
        u.color = WHITE
        u.d = INFINIT
        u.pred = None

    s.color = GRAY
    s.d = 0
    s.pred = None

    q = deque()
    q.append(s)
    while len(q) > 0:
        u = q.popleft()
        for v in g.adj[u]:
            if v.color == WHITE:
                v.color = GRAY
                v.d = u.d + 1
                v.pred = u
                q.append(v)
        u.color = BLACK
        print u.content

#    -- 4 -- 5
#   /
# 0 --- 1 -- 3
#   \   | 
#    -- 2
g = Graph()
g.vertices = [Vertex(i) for i in range(6)]
g.add_edge_by_index(0, 1)
g.add_edge_by_index(1, 3)
g.add_edge_by_index(0, 2)
g.add_edge_by_index(1, 2)
g.add_edge_by_index(0, 4)
g.add_edge_by_index(4, 5)

bfs(g, g.vertices[0])
