
class Node (object):
    def __init__ (self,data):
        self.data = data
        self.next = None

class LinkedList (object):
    def __init__(self,head):
        self.head = head

    def append(self,data):
        """ Function to append to tail of the node """
        node = Node(data)
        crnt = self.head
        while (not crnt.next):
            crnt = crnt.next
        crnt.next = node

    def delete(self,data):
        """ Delete a given node from the linked list """
        if data == self.head.data:
            self.head = self.head.next
            return
        crnt = self.head
        while (not crnt.next):
           nxt = crnt.next
           if nxt.head.data == data:
               crnt.next = nxt.next
               return
           crnt = crnt.next

    def weave(self):
        """ Weave a1 -> a2 -> b1 -> b2 => a1 -> b1 -> a2 -> b2
            Using runner technique to figure out the midpoint
            Then, on each iteration, pluck element and weave it to the front """
        if not self.head:
            return
        slow  = self.head
        fast = slow.next
        while(not fast.next):
            slow, fast = slow.next, fast.next.next
        fast = self.head
        while(not slow.next.next):
            tbm = slow.next
            fast.next, slow.next, tbm.next = tbm, slow.next.next, fast.next
            fast = fast.next.next
