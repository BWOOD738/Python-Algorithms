
"""
A stack is a linear data structure that stores items
in a Last-in/First out (LIFO) or First-in/Last out (FILO)
manner. In a stack, a new element is added at one end 
and an element is removed from that end only. The insert
and delete operations are often called push and pop.

Functions associated with stack are:

empty() - Returns whether or not the stack is empty. 
TIme complexity is O(1)

size() - return the size of the stack.

top() - Returns a reference to the top most element of
the stack.

push(h) - Would add "h" to the top of the stack.

pop() - Deletes the top most element of the stack.

Implementation:
Can use a list, collections.deque from the collections module.
queue.LifoQueue from the queue module.
"""
# Imolementing using a list:

stack = []

#append() to push element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print("Initial stack:")
print(stack)

#pop() to remove elements in LIFO order
print("\nElements removed:")
print(stack.pop())
print(stack.pop())

print("\nStack after the pop functions:")
print(stack)

#this is a stack implementaion using the collections module
"""
from collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')

print("Initial Stack: ")
print(stack)

# pop function to remove elements in LIFO order
print("\nPopped from the stack: ")
print(stack.pop())

print("\nElements remianing: ")
print(stack)
"""

"""
The queue module has a LIFO queue, which is essentially
a stack. Data is inserted using the put() function and
get() takes data out from the Queue.

Functiions:

maxsize() - Number of items allowed in the queue.
empty() - Return True if the queue is empty.
full() - True if there are maxsizes in the queue.
get() - Remove and return an item from the queue.
get_nowait() - Return an item if one is immediately available.
put(item) - Put item into the queue.
put_nowait(item) - Put item into the queue without blocking it.
qsize() - Return number of items in the queue.

"""

"""
#Implementation:
from queue import LifoQueue
 
# Initializing a stack
stack = LifoQueue(maxsize = 3)
 
# qsize() show the number of elements
# in the stack
print(stack.qsize())
  
# put() function to push
# element in the stack
stack.put('a')
stack.put('b')
stack.put('c')
 
print("Full: ", stack.full())
print("Size: ", stack.qsize())
 
# get() fucntion to pop
# element from stack in
# LIFO order
print('\nElements poped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())
 
print("\nEmpty: ", stack.empty())
"""