# INSERTION SORT
# sort each value to the past
# O(n^2)
def insertion_sort(arr):
    for i in range(len(arr)):
        curr = arr[i]
        pos = i

        while arr[pos - 1] > curr and pos > 0:
            arr[pos] = arr[pos - 1]
            pos -= 1

        arr[pos] = curr
    return arr