import math

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class MinStack(object):
    def __init__(self, item):
        self.head = Node((item,math.inf))

    def mini(self):
        """ returns the current minimum of the stack. """
        if not self.head:
            return None
        return self.head.data[1]

    def push(self, item):
        if not self.head:
            self.head = Node((item, math.inf))
        else:
            self.head.next = Node((item, min(self.mini(), item)))
            self.head = self.head.next

    def pop(self):
        if not self.head:
            return None
        else:
            value = self.head 
            self.head = self.head.next
            return value.data[0]
