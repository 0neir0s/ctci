TOTAL = 99

class ThreeStacks(object):
    def __init__(self, totalSize):
        self.heads = [None,None,None]
        self.ds = [0]*totalSize
        self.total = totalSize

    def push(self, stackNum, item):
        """ Push item to the required stack. Throws exception if stack length crosses the limit. """
        if not self.heads[stackNum]:
            index = totalSize/3*stackNum
        else:
            if self.heads[stackNum] == (totalSize/3*(stackNum+1))-1:
                raise Exception("Stack full")
            index = self.heads[stackNum] + 1
        self.ds[index] = item
        self.heads[stackNum] = index

    def pop(ds, stackNum, item):
        """ Pop item from the required stack. Throws exception if stack is empty """
        index = self.heads[stackNum]
        if not index:
            raise Exception("Stack empty")
        if index == totalSize/3*stackNum:
            self.heads[stackNum] = None
            return self.ds[index]
        self.heads[stackNum] -= 1
        return self.heads[index]    
