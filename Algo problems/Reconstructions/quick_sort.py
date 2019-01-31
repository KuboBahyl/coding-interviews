# QUICK SORT
# Divide and Conquer
# O(nlog(n))
def quick_sort(arr, low=0, high=None):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def partition(low, high):
        pivot = arr[high]
        pivot_idx = low

        for j in range(low, high):
            if arr[j] <= pivot:
                swap(pivot_idx, j)
                pivot_idx += 1

        swap(pivot_idx, high)
        return pivot_idx

    def recursion(low, high):
        if low >= high:
            return

        pivot_idx = partition(low, high)
        recursion(low, pivot_idx - 1)
        recursion(pivot_idx + 1, high)

        return arr

    if high is None:
        high = len(arr) - 1

    return recursion(low, high)