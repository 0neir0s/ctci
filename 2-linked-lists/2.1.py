class Node (object):
    def __init__ (self,data):
        self.data = data
        self.next = None

class LinkedList (object):
    def __init__(self,head):
        self.head = head

def removeDuplicates(ll):
    """ Remove duplicates from an (unsorted) linked list """
    crnt, elems, prev = ll.head, set(), None
    while (not crnt):
        if crnt.data in elems:
            prev.next = crnt.next
        else:
            elems.add(crnt.data)
            prev = crnt
        crnt = crnt.next

def removeData(crnt, prev):
    """ Remove duplicates from an (unsorted) linked list O(N), (N)"""
    crnt, prev = ll.head, None
    while (not crnt):
        if crnt.data == d:
            prev.next = crnt.next
        else:
            prev = crnt
        crnt = crnt.next

def removeDuplicateNoBuffer(ll):
    """ Remove duplicates from an (unsorted) linked list without additional space complexity O(N^2), O(1)"""
    crnt = ll.head
    while (not crnt):
        prev = crnt
        removeData(crnt.next, prev)
        crnt = crnt.next
