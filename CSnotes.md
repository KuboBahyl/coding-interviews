### Sorting in Python
In Python, the `sorted()` function is Timsort, which is a hybrid of merge sort and selection sort. Timsort first analyses the list it is trying to sort and then chooses an approach based on the analysis of the list. If the array we are trying to sort has fewer than 64 elements in it, Timsort will execute an insertion sort.

![alt text](https://cdn-images-1.medium.com/max/1600/1*1CkG3c4mZGswDShAV9eHbQ.png)


# Problem solving trade-offs
- **Time vs. Space complexity:** Often the we trade the time complexity improvement for the more space needed. **Dynamic programming** is another example where the time of solving problems can be decreased by using more memory.
**Example:** Traditional recurrent Fibonaci (O(2^n)) vs. memoized Fibonacci (O(n)).
- **How fast can we spot the wrong input / non-existent solution?** All corner cases should be treated before the main function if possible. 
- **Near-best scenario vs. worst case:** Since we often design an algo approach to treat the worst case scenario, this can actually damage the near-best case. 
**Example:** Quick sort (O(nlog(n))) is slower than Bubble sort (O(n^2)) if a single element is misplaced.
- **Too much data:** It is also common that the whole input is too large to fit into memory, or if the input arrives as a stream. The answer is usually a divide-and-conquer approach — perform distributed processing of the data and only read certain chunks of the input from disk into memory, write the output back to disk and combine them later.

# Other collected questions
- What’s the difference between TCP and UDP?  
- What are the tradeoffs? Memmory/Cpu, Throughput/Latency, Robustness/Scalability, etc.
- What’s the difference between Threads and Processes?
- How does Unix pipe work?
- Python dictionary merge?
- Git rebase, you want to fix commits A, B, C with A’, B’, C’
- Design interest recommendation
- Design knowledge graph
