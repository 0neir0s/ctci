class Node (object):
    def __init__ (self,data):
        self.data = data
        self.next = None

class LinkedList (object):
    def __init__(self,head):
        self.head = head

def getKthToLast(ll, k):
    """ get the kth element from the last of the linked list
        Throws Exception if linked list has less than k elements """
    prev = ll.head
    for _ in range(k-1):
        prev = prev.next
    crnt = prev.next
    while crnt.next:
        prev = crnt
        crnt = crnt.next
    return prev
