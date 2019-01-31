# Longest sorted subsequence 2 - return the lenght of the longest ordered sublist
# Input :
arr = [10, 22, 9, 33, 21, 50, 41, 60]


# Output : Length of LIS = 4
# The longest increasing subsequence is {3, 7, 40, 80}

def longest_sorted(myList: list):
    n = len(myList)
    lengths = [1] * n

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j] and lengths[j] >= lengths[i]:
                lengths[i] = lengths[j] + 1

    return max(lengths)


longest_sorted(arr)