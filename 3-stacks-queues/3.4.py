class Node(object):
    def __init__(self, data):
        self.data = data
        self.nxt = None

class Tower(object):
    def __init__(self):
        self.head = None

    def push(self, item):
        if not self.head:
            self.head = Node(item)
        else:
            self.head.next = Node(item)
            self.head = self.head.next

    def pop(self):
        if not self.head:
            raise Exception("Pop from an empty stack")
        entry = self.head
        self.head = self.head.next
        return entry.data

source = Tower()
buffer = Tower()
destination = Tower()

for i in range(1,6):
    source.push(i)

def towerOfHanoi(source, buffer, destination, N):
    """ Classic tower of Hanoi using 3 stacks """
    if N <= 0:
        return
    towerOfHanoi(source, destination, buffer, N-1)
    entry = source.pop()
    destination.push(entry)
    towerOfHanoi(buffer, source, destination, N-1)


