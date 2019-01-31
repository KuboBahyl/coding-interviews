# Data Structures
- storing and organizing data so that we can manipulate with them efficiently

### Linear
- elements accessed in sequential order
- Array, Linked List, Stack, Queue

### Non-linear
- elements are stored in groups / in other way
- Trees, Graphs

### Abstract DS
- defined behavior (operations), free implementation approach
- Linked List (single, double-linked), Stack (storing more than a single value), Queue (circular), Tree (binary), Hash Table, ...


# Arrays
- storing in contiguous locations
- single allocated block with starting index
- similar data types in array
- all elements indexed from 0 to n-1
- array size should be declared during creation
- in Python, Array is generalized to List

### Operations:
- access: O(1)
- search: O(n)
- insert: O(n)
- delete: O(n)

### Downsides:
- static array size
- one block allocation: what if there is no free block?
- not good for insertions
![image.png](attachment:image.png)


# Linked Lists
- DS for collections of data
- dynamic linear DS
- elements connected via pointers (value + pointer)
- last pointer points to Null
- single, double-linked lists (single is never used)
- easy growing and shrinking during execution
- not wasting consecutive memory (althought it takes extra space for the pointers)

### Operations:
- access: O(n)
- search: O(n)
- insert: O(1)
    - obv O(n) if inserting to the end
- delete: O(1)


### Downsides:
- slow in accessing the n-element (common operation)
- uses more storage than Array
![image.png](attachment:image.png)


# Stacks
- linear data structure with LIFO operations: push and pop
- examples
    - balancing parenthesis
    - infix to postfix conversion
    - function calls (recursion)
    - undo button in apps
    - tree traversals

## Operations:
- access: O(n)
- search: O(n)
- insert: O(1) = push
- delete: O(1) = pop

## Disadvantages:
- predefined stack size
![image.png](attachment:image.png)


# Queues
- linear data structure with FIFO operations: enqueue, dequeue
- ensures the ordering
- 3 types of Queues:
    - Deque (Double ended queue): insert and delete at both the ends
    - Circular: last position is connected back to front (circle)
    - Priority: elements added based on their priorities

## Operations:
- access: O(n)
- search: O(n)
- insert: O(1) = enqueue
- delete: O(1) = dequeue


## Disadvantages:
- predefined stack size
- bla
![image.png](attachment:image.png)


# Hash set
- an unordered collection of unique and immutable objects
- works as set in mathematics


# Hash table
- an array storing pointers to values: ability to call value with any key
- called "dictionary" in Python
- Hash function: converts a given big value to a small practical integer value, used as an index in Hash table. 
- Collision handling: can happen that two keys point to the same value (solvable by chaining)

## Operations:
- access: Not defined
- search: O(1)
- insert: O(1)
- delete: O(1)
![image.png](attachment:image.png)


# Trees
- hierarchical structure
- number of nodes: $2^d - 1$, where $d$ is the tree depth 
- number of leafs = number of nodes + 1

## Operations (all trees):
- access: O(log(n))
- search: O(log(n))
- insert: O(log(n))
- delete: O(log(n))

![image.png](attachment:image.png)


# Binary search tree
- node.left always smaller than node.val and node.right always bigger
- all left subtree vals always smaller than node.val and all right subtrees vals always bigger
- when feeding the tree, the subtrees are recursively also binary search trees
- cannot have the same value multiple times
- all values accesible and insertable in O(log(n)) time
![image.png](attachment:image.png)


# Heaps
- balanced binary tree
- either min heap or max heap
- representation of array - root is at index 1 for simplicity
- good for storing the sorted arrays
- given node at index $i$, location of:
    - left child: $2i$ 
    - right child: $2i+1$
    - parent: $i/2$
    
- example problems:
    - K’th smallest elem in an array
    - Sort an almost sorted array
    - merge K sorted arrays

## Operations:
- build: O(n)
- search: O(n)
- insert: O(log(n))
- delete: O(log(n))

![image.png](attachment:image.png)


# Graphs
- set of nodes (vertices) with edges
- edges can be directed or biderectional, can have value
- Representations:
    - matrix of edges
    - list containing nodes with a list of edges

## Operations:
- store graph: List: O(V+E), Matrix: O(V * V)
- add vertex: List: O(1), Matrix: O(V * V)
- add edge: List: O(1), Matrix: O(1)
- delete vertex: List: O(E), Matrix: O(V * V)
- delete edge: List: O(V), Matrix: O(1)

## Disadvantages:
- List: slow in removing vertices and edges (good only adding vertices)
- Matrix: slow in all vertices operation (good when vertices are fixed)

![image.png](attachment:image.png)


