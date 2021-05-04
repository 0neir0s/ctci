class BTNode(object):
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def exampleTree():
    root = BTNode(10)
    i1, i2, i3, i4 = BTNode(5), BTNode(6), BTNode(7), BTNode(8)
    root.left = i1
    root.right = i2
    i1.left = i3
    i2.right = i4

def inOrderTraversal(root):
    """ in-order traversal """
    if not root:
        return
    inOrderTraversal(root.left)
    print(root.data)
    inorderTraversal(root.right)

def preOrderTraversal(root):
    """ pre-order traversal """
    if not root:
        return
    print(root.data)
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)

def postOrderTraversal(root):
    """ post-order traversal """
    if not root:
        return
    postOrderTraversal(root.left)
    postorderTraversal(root.right)
    print(root.data)

class AVLNode(object):
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        self.height = 1

class AVLTree(object):
    def __init__(self):
        self.root = None

    def leftRotate(self, z):
        """ Rotate, adjust the height, and return the new root """
        y, T2 = z.right, y.left
        y.left, z.right = z, T2
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        """ Rotate, adjust the height, and return the new root """
        y, T3 = z.left, y.right
        y.right, z.left = z, T3
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def _insert(self, root, key):
        """ Insert function to insert a key under a root """
        root = root or self.root
        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.data:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        # Step 2 - Update the height of the ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))
        # Step 3 - Get the balance factor
        balance = self.getBalance(root)
        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
        # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
        # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root

    def insert(self, key):
        self.root = self._insert(self.root, key)


def sortedArrayToBalancedTree(sList):
    """ Sorted array to balanced tree 
        Time complexity - O(n) """
    if not sList:
        return None
    index = len(sList)/2
    root = sList[index]
    root.left = sortedArrayToBalancedTree(sList[:index])
    root.right = sortedArrayToBalancedTree(sList[index+1:])
    return root
