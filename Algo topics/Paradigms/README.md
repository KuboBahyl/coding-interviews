# Greedy algorithms
- always choosig the step that leads to the immediate benefit
- finding local optima instead of global one
- more efficient than Dynamic Programming
- approximation for hard problems

Some of the typical greedy algs:

### Kruskal's minimum spanning tree (MST)
MST is a subgraph of a general graph with V vertices and E edges, that is a tree with a minimal sum over edges. This Tree has V vertices and V-1 edges.
Alg: Always choose the smallest edge that doesn't cause a cycle.

### Prim's MST
Same as Kruskal's MST, but each new vortex has to be connected to the tree.

### Djikstra's shortest path
Same as Prim's MST, but the new vertex has to be the minimal choice from the source.

### Huffman coding
Loss-less compression for encoding characters. E.g. a,b,c,d cannot be encoded as 0, 1, 00, 01 (ambiguity in "0001"). Rather it should be 0, 10, 110, 111.


# Recursive programming
- function calling copy of itself
- needs termination (if ... return ...) // base case
- each time the call is in a simpler form (convergence of smaller problems)
- tail recursion: if the f() basically ends with `return f()`
- memory allocated for functions are stored in stack -> recursionError can occurr if exceeded -> great space requirements
- often exponentoal behavior
![image.png](attachment:image.png)



Typical recursive problems: tree traversals, Hanoi


# Dynamic Programming
- mainly an optimization over plain recursion
- solves the overlapping calculations
- simply store the results of subproblems
- reduces complexity from expo -> poly
![image.png](attachment:image.png)

### Tabulation vs Memoizatation
- tabulation: calculation $x[i] = f(x[i-1])$
    - transition relation is hard to think
    - fast method, no overhead
- memoization: usage of previously computed results
    - requires recursion
    - useful when overlapping certain subproblems
    
    
# Divide and Conquer
- Divide: Break the given problem into subproblems of same type.
- Conquer: Recursively solve these subproblems
- Combine: Appropriately combine the answers
- Image: Merge Sort
- examples: binary search, quicksort, mergesort, 
![image.png](attachment:image.png)


# Backtracking algs
- recursive solution while removing bad solutions
- e.g. Sudoku - if a digit doesn't lead to the solution, we remove it
![image.png](attachment:image.png)


# Branch and Bound
- used for solving combinatorial problems - typically exponentials problems
- based on tree search
- if the best in subtree is worse then the current best, let's ignore this node and subtrees
![image.png](attachment:image.png)