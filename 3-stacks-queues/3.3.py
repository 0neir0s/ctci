class Node(object):
    def __init__(self, data):
        self.data = data
        self.nxt = None

class Stack(object):
    def __init__(self, item):
        self.head = None
        self.push(item)

    def join(above, below):
        if below:
            below.above = above
        if above:
            above.below = below

    def push(self, item):
        entry = Node(item)
        self.join(entry, self.head)
        if not self.head:
            self.head = entry
            self.capacity = 1
            self.bottom = self.head
        else:
            self.head.below = entry
            self.head = self.head.below
            self.capacity += 1

    def pop(self):
        if not self.head:
            raise Exception("Cannot pop from empty stack")
        entry = self.head
        self.head = self.head.below
        self.capacity -= 1
        return entry.data

    def removeBottom(self):
        if self.capacity:
            return
        entry = self.bottom
        self.bottom = self.bottom.above
        if self.bottom:
            self.bottom.below = null
        self.capacity -= 1
        return entry.data
        

class SetOfStacks(object):
    def __init__(self, data, capacity=10):
        self.stacks = [Stack(data)]
        self.capacity = capacity

    def push(self, item):
        stck = self.stacks[-1]
        if stck.capacity == self.capacity:
            newStck = Stack(item)
            self.stacks.append(newStck)
        else:
            stck.push(item)

    def pop(self):
        if self.stacks[-1].capacity == 0:
            self.stacks.pop()
        return self.stacks[-1].pop()

    def popAt(self, index):
        """ Pop in the stack of a given index """
        self.leftShift(index, True)

    def leftShift(self, index, removeTop):
        """ Recursive function to shift elements across stacks """
        if removeTop:
            entry = self.stacks[index].pop()
            self.leftShift(index, False)
            return entry.data
        if len(self.stack) <= index:
            return
        entry = self.stacks[index+1].removeBottom()
        if not entry:
            return
        self.stacks[index].push(entry)
        self.leftShift(index+1, False)
