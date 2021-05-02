class MQueue(object):
    def __init__(self):
        self.insertStack = Stack()
        self.bufferStack = Stack()
        self.enqueueMode = True

    def enqueue(self, item):
        if not self.enqueueMode:
            while self.bufferStack.head:
                self.insertStack.push(self.bufferStack.pop())
            self.enqueueMode = True
        self.insertStack.push(item)

    def dequeue(self):
        if self.enqueueMode:
            while self.insertStack.head:
                entry = self.insertStack.pop()
                self.bufferStack.push(entry)
            self.enqueueMode = False
        return self.bufferStack.pop()
