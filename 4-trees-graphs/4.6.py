def leftmost(node):
    """ left-most child of the node """
    crnt = node
    while crnt.left:
        crnt = crnt.left
    return crnt

def rightmost(node):
    """ right-most child of the node """
    crnt = node
    while crnt.right:
        crnt = crnt.right
    return crnt

def successor(node):
    ''' find the successor of the node assuming a link to parents exist '''
    if not node:
        return None
    if node.right:
        return leftmost(node.right)
    crnt, parent = node, node.parent
    while parent and crnt == parent.right:
        crnt, parent = parent, parent.parent
    return parent

def predecessor(node):
    """ find the predecessor of the node assuming a link to parents exist """
    if not node:
        return None
    if node.left:
        return rightmost(node.left)
    crnt, parent = node, node.parent
    while parent and crnt == parent.left:
        crnt, parent = parent, parent.parent
    return parent

