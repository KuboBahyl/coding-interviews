# SELECTION SORT
# search for minimum and swap it to the front of stack
# O(n^2)
def selection_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    for i in range(n):
        pos = i

        for j in range(pos + 1, n):
            if arr[j] < arr[pos]:
                pos = j

        swap(i, pos)
    return arr