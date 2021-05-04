def sortedArrayToBalancedTree(sList):
    """ Sorted array to balanced tree 
        Time complexity - O(n) """
    if not sList:
        return None
    index = len(sList)/2
    root = Node(sList[index])
    root.left = sortedArrayToBalancedTree(sList[:index])
    root.right = sortedArrayToBalancedTree(sList[index+1:])
    return root
