import sys
import copy

from collections import deque

IMPOSSIBLE = 9999999

def steps_to_goal_new(maze, s, g, m, n):

     # Maze will have 4 possible states
    pmaze = []
    pmaze.append(process(copy.deepcopy(maze)))
    pmaze.append(process(rotate(copy.deepcopy(maze))))
    pmaze.append(process(rotate(rotate(copy.deepcopy(maze)))))
    pmaze.append(process(rotate(rotate(rotate(copy.deepcopy(maze))))))

    ps = [(i, j) for i in range(m) for j in range(n)]
    colors = {(p, t): "white" for p in ps for t in range(4)}
    dist = {(p, t): IMPOSSIBLE for p in ps for t in range(4)}

    colors[(s, 0)] = "gray"
    dist[(s, 0)] = 0

    q = deque()
    q.append((s, 0))
    while len(q) > 0:
        u = q.popleft()
        p1, t = u
        i, j = p1

        adj = [(i - 1, j), (i, j + 1), (i + 1, j), (i, j -1)]
        nt = (t + 1) % 4
        adj = [(p, nt) for p in adj]
        def valid_adj(a):
            p, t = a
            i, j = p
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if pmaze[t][i][j] in "b^>v<#":
                return False
            return True
        adj = [a for a in adj if valid_adj(a)]

        for v in adj:
            if colors[v] == "white":
                colors[v] = "gray"
                dist[v] = dist[u] + 1
                q.append(v)
        colors[u] = "black"

    return min([dist[(g, t)] for t in range(4)])

def process(maze):
    d = {"^": [], ">": [], "v": [], "<": []}
    for i, row in enumerate(maze):
        for j, e in enumerate(row):
            if e in "^>v<":
                d[e].append((i,j))
    
    for i, j in d[">"]:
        pre = maze[i][:j + 1]
        rem = list(maze[i][j + 1:])
        for l, e in enumerate(rem):
            if e == ".":
                rem[l] = "b"
            if e in "^>v<#":
                break
        rem = "".join(rem)
        maze[i] = pre + rem

    for i, j in d["<"]:
        pre = list(maze[i][:j])
        rem = maze[i][j:]
        for l, e in reversed(list(enumerate(pre))):
            if e == ".":
                pre[l] = "b"
            if e in "^>v<#":
                break
        pre = "".join(pre)
        maze[i] = pre + rem

    for i, j in d["v"]:
        for k in range(i + 1, m):
            if maze[k][j] == ".":
                maze[k] = list(maze[k])
                maze[k][j] = "b"
                maze[k] = "".join(maze[k])
            if maze[k][j] in "^>v<#":
                break

    for i, j in d["^"]:
        for k in range(i - 1, -1, -1):
            if maze[k][j] == ".":
                maze[k] = list(maze[k])
                maze[k][j] = "b"
                maze[k] = "".join(maze[k])
            if maze[k][j] in "^>v<#":
                break
    return maze

def rotated_symbol(s):
    if s == "^":
        return ">"
    if s == ">":
        return "v"
    if s == "v":
        return "<"
    if s == "<":
        return "^"
    return s

def rotate(maze):
    for i, r in enumerate(maze):
        maze[i] = "".join([rotated_symbol(s) for s in r])
    return maze

if __name__ == '__main__':
    fname = sys.argv[1]
    with open(fname) as f:
        t = int(f.readline())
        for c in range(1, t + 1):
            m, n = [int(x) for x in f.readline().strip().split()]

            s = None
            g = None
            maze = []
            for i in range(m):
                row = f.readline().strip()
                if "S" in row:
                    j = row.index("S")
                    s = (i, j)
                    row = row.replace("S", ".")
                if "G" in row:
                    j = row.index("G")
                    g = (i, j)
                    row = row.replace("G", ".")
                maze.append(row)

            r = steps_to_goal_new(maze, s, g, m, n)
            r = "impossible" if r == IMPOSSIBLE else str(r)
            print "Case #%d: %s" % (c, r)
