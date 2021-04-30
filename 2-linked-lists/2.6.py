class Node(object):
    def __init__(self, data):
        self.data = data
        self.nxt = None

class LinkedList(object):
    def __init__(self, head):
        self.head = head

def loopBeginning(cll):
    """ Given a circular linked list, return the node at the beginning of the loop - v1
    Time complexity: O(n) , Space complexity: O(n) """
    visited = set()
    crnt = cll.head
    while crnt:
        if id(crnt) in visited:
            return crnt
        visited.add(id(crnt))
        crnt = crnt.next
    return None

def loopBeginningClassical(cll):
    """ Given a circular linked list, return the node at the beginning of the loop using the runner method 
    1. Find the first point of collision: this would be (LOOP_SIZE-K)%LOOP_SIZE 
    2. Now, we know that the collision point is K%LOOP_SIZE away 
    3. Move one pointer to head, and then loop until they meet again. That would be K steps later - i.e. the start of the loop """
    slow, fast = cll.head
    while (fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    slow = cll.head
    while (slow != fast):
        slow = slow.next
        fast = fast.next
    return slow

