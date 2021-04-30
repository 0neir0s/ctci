class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self,head):
        self.head = head

def sumLinkedList(l1, l2):
    """ Add 2 numbers represented by a linked list and return a sum linked list """
    first = l1.head
    second = l2.head
    sum_ll = sum_end = None
    while (first or second):
        total = (first.data if first else 0) + (second.data if second else 0) + carry
        value, carry = total%10, total/10
        if not sum_ll:
            sum_end = sum_ll = LinkedList(Node(value))
        else:
            sum_end.next = Node(value)
            sum_end = sum_end.next
        first = first or first.next
        second = second or second.next
        return sum_ll
