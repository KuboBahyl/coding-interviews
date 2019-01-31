# given two sorted arrays, find min shared subsequence
arr1 = [1, 2, 3, 5, 6, 7, 20]
arr2 = [3, 6, 7, 8, 20]


# out -> [3,6,7]

def find_subsq(arr1, arr2):
    subsq = []
    if len(arr1) == 0 or len(arr2) == 0:
        return []

    i = j = 0
    M = len(arr1)
    N = len(arr2)

    while i < M and j < N:
        val_i = arr1[i]
        val_j = arr2[j]
        if val_i == val_j:
            subsq.append(arr1[i])
            i += 1
            j += 1
        elif val_i > val_j:
            j += 1
        else:
            i += 1

    return subsq


find_subsq(arr1, arr2)

# time: O(M + N) for M approx = N
# space: worst O(M) where M<N

# however if M >> N, the worst time is O(M*N)
# binary search of arr2 in arr1: worst O(N * log(M))

# let M = N^C, then O(N * log(M)) = O(C * N * log(N)) = O(N*log(N))
# also O(M + N) = O(N^C + N) = O(N^C) for C>=2
# proof: O(N^C) > O(N*log(N)), so the binary search is better