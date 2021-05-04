def pathWithRoot(root, total, path=[]):
    """ print path starting from root having a given total """
    if not root:
        return
    if sum(path) == total:
        print path
    path.append(root)
    pathWithRoot(root.left, total, path)
    pathWithRoot(root.right, total, path)
    path.pop()

def pathWithSum(root, total, path=[]):
    """ print any path having a given total """
    if not root:
        return
    path.append(root)
    pathWithSum(root.left, total, path)
    pathWithSum(root.right, total, path)
    partialSum = 0
    for elem in path[::-1]:
        partialSum += elem
        if partialSum == total:
            print(path)
    path.pop()
