from collections import deque
from time import time

class Animal(object):
    pass

class Cat(Animal):
    pass

class Dog(Animal):
    pass

class Farm(object):
    def __init__(self):
        self.queues = { Dog: deque(),
                        Cat: deque() }

    def enqueue(self, animal):
        """ Depending on the animal, put it in the correct queue with the timestamp """
        self.queues[type(animal)].append((time(), animal))

    def dequeueAny(self):
        """ Dequeue the oldest animal """
        if not self.queues[Cat]:
            return self.dequeueDog()
        if not self.queues[Dog]:
            return self.dequeueCat()
        oldestCat = self.queues[Cat][0][0]
        oldestDog = self.queues[Dog][0][0]
        return self.dequeueCat() if oldestCat > oldestDog else self.dequeueDog()

    def dequeueCat(self):
        self.queues[Cat].popleft()

    def dequeueDog(self):
        self.queues[Dog].popleft()
