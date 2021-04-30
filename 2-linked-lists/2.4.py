class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self, head):
        self.head = head

def partition(ll, x):
    """ Partition the linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x """
    less_ll = more_ll = less_end = more_end = None
    crnt = ll.head
    while crnt:
        if crnt.data > x:
            if more_end:
                more_end.next = Node(crnt.data)
                more_end = more_end.next
            else:
                more_end = more_ll = Node(crnt.data)
        else:
            if less_end:
                less_end.next = Node(crnt.data)
                less_end = less_end.next
            else:
                less_end = less_ll = Node(crnt.data)
        crnt = crnt.next
    if (not less_ll): #Case of no less than numbers
        return right_ll
    less_end.next = more_ll
    return less_ll
