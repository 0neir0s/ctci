from math import inf

def getBSTArray(root, bstArray=[]):
    """ array resulting from in-order traversal of the root """
    if not root:
        return bstArray
    getBSTArray(root.left, bstArray)
    bstArray.append(root.data)
    getBSTArray(root.right, bstArray)
    return bstArray

def isBSTv1(root):
    """ By using in-order traversal """
    elems = getBSTArray(root)
    for i in range(1,len(elems)):
        if elems[i-1] > elems[i]:
            return False
    return True

def isBST(root, minimum=-inf, maximum=inf):
    """ Check if a binary tree is a binary search tree """
    if not root:
        return True
    if not (minimum <= root.data <= maximum):
        return False
    if (not isBST(root.left, minimum, root.data) or (not isBST(root.right, root.data, maximum)):
        return False
    return True
