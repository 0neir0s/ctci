class Node(object):
    def __init__(self,data):
        self.data = data
        self.nxt = None

class Stack(object):
    def __init__(self, top):
        self.top = top

    def pop(self):
        if not self.top:
            return None
        output = self.top.data
        self.top = self.top.next
        return output

    def push(self, data):
        elem = Node(data)
        elem.next = self.top
        self.top = elem

    def peek(self):
        if not self.top:
            return None
        return self.top.data

class Queue(object):
    def __init__(self, start):
        self.first = self.last = start

    def enqueue(self, item):
        if not self.first:
            self.first = self.last = Node(item)
        else:
            self.last.next = Node(item)
            self.last = self.last.next

    def dequeue(self):
        if not self.first:
            return None
        item = self.first
        self.first = self.first.next
        return item.data

