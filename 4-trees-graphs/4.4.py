from collections import defaultdict

def depthLists(root, depth=0, depthMap=None):
    """ method which accepts a graph and creates a linked list of all the nodes at each depth """
    if not root:
        return 
    depthMap = depthMap or defaultdict(list)
    depthMap[depth].append(root)
    depthLists(root.left, depth+1, depthMap)
    depthLists(root.right, depth+1, depthMap)
    return list(depthMap.values())

def depthListsBFS(root):
    """ method which gets the depth linked lists using a modified BFS """
    if not root:
        return []
    result = []
    current = [root]
    while current:
        result.append(current)
        parents = current
        current = []
        for node in parents:
            if node.left:
                current.add(node)
            if node.right:
                current.add(node)
    return result
