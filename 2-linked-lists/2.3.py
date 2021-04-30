class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self, head):
        self.head = head

def deleteMiddleNode(n):
    """ Utility to delete a node in the middle of a singly linked list, with only access to that node. Cannot work if node is the last element of the list. """
    if not n or not n.next:
        return False
    n.data = n.next.data
    n.next = n.next.next
    return True
