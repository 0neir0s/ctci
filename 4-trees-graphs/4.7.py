# To find the common ancestor of two nodes

def covers(root, a):
    """ Check if a is in the sub-tree of root """
    if not root:
        return False
    if a == root:
        return True
    return covers(root.left, a) or covers(root.right, a)

def commonAncestor(root, a, b):
    """ Find the first common ancestor of the 2 nodes in a binary tree
        X(n) = 2*X(n/2) + O(n) => X(n) = O(n) """
    if not root:
        return False
    if a == root or b == root:
        return root
    aInLeft, bInLeft = covers(root.left, a), covers(root.left, b)
    if aInLeft != bInLeft:
        return root
    subTree = root.left if aInLeft else root.right
    return commonAncestor(subTree, a, b)

def commonAncestorV2(root, a, b):
    """ Find the first common ancestor of the 2 nodes in a binary tree in a more efficient manner """
    if not root:
        return False, None
    if a == b:
        return True, root
    lFoundAncestor, lAncestor = commonAncestorV2(root.left, a, b)
    if lFoundAncestor:
        return True, lAncestor
    rFoundAncestor, rAncestor = commonAncestorV2(root.right, a, b)
    if rFoundAncestor:
        return True, rAncestor
    if lAncestor and rAncestor:
        return True, root
    if root in [a,b]:
        return lAncestor or rAncestor, root
    return False, lAncestor or rAncestor
