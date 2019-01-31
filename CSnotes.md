### 1 Bit = 8 Bytes
The byte was originally the smallest number of bits that could hold a single character from ASCII.
Since 2^8 = 256 (ranging from 0000-0000 to 1111-1111), every (extended) ASCII covers a single byte.
http://www.asciitable.com/
Earlier, for classical ASCII we used 7 bits and the 8th one for avoiding errors as parity bit.

### ASCII and Unicode (UTF-8)
ASCII covered English, extended ASCII the Latin and Unicode all characters from all languages. UTF-8 and UTF-16 are variable length encodings. In UTF-8, a character may occupy a minimum of 8 bits. Unicode defines (less than) $2^{21}$ characters, which, similarly, map to numbers $0–2^{21}$ (though not all numbers are currently assigned, and some are reserved). Unicode is a superset of ASCII, and the numbers 0–128 have the same meaning as in ASCII.

### Sorting in Python
In Python, the `sorted()` function is Timsort, which is a hybrid of merge sort and selection sort. Timsort first analyses the list it is trying to sort and then chooses an approach based on the analysis of the list. If the array we are trying to sort has fewer than 64 elements in it, Timsort will execute an insertion sort.
![image.png](attachment:image.png)


# Problem solving trade-offs
- **Time vs. Space complexity:** Often the we trade the time complexity improvement for the more space needed. **Dynamic programming** is another example where the time of solving problems can be decreased by using more memory.
**Example:** Traditional recurrent Fibonaci (O(2^n)) vs. memoized Fibonacci (O(n)).
- **How fast can we spot the wrong input / non-existent solution?** All corner cases should be treated before the main function if possible. 
- **Near-best scenario vs. worst case:** Since we often design an algo approach to treat the worst case scenario, this can actually damage the near-best case. 
**Example:** Quick sort (O(nlog(n))) is slower than Bubble sort (O(n^2)) if a single element is misplaced.
- **Too much data:** It is also common that the whole input is too large to fit into memory, or if the input arrives as a stream. The answer is usually a divide-and-conquer approach — perform distributed processing of the data and only read certain chunks of the input from disk into memory, write the output back to disk and combine them later.


# Questions collected by Dano

- What’s the difference between TCP and UDP?  
- What are the tradeoffs? Memmory/Cpu, Throughput/Latency, Robustness/Scalability, …
- What’s the difference between Threads and Processes
- Verify a tree has the binary tree property.
- String match with any permutation of the pattern.
- eval(a+b) like expressions
- How does Unix pipe work?
- Slice a file.
- IP address regexp match.
- Python dictionary merge? Then sort by values.
- Git rebase, you want to fix commits A, B, C with A’, B’, C’
- (Any language) Increment a number in an array based representation
- You’ve an infinitely long streaming log, you want to maintain a uniformly random sample of size K.
- vImplement SetInterval(i,j,value) and GetValue(i)
- How does a max distribution of K (first K=2) uniformly random variables look like?
- Design interest recommendation
- Design knowledge graph