class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self,head):
        self.head = head

def isPalindrome(ll):
    """ Check if a linked list is palindrome """
    crnt = ll.head
    reverse_ll = LinkedList(ll.head)
    while (crnt.next):
        crnt = crnt.next
        elem = Node(crnt.data)
        elem.next = reverse_ll.head
        reverse_ll.head = elem

    crnt, rev_crnt = ll.head, reverse_ll.head
    while (crnt and rev_crnt):
        if crnt.data != rev_crnt.data:
            return False
        crnt, rev_crnt = crnt.next, rev_crnt.next
    return True

def length(ll):
    """ return the length of the linked list """
    crnt, count = ll.head, 0
    while(crnt):
        count += 1
        crnt = crnt.next
    return count

def isPalindrome_v2(ll):
    """ Check if a linked list is palindrome with reduced space complexity """
    ll_len = length(ll)
    if ll_len == 0: return True
    stck, count, crnt = [], 0, ll.head
    for _ in range(ll_len/2):
        stck.push(crnt)
        crnt = crnt.next
    if ll_len % 2:
        crnt = crnt.next
    while crnt:
        elem = stck.pop()
        if elem != crnt.data:
            return False
        crnt = crnt.next
    return True






