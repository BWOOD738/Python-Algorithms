"""
A hash table is a data structure used to store 
large amounts of data and can be accessed in O(1) 
time. It uses operations such as search, insert
and delete.

While hashing, the hashing function may lead to a 
collision. This is where two keys will try to be stored
at the same address. We use a process called chaining to 
prevent this. The idea is to make each cell if the table
point to a linked list of records that have the same hash
function value

Performance of hash table:

m = Length of Hash Table
n = Total keys to be inserted in the hash table
 
Load factor lf = n/m 
Expected time to search = O(1 +lf )
Expected time to insert/delete = O(1 + lf)

The time complexity of search insert and delete is 
O(1) if  lf is O(1)
"""

# Example of a python implementation of hashing
def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end = " ")

        for j in hashTable[i]:
          print("->", end = " ")
          print(j, end = " ")
        
        print()

# Creating table as nested list
HashTable = [[] for _ in range(10)]

# Hashing to return key of every value
def Hash(keyValue):
    return keyValue % len(HashTable)

# Function to add values to the hash table
def insert(hashTable, keyValue, value):
 hash_key = Hash(keyValue)
 hashTable[hash_key].append(value)

insert(HashTable, 10, "S")

display_hash(HashTable)