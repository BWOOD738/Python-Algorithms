"""
A queue is like a stack except it stores items in a First 
In last out manner (FIFO). This means the least recently
added item is the furst one to be removed.

Operations associated with queue:

Enqueue: Adds an item to the queue. If the queue is full,
then it is said to be an Overflow condition.

Dequeue: Removes item from the queue. If the queue is empty,
then there is an underflow condition.

Front: Get the front item from the queue.

Rear: Get the last item from the queue.

Queue can be implemented using a list and python modules.

"""

#Implementation using a list
q = []

q.insert(0, 70) # or append
q.insert(0,56)
q.insert(0, 53)

q.pop() # Returns 70

# Implementation using the collections module
from collections import deque

q = deque()

q.appendleft(4) # appendleft() Used for queue not stack
q.appendleft(2)
q.appendleft(3)

q.pop() # removes 4

# Class implementation

# from collections import deque
class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        return self.buffer.pop()
    
    def isEmpty(self): 
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)