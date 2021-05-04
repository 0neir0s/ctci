from collections import deque

def hasRouteBFS(a, b, graph):
    """ Given two nodes in a graph, check if there is a route between them """
    visited, q = {a}, deque([a])
    while q:
        node = q.popleft()
        if node == b:
            return True
        for neighbor in graph.graph[node]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            q.append(neighbor)
    return False

def hasRouteDFS(a, b, graph, visited = set()):
    """ Same problem as last function done using DFS """
    if a == b:
        return True
    visited.add(a)
    for neighbor in graph.graph[a]:
        if neighbor in visited:
            continue
        if not hasRouteDFS(neighbor, b, graph, visited):
            continue
        return True
    return False
