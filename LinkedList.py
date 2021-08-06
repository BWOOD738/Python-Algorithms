"""
A linked list consists of nodes. Each node has a value and 
a pointer to another node. The starting node is known as a 
header or root node.

ADVANTAGE:

While arrays are set to a certain size of bytes, a linked list
can be dynamic. Arrays also need a sequence of bytes in memory,
but link list can be anywhere. 

DISADVANTAGE:

Linked list can have more time complexity because you have to start
from the beginning of a chain and check each element at a time. 
"""

# First, create a node class
class Node:
    def __init__(self, val):
        self.val = val # the data of the node
        self.next = None # initally the pointer points to nothing

# Once the node class is made you can implement the list like so:
node0 = Node(12)
node1 = Node(3)
node2 = Node(5)

node0.next = node1
node1.next = node2
