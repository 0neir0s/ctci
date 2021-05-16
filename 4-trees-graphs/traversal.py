from collections import defaultdict, deque

class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, a, b):
        self.graph[a].append(b)

def dfs(graph):
    """ DFS: Recursive function accepting a v and visited set """
    def dfsFrom(node):
        if node in visited:
            return
        visited.add(node)
        visit(node)
        for neighbor in graph[node]:
            dfsFrom(neighbor)
    visited = set()
    dfsFrom(graph.keys()[0])

def dfsi(graph, v):
    s, visited = [], set()
    while s:
        node = s.pop()
        if node in visited:
            continue
        visited.add(node)
        visit(node)
        for neighbor in graph[node]:
            s.append(v)


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
