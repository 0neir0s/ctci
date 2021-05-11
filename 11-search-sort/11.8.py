class Node(object):

    def __init__(self, val):
        self.data = val
        self.left = self.right = None
        self.leftCount = 0

class BST(object):

    def __init__(self):
        self.root = None

    def insert(self, val):
        """ Insert element """
        def insertInto(root):
            """ Insert into a binary search tree """
            if root.data > val:
                if self.root.right:
                    insertInto(self.root.right, val)
                else:
                    root.right = Node(val)
            else:
                root.leftCount += 1
                if root.left:
                    insertInto(root.left, val)
                else:
                    root.left = Node(val)

        if not self.root:
            self.root = Node(val)
        else:
            insertInto(self.root)

    def delete(root, val):
        

    def rank(root, elem):
        """ Rank of an element in non-null BST """
        if root.data == elem:
            return 1 + root.leftCount
        elif root.data < elem:
            return rank(root.left, elem)
        else:
            return 1 + root.leftCount + rank(root.right, elem)
