from collections import defaultdict, deque

class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, a, b):
        self.graph[a].append(b)

def dfs(graph, v, visited):
    """ DFS: Recursive function accepting a v and visited set """
    if not v:
        return
    visit(v)
    visited.add(v)
    for node in graph[v]:
        if node in visited:
            continue
        dfs(graph, node, visited)

def bfs(graph, v):
    q, visited = deque(), {v}
    visit(v)
    q.append(v)
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if neighbor in visited:
                continue
            visit(neighbor)
            visited.add(neighbor)
            q.append(neighbor)
