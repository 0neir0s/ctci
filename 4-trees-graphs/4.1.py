import math

def height(root):
    """ Height of the binary tree given its root """
    if not root:
        return 0
    return 1 + max(height(root.left),height(root.right))

def isBalancedBT(root):
    """ check if the binary tree is balanced """
    leftStatus = not root.left or isBalancedBT(root.left)
    if not leftStatus:
        return False
    rightStatus = not root.right or isBalancedBT(root.right)
    if not rightStatus:
        return False
    return math.abs(height(root.left) - height(root.right)) < 2

def isBalancedBTv2(root):
    """ Check if the binary tree is balanced without unnecessary height computations """
    if not root:
        return True, 0
    isLeftBalanced, leftHeight = isBalancedBTv2(root.left)
    if not isLeftBalanced:
       return False, leftHeight
    isRightBalanced, rightHeight = isBalancedBTv2(root.right)
    if not isRightBalanced:
        return False, rightHeight
    return math.abs(rightHight - leftHeight)<2, 1 + max(rightHeight, leftHeight)
